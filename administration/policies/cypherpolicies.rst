Cypher Policies
---------------

|morpheus| allows administrators to set robust Cypher policies, which determine global, role, and/or specific user access to configured Cypher secret mount points. A number of considerations should be made when deploying Cypher Access policies, including how user role permissions will interact with the policy and how conflicts between overlapping policies are resolved.

Role Permissions
^^^^^^^^^^^^^^^^

User Role permissions (|AdmRol|) greatly affect Cypher access. Cypher access Role permissions are set from the Features tab of the selected Role under "Tools: Cypher". The Role permission should be set based on the highest level of access to any one individual Cypher entry needed for the specific Role. For example, if the Role needs no access to any Cypher entries, set the feature permission to "None" and hide the Cypher UI from the Role completely. Alternatively, if the Role needs to use and decrypt even one Cypher entry, set the feature permission to "Full Decrypt". The complete set of available permissions are below:

- **NONE:** Cypher UI hidden
- **READ:** Cypher UI present, entries can be listed
- **USER:** Cypher UI present, user sees and can use their own entries, user can create new entries
- **FULL:** Cypher UI present, user sees and can use all entries, user can create new entries, user cannot decrypt any entries
- **FULL DECRYPT:** Full access to Cypher features including the ability to decrypt secrets

Cypher Access Policies
^^^^^^^^^^^^^^^^^^^^^^

Like other Policy types, Cypher Access Policies are created in |AdmPol|. Click :guilabel:`+ ADD POLICY` to create new. Set the type to "Cypher Access" and the relevant configuration options will be displayed. In addition to the type, enter a name for the Policy in the top section.

.. image:: /images/administration/policies/polname.png
  :width: 50%

In the next section, enter the key path to which the Policy will apply. In addition to static entries that point to one specific Cypher entry, this field supports pattern matching with regex. For example, enter ".*" to refer to all Cypher entries or "secret/.*" to refer to all entries under the secret mount point.

In addition to the path, set the privileges users in the Policy scope should have on the indicated path.

- **LIST:** See the entries on the indicated path listed in the Cypher UI
- **READ:** Decrypt the entries on the indicated path
- **WRITE:** Add new entries on the indicated path
- **UPDATE:** Edit Cypher entries on the indicated path. This is future functionality, the ability to update Cypher entries does not currently exist in the product
- **DELETE:** Delete entries on the indicated path

.. image:: /images/administration/policies/polconfig.png
  :width: 50%

Finally, set the scope for the Policy. Cypher Access Policies support Global, Role, and User scope. For example, you may want to block off sets of Cypher entries for various departments within your organization. If you have existing Roles in |morpheus| for each department, you can set up Role-scoped Policies to ensure they can only list, use, and add Cypher entries which are relevant to their own department.

.. image:: /images/administration/policies/polfilter.png
  :width: 50%

.. IMPORTANT:: When Cypher Access Policies conflict, the Policy with the longest path string length (typically the most specific) takes precedence. For example, a Policy giving LIST and READ access to "secret/aws/.*" would be superseded by a Policy giving NO access to "secret/aws/my-secret-key". In such a case, the user would see everything at the "secret/aws/.*" path except the one indicated in the more specific Policy. When Policies targeting the same path differ only in their scope, the following scope precedence is applied: Role > User > Global. For example, if a Role-scoped Policy targeting ".*" grants LIST and READ while a User-scoped Policy targeting the same path grants LIST, the user would be granted the rights in the Role-scoped Policy.

Example Policy
^^^^^^^^^^^^^^

In my example organization, I have one department that needs access to AWS-related secrets and another department that needs access to Azure-related secrets. There are many other secrets stored in my appliance but I don't want either of these departments to access any of those.

.. image:: /images/administration/policies/cypherlist.png

For the first department, I've set up a Policy that allows them to list and read (including use and decryption rights) AWS secrets. A second Policy specifically excludes them from seeing one specific entry. The Policy with the more specific path will supersede the more generic Policy that includes a wildcard.

.. image:: /images/administration/policies/pollist.png

By impersonating the user, we see they indeed have access to just the two desired Cypher entries.

.. image:: /images/administration/policies/user1cypher.png

For the second department, I have set up a Policy that allows them to list and read (including use and decryption rights) Azure secrets.

.. image:: /images/administration/policies/cypherlist2.png

By impersonating the user once again, we see they indeed have access only to Azure entries.

.. image:: /images/administration/policies/user2cypher.png
