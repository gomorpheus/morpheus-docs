Cluster Layouts
---------------

|morpheus| includes many different types of Cluster Layouts out-of-the-box which support a number of provisioning technologies. Many of these |morpheus|-provided Cluster Layouts may also be cloned for use in creating custom layouts. Edit or delete user-created Cluster Layouts using the pencil (|pencil|) or trash can (|trash|) icons next to the desired layout on the Cluster Layouts list page. See the next section for an

.. image:: /images/provisioning/library/clusterLayouts.png

.. note:: |morpheus| now syncs available (non-preview) AKS k8s versions daily. Existing synced versions that are no longer supported by Azure are automatically disabled. The table below includes available AKS versions at time of |morphver| release.

- .. toggle-header:: :header: **List of Default System Cluster Layouts**

    .. include:: system_cluster_layouts.rst

Creating Custom Cluster Layouts
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Custer Layouts can be built for an infinite number of use cases and targeting a wide range of configurations or provisioning technologies. However, it still may help to see an example Cluster Layout created. In this section, we'll create an example Cluster Layout which provisions a Kubernetes Cluster to a VMware vCenter Cloud containing a master node and three worker nodes. We'll build out two Node Types to embed in the Cluster, one master and one worker. Within the Node Types, we will embed Script Templates needed to configure the nodes as they are provisioned and allow the workers to join the cluster. Script Templates can be configured to execute at various phases of the lifecycle of the node, similar to a Provisioning Workflow, so |morpheus| can orchestrate the whole process.

