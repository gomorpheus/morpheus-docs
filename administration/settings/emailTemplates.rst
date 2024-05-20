Email Templates
^^^^^^^^^^^^^^^

|morpheus| sends out email to its users periodically to alert for various conditions such as an Instance provisioning success, warnings about upcoming Instance expiration, requests for password reset links, and more. |morpheus| includes system-default email templates for all of these emailed conditions but allows users to create their own email templates to override the default template.

On accessing the Email Templates tab, users will see a list of all email templates that currently exist. We can also see the owner which created the template as well as the associated Account (Tenant). System-default templates are shown as being owned by "System" and show no associated Account (Tenant). When a |mastertenant| user creates a template, the option is given to tie the template to an Account or to make a global template. The Accounts column will show "Global" for global templates. Templates will apply in order of specificity: Tenant-specific templates apply first, then custom global templates, and finally system templates if no others exist for that email type.

.. IMPORTANT:: Email templates apply in order of specificity. Tenant-specific templates apply over custom global templates which apply over system-default templates.

.. image:: /images/administration/settings/emailTemplateList.png

**Creating Templates**

Before creating the first template, it's important to realize email from custom templates will still come wrapped in the standard |morpheus| email headers and footers. It will also have included styling. This styling comes directly from your Tenant whitelabel configuration and will include |morpheus| standard styling or your custom whitelabel styling depending on appliance configuration. The template itself should only include email body content which will be inserted within the styling wrapper.

.. IMPORTANT:: It is possible to break the functionality of certain types of generated email by creating a custom template. For example, in a password reset email, you must ensure the password reset button is still included with the template. Other functionality-breaking scenarios may also be possible. Review the system-default template of any email type to copy syntax examples for such vital components.

Some template types will have variables accessible, such as the logged in user's name (to address the email) or an Instance name. To see the available variables, click on the info button for the system-default template of the type you wish to create. You'll see the variables mentioned in a comment at the bottom of the template such as in this example Confirm Password Update Template:

.. code-block:: html

  <p>{{{i18n "com.bertramlabs.plugins.accounts.password.email.greeting"}}}</p>
  <p>{{{i18n "com.bertramlabs.plugins.accounts.password.email.message"}}}</p>
  <a href={{{url}}}>{{{i18n "com.bertramlabs.plugins.accounts.password.email.linkLabel"}}}</a>
  <p>{{{i18n "com.bertramlabs.plugins.accounts.password.email.signature"}}} </p>
  <!-- available hbs variables are user.displayName and user.username -->

To begin creating a new template, from the Email Templates tab of the global settings page (|AdmSet|), click :guilabel:`+ CREATE`. The following configurations must be set:

- **TYPE:** Select the email type for the new template
- **TEMPLATE:** The HTML markdown for the new custom email template
- **TENANTS:** This option is only available in the |mastertenant|. Select a specific Tenant to tie the template to that Tenant or leave it empty to create a global template

The following is an example of a Forgot Password Template. Note that it calls in the variable for the associated user display name and username.

.. code-block:: html

  <p>Hello {{{user.displayName}}},</p>
  <p>You have requested to reset the password for the account with username: {{{user.username}}}.</p>
  <p>To reset the password, please click the button below. If you did not make this request, you can ignore this email but you should change your password.</p>
  <a href='{{{forgotPasswordUrl}}}' class="btn-primary">Magical Password Reset Button</a>
