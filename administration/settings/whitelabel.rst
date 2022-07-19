Whitelabel Settings
^^^^^^^^^^^^^^^^^^^

Overview
````````

|morpheus| Tenants can be WhiteLabeled with custom Logos, Colors, Copy, and custom CSS. Sub-Tenants can be individually white-labeled, or the Master Tenant Whitelabel can apply to all Sub-Tenants.

Enable Whitelabel
	Turns on the configured Whitelabel settings. Disabling will return the Appliance to the default colors and logos, but the configured options will remain saved and will apply if Whitelabel is re-enabled.
Appliance Name
	Replaces |morpheus| in page titles.
Header Logo
	Top left header logo. Uploaded image is resized to 38 pixels high with a proportional width at that height.
Disable Support Menu
	Enable this flag to hide the support dropdown menu in the header.
Support Menu Links
	Customize support links. Label Code can be used for translations and is optional. Be sure to specify fully qualified url if linking to external sites.
Security Banner
	The Security Banner section in ``/admin/settings#!whitelabel`` displays content on the login screen for Security and Consent messaging and warnings.
		- Applicable at Global and Tenant levels
		- Security Banner input field accepts plain text and markdown
		- Content is displayed below login section in scoped ``/login/auth`` pages.
Footer Logo
	Footer Logo in bottom left. Uploaded image is resized to 27 pixels high with a proportional width at that height.
Login Logo
	Logo shown on Login screen. Uploaded image is resized to 192 pixels wide with an unbound height proportional to that locked width.
Favicon
	Must be a .ico file type.
Reset
	When selected and Whitelabel settings are saved, associated logo is returned to blank default value.

Colors
``````

Update Colors by entering HEX value or selecting the Color Selector pop-up next to each filed and selecting a color.

* Header Background
* Header Foreground
* Nav Background
* Nav Foreground
* Nav Hover
* Primary Button Bg
* Primary Button Fg
* Primary Button Hover Bg
* Primary Button Hover Fg
* Footer Background
* Footer Foreground
* Login Background

Override CSS
````````````

Override CSS settings by entering CSS in `Override CSS` field.

Example: (this will add one continues background image to the Header)

.. code-block:: bash

	header #topHeader {
		background-image: url(http://image_url.png);
		}
	header {
		background-image: url(http://image_url.png);
		}

Copy
````

Add custom Copyright String, Terms of Use, Privacy Policy contained in the Footer text and links in the App and on the login page and emails.

Available Copy fields

* Copyright String
* Terms and Privacy String
* Terms of Use
* Privacy Policy

		.. NOTE:: Terms of Use and Privacy Policy Footer links will load internal pages at ``https://applaince_url/privacy-policy`` and ``https://applaince_url/terms-of-use`` displaying the entered info as plain text. The Terms and Privacy String will update the legal text displayed on the |morpheus| login page. This field takes any custom HTML markup allowing you to link to the internal legal pages or to your own outside legal pages if you prefer.

​UI Loading Page
````````````````

When the |morpheus| UI is restarted or loading, a default "Morpheus is Loading" page is displayed. This page can be changed by adding the following to ``/etc/morpheus/morpheus.rb`` and adjusting the values.

.. NOTE:: ``morpheus-ctl reconfigure`` must be ran for any chnages to ``/etc/morpheus/morpheus.rb`` to take effect.

.. code-block:: bash

		nginx['web_root_internal'] = "/opt/morpheus/embedded/nginx/html"
		nginx['loading_pages']['max_loops'] = 6 * 10 # 10 secs per loop x 6 times to get 60 seconds * 10 to get to 10 minutes
		nginx['loading_pages']['timeout_page'] = '/timeout.html'
		nginx['loading_pages']['iteration_time'] = 10_000
		nginx['loading_pages']['loading_page_title'] = 'Morpheus Loading'
		nginx['loading_pages']['loading_page_h1'] = 'Morpheus is Loading...'
		nginx['loading_pages']['loading_page_h2'] = 'please wait'
		nginx['loading_pages']['timout_page_title'] = 'Morpheus timeout, please try again...'
		nginx['loading_pages']['timout_page_h1'] = 'Timeout waiting for Morpheus to load, click below to try again.'
		nginx['loading_pages']['failure_page_title'] = 'Morpheus Server Error'
		nginx['loading_pages']['failure_page_h1'] = 'Morpheus Server Error'
		nginx['loading_pages']['failure_page_h2'] = 'Please contact your system administrator for assistance.'
