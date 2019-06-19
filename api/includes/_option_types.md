# Option Types

Morpheus has several objects that have dynamic models depending on the type of the object. This includes options when provisioning different instances or even options when defining tasks or creating docker hosts!. This section aims to describe what is contained in the option-types association as well as how to query morpheus for available options in certain option-type scenarios.

## Example of an Option Type Record

```json
{
	"optionTypes": [
                {
                    "name": "subnet",
                    "description": null,
                    "fieldName": "subnetId",
                    "fieldLabel": "Subnet",
                    "fieldContext": "config",
                    "fieldAddOn": null,
                    "placeHolder": null,
                    "helpBlock": "",
                    "defaultValue": null,
                    "optionSource": "amazonSubnet",
                    "type": "select",
                    "advanced": false,
                    "required": true,
                    "editable": false,
                    "config": [],
                    "displayOrder": 100
                },
                {
                    "name": "security group",
                    "description": null,
                    "fieldName": "securityId",
                    "fieldLabel": "Security Group",
                    "fieldContext": "config",
                    "fieldAddOn": null,
                    "placeHolder": null,
                    "helpBlock": "",
                    "defaultValue": null,
                    "optionSource": "amazonSecurityGroup",
                    "type": "select",
                    "advanced": false,
                    "required": true,
                    "editable": false,
                    "config": [],
                    "displayOrder": 101
                },
                {
                    "name": "public key",
                    "description": null,
                    "fieldName": "publicKeyId",
                    "fieldLabel": "Public Key",
                    "fieldContext": "config",
                    "fieldAddOn": null,
                    "placeHolder": null,
                    "helpBlock": "",
                    "defaultValue": null,
                    "optionSource": "keyPairs",
                    "type": "select",
                    "advanced": false,
                    "required": false,
                    "editable": false,
                    "config": [],
                    "displayOrder": 9
                }
            ]
}
```


Option types can easily represent some common input types, including text, number, radio, checkbox, and dropdown/multiple choice.


### JSON Parameters

Parameter   | Description
---------   | -----------
name        | The name of the option type for handy reference
description | Short description of hte option type (the CLI actually shows this when pressing `?` for help)
fieldName   | The property key for when posting this option type to a JSON POST request
fieldLabel  | User friendly label for prompting a user for input
fieldContext | Some properties need nested i.e. in a `config: {}` block. This is a `.` seperated context of where the property should be constructed
placeHolder | Any placeholder text when nothing is yet entered
helpBlock  | Short help text describing the option
defaultValue | The default value if no user entry is specified. This value should be passed to the desired JSON Map if nothing else is entered
optionSource | Option source references an API endpoint for receiving a JSON list of available options for this field.
type         | The type of input. I.e. text, select, radio,checkbox, etc.
required     | Is this field entry required for the request
editable     | Used primarily on tasks and workflows. Basically wether or not the field can be overridden optionally when the object is run
displayOrder | The order with which the fields should be prompted. This is rather important when using optionSource in some scenarios for determining available values.
config:      | Any special configuration options pertaining to specific input types, like a radio button.

## Get Option Source Data

```shell
curl "https://api.gomorpheus.com/api/options/keyPairs"
  -H "Authorization: BEARER access_token"
```

> The above command returns JSON structured like this

```json
[
	["name": "Davids Key Pair", "value": 1]
]
```


### HTTP Request

`GET https://api.gomorpheus.com/api/options/:optionSource`

Returns a list of name/value pairs for option-type models. Some option-types depend on input data for proper representation. This typically includes zoneId or siteId for the item being provisioned as request parameters or sometimes previous option type parameters.