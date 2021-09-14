Option Types
------------

Option Types are custom input fields that can be added to Instance Types and Layouts, then presented in Instance, App, and Cloning wizards. The resulting value is available in the Instance config map as <%=customOptions.fieldName%>. The fieldName and value can also be exported as Tags.

.. image:: /images/provisioning/library/new_option_type.png
   :align: center
   :scale: 40%

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
DEPENDENT FIELD
 The Field Name value for a field that will reload this Option List to present a different set of selections. Take a look at the section below on Cascading Option Types as well as the `associated article <https://support.morpheusdata.com/s/article/How-to-create-option-lists?language=en_US>`_ in our KnowledgeBase for documented examples of this feature
VISIBILITY FIELD
 A Field Name and selection value that will trigger this field to become visible. Currently, this only works when the Option Type is associated with a Service Catalog Item and viewed from the Service Catalog Persona perspective. See the section below on the Visibility Field for instructions on configuring this value
DISPLAY VALUE ON DETAILS
 When selected, the Option Type label and value (label: value) will be visible in a list of custom options on the Instance detail page
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
HELP BLOCK
 Helpful text that will appear under your Option Type field to inform users about their selection
REQUIRED
 Prevents User from proceeding without setting value
DEFAULT CHECKED
 For ``Checkbox`` types, when marked the Checkbox will be checked by default
OPTION LIST
 For ``Select List`` types, select a pre-existing Option List to set dropdown values

 .. NOTE:: ``Select List`` and ``Typeahead`` Option Types require creation and association of an Option List

Cascading Option Types
^^^^^^^^^^^^^^^^^^^^^^

One powerful facet of |morpheus| Option Types is the ability to present users with different lists of input options based on their selections in other Option Types within the same wizard or modal. One common example, which is fully illustrated in this section, might be to have a user select:

- The Group they wish to provision into...
- Then select the target Cloud from a list limited to Clouds which are in the selected Group...
- Then select the target network from a list limited to networks which are in the selected Cloud *and* Group

To set this up, we'll first configure our Option Types (custom option fields that can be applied to Instance Types and other |morpheus| constructs) and Option Lists (dynamic lists of possible choices which can be associated with Option Types and presented in a dropdown or typeahead format). Once the custom options are configured, we'll associate them with a new service catalog item and take a look at how the user would ineract with them.

Group Custom Option
```````````````````

To begin, we'll create a new `Option List <https://docs.morpheusdata.com/en/latest/provisioning/library/library.html#option-lists>`_. In this case, we'll select type of "Morpheus Api" which will populate the list based on a call to the internal |morpheus| API. Option Lists can also be populated by calls to external REST APIs or even from static lists that you enter manually. When dynamically populating Option Lists, whether via |morpheus| API or an external API, translation and/or request scripts may be needed to prepare the request or translate the results. More on that as we build out the example.

I've called my Option List "Groups" and selected "Groups" from the OPTION LIST menu. This simply indicates that Groups are the construct we want to call into our list from |morpheus| API. In this case, we want to present a list of all Groups to the user by their name and pass the Group database ID in the background. Since it's common to create Option Lists from |morpheus| API where the construct name is displayed to the user and the ID is passed, we actually don't need to input any translation scripts in this case. However, I'll include a translation script here which does the same thing simply to provide more clarity to the example. |morpheus| `Option List documentation <https://docs.morpheusdata.com/en/latest/provisioning/library/library.html#morpheus-api-option-list-fields>`_ includes additional details on available translation script inputs and which are available without translation as a convenience feature.

.. code-block:: bash

  for (var x = 0; x < data.length; x++) {
    results.push({name: data[x].name, value:data[x].id});
  }

After saving the Option List, create the Option Type that presents the list we just created. I gave my Option Type the name of "Selected Group", field name of "selectedGroup", and label of "Group". For type, choose "Select List" and a new field will appear at the bottom of the modal where we can select the Option List we just created.

Cloud Custom Option
```````````````````



Network Custom Option
`````````````````````

Setting Custom Options at Provision Time
````````````````````````````````````````


Visibility Field
^^^^^^^^^^^^^^^^

The Visibility field for Option Types allows users to set conditions under which the Option Type being created or edited is displayed. A very simple visibility configuration would look like the following: ``config.customOptions.color:(red)`` where "color" represents the ``fieldName`` for any other Option Type which will determine the visibility of the current one and "red" represents any JavaScript regular expression that matches to the values that meet your desired conditions.

Expanding on the simplified example above, we could trigger visibility based on any one of multiple selections from the same Option Type by using a different regular expression, such as ``config.customOptions.color:(red|blue|yellow)``. Additionally, we aren't restricted to the conditions of just one Option Type to determine visibility as the following would also be valid: ``config.customOptions.color:(red|blue|yellow),config.customOptions.shape:(square)``. In the previous example, the Option Type "Color" would have to be set to red, blue, or yellow `OR` the Option Type "Shape" would have to be set to square in order to trigger visibility of the Option Type currently being configured. Prepend the previous example with ``matchAll::`` in order to require both conditions to be met rather than one or the other (ex. ``matchAll::config.customOptions.color:(red|blue|yellow),config.customOptions.shape:(square)``).

Putting it all together, you'll first configure visibility for your selected Option Types as described above. You can see in the screenshot below I've set the Option Type being edited to have a visibility dependent on another Option Type which you can see in the background.

.. image:: /images/provisioning/optionTypes/1optionType.png

Next, ensure the relevant Option Types are associated with the Service Catalog Item (Tools > Self Service).

.. image:: /images/provisioning/optionTypes/2configCatalogItem.png
  :width: 50%

Finally, when Service Catalog Persona users interact with my Catalog Item, they will be able to toggle additional Option Types to be visible based on their selections.

.. image:: /images/provisioning/optionTypes/3toggleOption.gif
