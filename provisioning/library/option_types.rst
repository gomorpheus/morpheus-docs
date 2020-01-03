Option Types
------------

Option Types are custom input fields that can be added to Instance Types and Layouts and used in Instance, App and Cloning wizards. The resulting value is available in the Instance config map as <%=customOptions.fieldName%>, and the filedName and value can also be exported as metadata.

.. image:: /images/provisioning/library/newOptionType.png
   :align: center

Create Option Type
^^^^^^^^^^^^^^^^^^

.. note:: All Fields listed. Applicable fields depend on ``TYPE`` selection

NAME
 Name of the Option Type
DESCRIPTION
 Description for reference in the Option Type list view
FIELD NAME
 This is the input fieldName property that the value gets assigned to.
EXPORT AS METADATA
 Creates Metadata tags for Field Name and Value on Instances
TYPE
 Text
  Text Input Field
 Select List
  Used with Option Lists, presents a manual or rest populated dropdown list
 Checkbox
  Checkbox with true or false values
 Number
  Input field allowing only numbers
 Typeahead
  Used with Option Lists: Rather than presenting a potentially-large dropdown menu, the user can begin typing a selection into a text field and choose the desired option. Multiple selections can be allowed with this type by marking the 'ALLOW MULTIPLE SELECTIONS' box
 Hidden
  No filed will be displays, but the field name and default value will be added to Instance config map for reference.
 Password
  A specific Option Type for accepting password values
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
 For ``Select`` types, select associated Option List. The needed Option List must already exist must already exist if you plan to create an Option Type relying on selct lists.
DEPENDENT FIELD
 An associated fieldName that will trigger reloading the Option List based on the chosen selection. This option is available in Morpheus version 4.1.0 and greater.

.. NOTE:: To see an example of an Option Type with a dependent list and how they can be added as a selection when provisioning a custom instance type, see our `Knowledge Base <https://support.morpheusdata.com/s/article/How-to-create-option-lists>`_ article on the subject.


