Task Plugin
```````````
Add custom Tasks types to Morpheus

Setup
.....

Tasks (called Jobs in the UI) are useful components of your provisioning workflow. This plugin allows you to create custom Tasks

- Create a new class that implements ``com.morpheusdata.core.TaskProvider``
- Create a new class that extends ``com.morpheusdata.core.AbstractTaskService``.

This service defines methods for task execution in a variety of contexts, described below.

Options
.......

``OptionType`` is an easy way to create configuration for your new Task. Simply provide a list of ``com.morpheusdata.model.OptionType`` to the ``TaskProvider.getOptionTypes`` method.

.. code-block:: groovy

			@Override
			List<OptionType> getOptionTypes() {
				OptionType optionType = new OptionType(
						name: 'myTask',
						code: 'myTaskText',
						fieldName: 'myTask',
						optionSource: true,
						displayOrder: 0,
						fieldLabel: 'Text to Reverse',
						required: true,
						inputType: OptionType.InputType.TEXT
				)
				return [optionType]
			}

Task Contexts
.............

A task can be run in one of three contexts:

- None/Local (``executeLocalTask``)
- Remote (``executeRemoteTask``)
- Instance (``executeContainerTask``, ``executeContainerTask``)

Task Logo
.........

A custom logo can be used in the Morpheus UI by placing an image at ``src/assets/images/{task-code}.png``.
Recommended file size is 180 x 60 px.