Creating Script Templates
`````````````````````````

We'll first start by creating the necessary Script Templates. In this example, I'll use a generic prep script that both the master and worker nodes will utilize and then I'll create three additional scripts (two for the master node and one for the worker nodes) to accomplish various Kubernetes cluster setup tasks (``kubeadm init``, creating Role Bindings, joining workers to the cluster, etc.). I'll briefly describe each here and step through the process of creating the Script Template objects in |morpheus|.

To begin a new Script Template, navigate to |LibTemScr| and click :guilabel:`+ ADD`. All of the scripts used in this example will be "Bash" type, run as user "root" and with SUDO marked.

The first script to add will be a prep script that both the master and worker nodes will use. This script turns swap off, installs ``containerd``, runs updates, sets network config, and installs ``kubelet``, ``kubeadm``, and ``kubectl``. Set this script to run in the PreProvision phase. The complete script, named "k8sprep" in my example can be viewed below:

- .. toggle-header:: :header: **k8sprep Script Template**

    .. code-block:: bash

      function wait_for_dpkg() {
        FRONT_END_LOCK_FILE=/var/lib/dpkg/lock-frontend
        DPKG_LOCK_FILE=/var/lib/apt/lists/lock

        echo "checking for dpkq lock existence..."
        if [ -e "$DPKG_LOCK_FILE" ]; then
          while fuser $DPKG_LOCK_FILE >/dev/null 2>&1 ; do
            echo "Waiting for lock $DPKG_LOCK_FILE..."
            sleep 1
          done
        fi
        echo "checking for dpkq lock-frontend existence..."
        if [ -e "$FRONT_END_LOCK_FILE" ]; then
          while fuser $FRONT_END_LOCK_FILE >/dev/null 2>&1 ; do
            echo "Waiting for lock $FRONT_END_LOCK_FILE..."
            sleep 1
          done
          echo "force removing lock $FRONT_END_LOCK_FILE"
          sudo rm $FRONT_END_LOCK_FILE
          sleep 5
        fi
      }
        # Swap must be turned off see https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/install-kubeadm/
      sudo swapoff -a ; sudo sed -i '/ swap / s/^/#/' /etc/fstab
        # Install containerd packages from Debian sse: https://docs.docker.com/engine/install/ubuntu/
      wait_for_dpkg
      sudo apt-get update
      sudo apt-get install ca-certificates curl gnupg lsb-release -y
      sudo mkdir -m 0755 -p /etc/apt/keyrings
      sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
      sudo mkdir -m 0755 -p /etc/apt/keyrings
      sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpgsudo
      echo   "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
      $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
      sudo apt-get update
        # the Docker documentation advises to install the whole Docker runtime environment but containerd.io is sufficient
      sudo apt-get install containerd.io -y
        # Prepare the necessary network config see: https://kubernetes.io/docs/setup/production-environment/container-runtimes/
      sudo cat <<EOF | sudo tee /etc/modules-load.d/k8s.conf
      overlay
      br_netfilter
      EOF
      sudo modprobe overlay
      sudo modprobe br_netfilter
      sudo cat <<EOF | sudo tee /etc/sysctl.d/k8s.conf
      net.bridge.bridge-nf-call-iptables  = 1
      net.bridge.bridge-nf-call-ip6tables = 1
      net.ipv4.ip_forward                 = 1
      EOF
        # Apply sysctl params without reboot
      sudo sysctl --system
        # Install kubeadm follwing the K8s documentation: https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/install-kubeadm/
      sudo apt-get install -y apt-transport-https ca-certificates curl
      sudo curl -fsSL  https://packages.cloud.google.com/apt/doc/apt-key.gpg|sudo gpg --dearmor -o /etc/apt/trusted.gpg.d/k8s.gpg
      sudo echo "deb https://apt.kubernetes.io/ kubernetes-xenial main" | sudo tee /etc/apt/sources.list.d/kubernetes.list
      sudo apt-get update
      sudo apt-get -y install -y kubelet=1.26.1-00 kubeadm=1.26.1-00 kubectl=1.26.1-00

      sudo apt-mark hold kubelet kubeadm kubectl
        # see https://github.com/etcd-io/etcd/issues/13670
      cat << EOF | sudo tee /etc/containerd/config.toml
      version = 2
        [plugins]
        [plugins."io.containerd.grpc.v1.cri"]
         [plugins."io.containerd.grpc.v1.cri".containerd]
            [plugins."io.containerd.grpc.v1.cri".containerd.runtimes]
              [plugins."io.containerd.grpc.v1.cri".containerd.runtimes.runc]
                runtime_type = "io.containerd.runc.v2"
                [plugins."io.containerd.grpc.v1.cri".containerd.runtimes.runc.options]
                  SystemdCgroup = true
      EOF
      sudo systemctl restart containerd

Next we'll add a script called "kubeadm-init" in this example which will create and configure some working directories, set the ``kubeadm`` config yaml, and run ``kubeadm init``. Set this script to run in the PreProvision phase as well. The complete script can be viewed below:

- .. toggle-header:: :header: **kubeadm-init Script Template**

    .. code-block:: bash

      mkdir -p <%=morpheus.morpheusHome%>/kube
      mkdir -p <%=morpheus.morpheusHome%>/kube/working
      mkdir -p <%=morpheus.morpheusHome%>/.kube
      sudo chown <%=morpheus.morpheusUser%>:<%=morpheus.morpheusUser%> <%=morpheus.morpheusHome%>/kube
      sudo chown <%=morpheus.morpheusUser%>:<%=morpheus.morpheusUser%> <%=morpheus.morpheusHome%>/kube/working
      cat <<EOF | sudo tee <%=morpheus.morpheusHome%>/kube/working/kubeadm-config.yaml
      # kubeadm-config.yaml
      kind: ClusterConfiguration
      apiVersion: kubeadm.k8s.io/v1beta3
      kubernetesVersion: v1.26.1
      networking:
        serviceSubnet: "10.96.0.0/16"
        podSubnet: "10.244.0.0/24"
        dnsDomain: "cluster.local"
      apiServer:
        extraArgs:
          authorization-mode: "Node,RBAC"
      clusterName: "example-cluster"
      ---
      kind: KubeletConfiguration
      apiVersion: kubelet.config.k8s.io/v1beta1
      cgroupDriver: systemd
      EOF
      sudo kubeadm init --config <%=morpheus.morpheusHome%>/kube/working/kubeadm-config.yaml
      sudo cp -i /etc/kubernetes/admin.conf <%=morpheus.morpheusHome%>/.kube/config &&
      sudo chown <%=morpheus.morpheusUser%>:<%=morpheus.morpheusUser%> <%=morpheus.morpheusHome%>/.kube/config

Lastly, we'll add a setup script for the Kubernetes master node called "k8s-master-setup" for this example. This script creates the service account and role bindings. Set this script to run in the PostProvision phase and view the complete script below:

- .. toggle-header:: :header: **k8s-master-setup Script Template**

    .. code-block:: bash

      #create a service account
      cd <%=morpheus.morpheusHome%>
      #kubectl -n kube-system create sa morpheus
      kubectl create sa morpheus
      cat <<EOF | tee <%=morpheus.morpheusHome%>/kube/morpheus-sa.yaml
      apiVersion: v1
      kind: Secret
      metadata:
        name: morpheus-token
        annotations:
          kubernetes.io/service-account.name: morpheus
      type: kubernetes.io/service-account-token
      EOF
      kubectl create clusterrolebinding serviceaccounts-cluster-admin --clusterrole=cluster-admin --group=system:serviceaccounts
      kubectl create -f <%=morpheus.morpheusHome%>/kube/morpheus-sa.yaml
      kubectl apply -f https://raw.githubusercontent.com/projectcalico/calico/v3.25.0/manifests/calico.yaml

The three scripts we've just created will prepare the master node for our cluster. We now need an additional script that will prepare the worker nodes and join them to the cluster. The worker nodes will also use the "k8s-prep" script we added in the very first step which you'll see in the next step when we create the node types.

Add a fourth script which I've called "k8s-join" for this example. This script takes advantage of a special ``joinCommand`` variable as you'll see when you view the full script. If you want to see exactly what this does later, you can create a new Bash script Task that echoes out that variable and run it against an existing Kubernetes worker node VM (``echo "<%=morpheus.kubernetes.joinCommand%>"``). Set this script to run in the PostProvision phase and view the full script below:

- .. toggle-header:: :header: **k8s-join Script Template**

    .. code-block:: bash

      sudo <%=morpheus.kubernetes.joinCommand%>

This completes the needed Script Templates which we will set on two new Node Types in the next step. Continue on to the next section.

Creating Node Types
```````````````````

