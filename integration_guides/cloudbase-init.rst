Windows Image with Cloudbase-Init
=================================

|Morphues| supports provisioning Windows images with Cloudbase-init to set user data, network setting and other data at boot time. The following is an example of how to prepare a Windows image with cloudbase-init and optionally sysprep it.

Setup
-----

#. On your Windows VM download and install Cloudbase-init from https://cloudbase.it/cloudbase-init/
#. Use the default settings, and **do not** run sysprep at the end of the install.
#. Under C:\Program Files\Cloudbase Solutions\Cloudbase-Init\conf, edit the ``cloudbase-init.conf`` file, referring to the sample configuration below. If the image will be sysprepped, edit ``cloudbase-init-unattend.conf`` and ``unattend.xml`` as well.

   .. NOTE:: Sample configurations only, user configurations may vary.

    cloudbase-init.conf
    ^^^^^^^^^^^^^^^^^^^
    .. code-block:: xml

        [DEFAULT]
        # username=Admin
        # groups=Administrators
        # inject_user_password=true
        inject_user_password=false
        first_logon_behaviour=no
        config_drive_raw_hhd=true
        config_drive_cdrom=true
        config_drive_vfat=true
        bsdtar_path=C:\Program Files\Cloudbase Solutions\Cloudbase-Init\bin\bsdtar.exe
        mtools_path=C:\Program Files\Cloudbase Solutions\Cloudbase-Init\bin\
        verbose=true
        debug=true
        logdir=C:\Program Files\Cloudbase Solutions\Cloudbase-Init\log\
        logfile=cloudbase-init.log
        default_log_levels=comtypes=INFO,suds=INFO,iso8601=WARN,requests=WARN
        logging_serial_port_settings=
        mtu_use_dhcp_config=true
        ntp_uce_dhcp_config=true
        local_script_path=C:\Program Files\Cloudbase Solutions\Cloudbase-Init\LocalScripts\

        # servers - tried in order until success
        metadata_services=cloudbaseinit.metadata.services.configdrive.ConfigDriveService,
        	cloudbaseinit.metadata.services.httpservice.HttpService,
        	cloudbaseinit.metadata.services.ec2service.EC2Service,
        	cloudbaseinit.metadata.services.maasservice.MaaSHttpService

        # What plugins to execute.
        plugins=cloudbaseinit.plugins.common.mtu.MTUPlugin,
        	cloudbaseinit.plugins.windows.extendvolumes.ExtendVolumesPlugin,
          cloudbaseinit.plugins.common.userdata.UserDataPlugin,
          cloudbaseinit.plugins.common.networkconfig.NetworkConfigPlugin

        # disabled plugins
        # cloudbaseinit.plugins.common.sethostname.SetHostNamePlugin
        # cloudbaseinit.plugins.windows.createuser.CreateUserPlugin
        # cloudbaseinit.plugins.windows.setuserpassword.SetUserPasswordPlugin
        # cloudbaseinit.plugins.common.networkconfig.NetworkConfigPlugin
        # cloudbaseinit.plugins.common.sshpublickeys.SetUserSSHPublicKeysPlugin
        # cloudbaseinit.plugins.windows.winrmlistener.ConfigWinRMListenerPlugin
        # cloudbaseinit.plugins.windows.licensing.WindowsLicensingPlugin
        # cloudbaseinit.plugins.windows.ntpclient.NTPClientPlugin
        # cloudbaseinit.plugins.common.userdata.UserDataPlugin

        # Miscellaneous.
        allow_reboot=false    # allow the service to reboot the system
        # stop_service_on_exit=false


    cloudbase-init-unattend.conf
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    .. code-block:: xml

        [DEFAULT]
        username=Admin
        groups=Administrators
        inject_user_password=true
        config_drive_raw_hhd=true
        config_drive_cdrom=true
        config_drive_vfat=true
        bsdtar_path=C:\Program Files\Cloudbase Solutions\Cloudbase-Init\bin\bsdtar.exe
        mtools_path=C:\Program Files\Cloudbase Solutions\Cloudbase-Init\bin\
        verbose=true
        debug=true
        logdir=C:\Program Files\Cloudbase Solutions\Cloudbase-Init\log\
        logfile=cloudbase-init-unattend.log
        default_log_levels=comtypes=INFO,suds=INFO,iso8601=WARN,requests=WARN
        logging_serial_port_settings=
        mtu_use_dhcp_config=true
        ntp_use_dhcp_config=true
        local_scripts_path=C:\Program Files\Cloudbase Solutions\Cloudbase-Init\LocalScripts\
        metadata_services=cloudbaseinit.metadata.services.configdrive.ConfigDriveService,cloudbaseinit.metadata.services.httpservice.HttpService,cloudbaseinit.metadata.services.ec2service.EC2Service,cloudbaseinit.metadata.services.maasservice.MaaSHttpService
        plugins=cloudbaseinit.plugins.common.mtu.MTUPlugin,cloudbaseinit.plugins.common.sethostname.SetHostNamePlugin,cloudbaseinit.plugins.windows.extendvolumes.ExtendVolumesPlugin
        allow_reboot=false
        stop_service_on_exit=false
        check_latest_version=false

    unattend.xml
    ^^^^^^^^^^^^

    .. code-block:: xml

        <?xml version="1.0" encoding="utf-8"?>
        <unattend xmlns="urn:schemas-microsoft-com:unattend">
          <settings pass="generalize">
            <component name="Microsoft-Windows-Security-SPP" processorArchitecture="amd64" publicKeyToken="31bf3856ad364e35" language="neutral" versionScope="nonSxS" xmlns:wcm="http://schemas.microsoft.com/WMIConfig/2002/State" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
              <SkipRearm>1</SkipRearm>
            </component>
            <component name="Microsoft-Windows-PnpSysprep" processorArchitecture="amd64" publicKeyToken="31bf3856ad364e35" language="neutral" versionScope="nonSxS" xmlns:wcm="http://schemas.microsoft.com/WMIConfig/2002/State" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
              <PersistAllDeviceInstalls>false</PersistAllDeviceInstalls>
              <DoNotCleanUpNonPresentDevices>false</DoNotCleanUpNonPresentDevices>
            </component>
          </settings>
          <settings pass="oobeSystem">
            <component name="Microsoft-Windows-International-Core" processorArchitecture="amd64" publicKeyToken="31bf3856ad364e35" language="neutral" versionScope="nonSxS" xmlns:wcm="http://schemas.microsoft.com/WMIConfig/2002/State" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
              <InputLocale>en-US</InputLocale>
              <SystemLocale>en-US</SystemLocale>
              <UILanguage>en-US</UILanguage>
              <UserLocale>en-US</UserLocale>
            </component>
            <component name="Microsoft-Windows-Shell-Setup" processorArchitecture="amd64" publicKeyToken="31bf3856ad364e35" language="neutral" versionScope="nonSxS" xmlns:wcm="http://schemas.microsoft.com/WMIConfig/2002/State" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
              <OOBE>
                <HideEULAPage>true</HideEULAPage>
                <ProtectYourPC>1</ProtectYourPC>
                <NetworkLocation>Home</NetworkLocation>
                <HideWirelessSetupInOOBE>true</HideWirelessSetupInOOBE>
              </OOBE>
              <TimeZone>UTC</TimeZone>
              <UserAccounts>
                <AdministratorPassword>
                  <Value>administratorPassword</Value>
                  <PlainText>true</PlainText>
                </AdministratorPassword>
                <LocalAccounts>
                  <LocalAccount wcm:action="add">
                    <Password>
                      <Value>password</Value>
                      <PlainText>true</PlainText>
                    </Password>
                    <Group>administrators</Group>
                    <DisplayName>morpheus</DisplayName>
                    <Name>morpheus</Name>
                    <Description>Morpheus User</Description>
                  </LocalAccount>
                </LocalAccounts>
              </UserAccounts>
            </component>
          </settings>
          <settings pass="specialize"></settings>
        </unattend>

#. Save and changes to cloudbase-init.conf, cloudbase-init-unattend.conf, and unattend.xml files.

   .. NOTE:: The Administrator password is being set in the unattend.xml file to be set upon boot after sysprep. This is not required if sysprep is not being used, and may not be preferred. Other mechanisms such as requiring the Administrator password to be reset or randomly generated can be used. |morpheus| can also securely via the user_data file at provision time.


#. To run a sysprep using the cloudbase-init configuraiton, run the following in a command prompt:

   .. code-block:: powershell

    cd C:\Program Files\Cloudbase Solutions\Cloudbase-Init\conf

    C:\Windows\System32\sysprep\sysprep.exe /generalize /oobe /unattend:Unattend.xml

#. Sysprep will run and Windows will be powered down. The VM can now be converted to an Image/Template and synced or uploaded to Morpheus and used for Provisioning.

.. IMPORTANT:: Upon upload or sync of the Virtual Image, ensure ``cloudbase enable`` is checked in the Virtual Image config, and the existing or unattend.xml credentials when using sysprep are populated.
