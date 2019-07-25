Option Types
------------

Option Types are custom input fields that can be added to Instance Types and Layouts and used in Instance, App and Cloning wizards. The resulting value is available in the Instance config map as <%=customOptions.fieldName%>, and the filedName and value can also be exported as metadata.

.. image:: /images/provisioning/library/addOptionType.png

Create Option Type
^^^^^^^^^^^^^^^^^^

.. note:: All Fields listed. Applicable fields depend on ``TYPE`` selection
NAME
 Name of the Option Type
DESCRIPTION
 Description for reference in Option Type list view
FIELD NAME
 This is the input fieldName property that the value gets assigned to.
EXPORT AS METADATA
 Creates Metadata tags for Field Name and Value on Instances
TYPE
 Text
  Text Input Field
 Select
  Used with Option Lists, presents a manual or rest populated dropdown list
 Checkbox
  Checkbox with true or false values
 Number
  Input field allowing only numbers
 Hidden
  No filed will be displays, but the field name and default value will be added to Instance config map for reference.
LABEL
 This is the input label that shows typically to the left of a custom option.
PLACEHOLDER
 Background text that populates inside a field for adding example values. Does not set a value.
DEFAULT VALUE
 Populates field with default value, can be
REQUIRED
 Prevents user from proceeding without setting value
DEFAULT CHECKED
 For ``Checkbox`` types, when enabled Checkbox will be checked by default
OPTION LIST
 For ``Select`` types, select associated Option List

 .. NOTE:: ``Select`` Option Types require creation and association of an Option List