With the Script Templates created we now need to make two new Node Types, one for the master node and one for the worker nodes. In this example case, we don't need to add a new Virtual Image because we can use one of the preinstalled system images for Ubuntu on VMware vCenter which will work fine. Node Types are created in |LibBluNod|. Once there, click :guilabel:`+ ADD`. Within the modal for the new Node Type, configure the following:

- **NAME:** Provide a name for the Node Type, can be anything to denote this is the master node
- **SHORT NAME:** A shortened version of the name without any spaces
- **VERSION:** The version number you wish to apply for this particular Node Type which is useful if you iterate on your Node Types at any point
- **TECHNOLOGY:** For this example case, VMware. Once set, additional options will appear
- **VM IMAGE:** A pre-installed Ubuntu system image will work
- **SCRIPTS:** Using the typeahead field, set the "k8sprep", "kubeadm-init" and "k8s-master-setup" Script Templates (you may have called them something different)

Finally, click :guilabel:`SAVE CHANGES`.

Repeat the process to create a second Node Type. The second time around, use the following configurations:

- **NAME:** Provide a name for the Node Type, can be anything to denote this is the worker node
- **SHORT NAME:** A shortened version of the name without any spaces
- **VERSION:** The version number you wish to apply for this particular Node Type which is useful if you iterate on your Node Types at any point
- **TECHNOLOGY:** For this example case, VMware. Once set, additional options will appear
- **VM IMAGE:** A pre-installed Ubuntu system image will work
- **SCRIPTS:** Using the typeahead field, set the "k8sprep" and "k8s-join" Script Templates (you may have called them something different)

Once done, click :guilabel:`SAVE CHANGES` to save the second Node Type. With the pieces in place, we are now ready to create the Cluster Layout object itself. Continue on to the next section.

Creating a Cluster Layout
`````````````````````````

At this point we can create the Cluster Layout object in |morpheus| and attach the Node Types we've just created (which themselves have our Script Templates applied). Cluster Layouts are created in |LibBluClu|. Click :guilabel:`+ ADD` and configure the following:

- **NAME:** Provide a name for the Cluster Layout, can be anything to denote this is a Kubernetes cluster
- **VERSION:** The version number you wish to apply to this Cluster Layout which is useful if you later iterate on this Cluster Layout
- **CLUSTER TYPE:** Kubernetes Cluster
- **TECHNOLOGY:** VMware
- **MINIMUM MEMORY:** 4096 MB
- **INPUTS:** Use the typeahead field to add configured Inputs to the Cluster Layout
- **MASTER NODES:** Use the typeahead field to find the Kubernetes master Node Type we just created
- **WORKER NODES:** Use the typeahead field to find the Kubernetes worker Node Type we just created. Set the "Count" value to three (3) since we wish to have three worker nodes in this cluster
- **CLUSTER PACKAGES:** Use the typeahead field to add configued Cluster Packages to the Cluster Layout. Cluster Packages are created in the `Templates section <https://docs.morpheusdata.com/en/latest/library/templates/templates.html>`_
- **SPEC TEMPLATES:** Use the typeahead field to add Spec Templates to the Cluster Layout

Click :guilabel:`SAVE CHANGES` to save the Cluster Layout.

Testing and Wrap-Up
```````````````````

At this point we are finished and we have a viable Kubernetes cluster that we can deploy with just one click. To add a new managed cluster to this |morpheus| environment, navigate to |InfClu|. To provision a cluster from the layout we just created, click :guilabel:`+ ADD CLUSTER` and select "Kubernetes Cluster" from the dropdown menu. Make the appropriate selections to target the new cluster to an existing VMware vCenter Cloud and complete the wizard. Once complete, the new cluster will be visible on your clusters list page and from there you can drill into the detail page to view relevant details about the cluster including monitoring metrics, current workloads, and more.
