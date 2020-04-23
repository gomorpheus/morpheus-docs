Option Types
------------

Option Types are custom input fields that can be added to Instance Types and Layouts, then presented in Instance, App, and Cloning wizards. The resulting value is available in the Instance config map as <%=customOptions.fieldName%>. The fieldName and value can also be exported as Tags.

.. image:: /images/provisioning/library/newOptionType.png
   :align: center

Create Option Type
^^^^^^^^^^^^^^^^^^

.. note:: All possible fields listed. Displayed fields depend on ``TYPE`` selection

NAME
 Name of the Option Type
DESCRIPTION
 Description for reference in Option Type list view
FIELD NAME
 This is the input fieldName property that the value gets assigned to.
EXPORT AS TAG
 Creates Tags for Field Name and value on Instances
TYPE
 Text
  Text Input Field
 Select List
  Used with Option Lists, presents a manual or REST-populated dropdown list
 Checkbox
  Checkbox for ``on`` or ```off`` values
 Number
  Input field allowing only numbers
 Typeahead
  Used with Option Lists: Rather than presenting a potentially-large dropdown menu, the user can begin typing a selection into a text field and choose the desired option. Multiple selections can be allowed with this type by marking the 'ALLOW MULTIPLE SELECTIONS' box
 Hidden
  No filed will be displays, but the field name and default value will be added to Instance config map for reference
 Password
  An input field with suitable encryption for accepting passwords
LABEL
 This is the input label that shows typically to the left of a custom option.
PLACEHOLDER
 Background text that populates inside a field for adding example values, does not set a value
DEFAULT VALUE
 Populates field with default value
REQUIRED
 Prevents user from proceeding without setting value
DEFAULT CHECKED
 For ``Checkbox`` types, when enabled Checkbox will be checked by default
OPTION LIST
 For ``Select List`` types, select associated Option List

 .. NOTE:: ``Select List`` Option Types require creation and association of an Option List
