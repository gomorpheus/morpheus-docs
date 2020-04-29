Option Types
------------

Option Types are custom input fields that can be added to Instance Types and Layouts, then presented in Instance, App, and Cloning wizards. The resulting value is available in the Instance config map as <%=customOptions.fieldName%>. The fieldName and value can also be exported as Tags.

.. image:: /images/provisioning/library/new_option_type.png
   :align: center
   :width: 80%

Create Option Type
^^^^^^^^^^^^^^^^^^

.. note:: All possible fields listed. Displayed fields depend on ``TYPE`` selection

NAME
 Name of the Option Type
DESCRIPTION
 Description for reference in Option Type list view
FIELD NAME
 This is the input fieldName property that the value gets assigned to
EXPORT AS TAG
 Creates Tags for fieldName/value (key/value) on Instances
TYPE
  - **Text:** Text Input Field

  - **Select List:** Populated by Option Lists, presents a manual or REST-populated dropdown list

  - **Checkbox:** Checkbox for ``on`` or ``off`` values

  - **Number:** Input field allowing only numbers

  - **Typeahead:** Populated by Option Lists: Rather than presenting a potentially-large dropdown menu, the user can begin typing a selection into a text field and choose the desired option. Multiple selections can be allowed with this type by marking the 'ALLOW MULTIPLE SELECTIONS' box

  - **Hidden:** No field will be displayed, but the field name and default value will be added to the Instance config map for reference

  - **Password:** An input field with suitable encryption for accepting passwords
LABEL
 This is the input label that typically shows to the left of a custom option
PLACEHOLDER
 Background text that populates inside a field for adding example values, does not set a value
DEFAULT VALUE
 Pre-populates field with a default value
REQUIRED
 Prevents User from proceeding without setting value
DEFAULT CHECKED
 For ``Checkbox`` types, when marked the Checkbox will be checked by default
OPTION LIST
 For ``Select List`` types, select a pre-existing Option List to set dropdown values

 .. NOTE:: ``Select List`` and ``Typeahead`` Option Types require creation and association of an Option List
