Image Builder
=============

The Morpheus Image Builder service creates vmdk, qcow2, vhd and raw Images from scratch. The Image Builder creates a blank VM in VMware, attaches an os iso, executes a boot script on the VM at startup via VNC which calls a preseed script which runs the unattended os installation and configuration. Morpheus then executes an ova export of the completed vmdk to target Storage provider, and converts the image to all other specified formats. The new Virtual Image records are automatically added to Morpheus and the Images are then available for use.

Requirements
------------

- DHCP must be enabled on the network specified for the VM in Morpheus, and network settings configured for DHCP in Morpheus
   The blank VM must get network configuration via DHCP upon boot. Static IP assignment is not possible.
- Hypervisor Console must be enabled on the Target Cloud
   Morpheus utilizes VNC to pass the boot script to the VM.
- VM must be able to reach and resolve the Morpheus appliance url over 443
   The boot script calls to the Morpheus appliance to get the preseed script.
- Valid Linux iso set for the Virtual Image. Windows is not supported.
   The iso can exist in the target cloud or uploaded to Morpheus

   .. note:: ``cloud-init enabled`` must be disabled on the iso Virtual Image settings.

- Access to target ESXi host(s) over 443 and ESXi hostname dns resolution
   - Same requirement as Hypervisor Console and Image upload/download to/from vCenter.
- Valid Boot Script
- Valid Pre-seed script
- Valid Storage Provider configure for ova export of generated image.

Sample Scripts
--------------

Sample Boot Script
^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

   <wait5><tab> text ks=<%=preseedUrl%><enter>

.. note:: ``<%=preseedUrl%>`` is a Morpheus variable that will populate with the Morpheus appliance url.

Sample Preseed Script
^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

    # CentOS 7.x kickstart file - ks.cfg
    #
    # For more information on kickstart syntax and commands, refer to the
    # CentOS Installation Guide:
    # https://access.redhat.com/documentation/en-US/Red_Hat_Enterprise_Linux/7/html/Installation_Guide/sect-kickstart-syntax.html
    #
    # For testing, you can fire up a local http server temporarily.
    # cd to the directory where this ks.cfg file resides and run the following:
    #    $ python -m SimpleHTTPServer
    # You don't have to restart the server every time you make changes.  Python
    # will reload the file from disk every time.  As long as you save your changes
    # they will be reflected in the next HTTP download.  Then to test with
    # a PXE boot server, enter the following on the PXE boot prompt:
    #    > linux text ks=http://<your_ip>:8000/ks.cfg

    # Required settings
    lang en_US.UTF-8
    keyboard us
    rootpw password
    authconfig --enableshadow --enablemd5
    timezone UTC

    # Optional settings
    install
    cdrom
    user --name=cloud-user --plaintext --password password
    unsupported_hardware
    network --bootproto=dhcp
    firewall --disabled
    selinux --permissive
    bootloader --location=mbr --append="biosdevname=0 net.ifnames=0"
    text
    skipx
    zerombr
    clearpart --all --initlabel
    autopart --type=plain
    firstboot --disabled
    reboot

    %packages --nobase --ignoremissing --excludedocs
    openssh-clients
    # Prerequisites for installing VMware Tools or VirtualBox guest additions.
    # Put in kickstart to ensure first version installed is from install disk,
    # not latest from a mirror.
    kernel-headers
    kernel-devel
    gcc
    make
    perl
    curl
    wget
    bzip2
    dkms
    patch
    net-tools
    git
    # Core selinux dependencies installed on 7.x, no need to specify
    # Other stuff
    sudo
    nfs-utils
    open-vm-tools
    -fprintd-pam
    -intltool
    -biosdevname

    # unnecessary firmware
    -aic94xx-firmware
    -atmel-firmware
    -b43-openfwwf
    -bfa-firmware
    -ipw*-firmware
    -irqbalance
    -ivtv-firmware
    -iwl*-firmware
    -libertas-usb8388-firmware
    -ql*-firmware
    -rt61pci-firmware
    -rt73usb-firmware
    -xorg-x11-drv-ati-firmware
    -zd1211-firmware
    %end

    %post
    # configure vagrant user in sudoers
    echo "%cloud-user ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers.d/cloud-user
    chmod 0440 /etc/sudoers.d/cloud-user
    cp /etc/sudoers /etc/sudoers.orig
    sed -i "s/^\(.*requiretty\)$/#\1/" /etc/sudoers
    # keep proxy settings through sudo
    echo 'Defaults env_keep += "HTTP_PROXY HTTPS_PROXY FTP_PROXY RSYNC_PROXY NO_PROXY"' >> /etc/sudoers
    %end
