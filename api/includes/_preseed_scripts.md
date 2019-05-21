# Preseed Scripts

Preseed Scripts are used in the Image Builder service. See [Image Builds](#image-builds)

## Get All Preseed Scripts

```shell
curl "https://api.gomorpheus.com/api/preseed-scripts"
  -H "Authorization: BEARER access_token"
```

> The above command returns JSON structured like this:

```json
{
  "preseedScripts": [
    {
      "id": 1,
      "account": {
        "id": 1,
        "name": "root"
      },
      "fileName": "debian 8",
      "description": null,
      "content": "...",
      "createdBy": {
        "username": "admin"
      }
    }
  ],
  "meta": {
    "offset": 0,
    "max": 25,
    "size": 1,
    "total": 1
  }
}
```

This endpoint retrieves all preseed scripts associated with the account.

### HTTP Request

`GET https://api.gomorpheus.com/api/preseed-scripts`

### Query Parameters

Parameter | Default | Description
--------- | ------- | -----------
name |  | If specified will return an exact match on fileName
phrase |  | If specified will return a partial match on fileName

## Get a Specific Preseed Script


```shell
curl "https://api.gomorpheus.com/api/preseed-scripts/1" \
  -H "Authorization: BEARER access_token"
```

> The above command returns JSON structured like this:

```json
{
  "preseedScript": {
    "id": 1,
    "account": {
      "id": 1,
      "name": "root"
    },
    "fileName": "debian 8",
    "description": null,
    "content": "...",
    "createdBy": {
      "username": "admin"
    }
  }
}
```

This endpoint retrieves a specific preseed script.


### HTTP Request

`GET https://api.gomorpheus.com/api/preseed-scripts/:id`

### URL Parameters

Parameter | Description
--------- | -----------
ID | The ID of the preseed script to retrieve


## Create a Preseed Script

```shell
curl -XPOST "https://api.gomorpheus.com/api/preseed-scripts" \
  -H "Authorization: BEARER access_token" \
  -H "Content-Type: application/json" \
  -d '{
  "preseedScript": {
    "fileName": "ubuntu build",
    "content": "choose-mirror-bin mirror/http/proxy string\nd-i apt-setup/use_mirror boolean true\nd-i base-installer/kernel/override-image string linux-server\nd-i debian-installer/add-kernel-opts string net.ifnames=0 biosdevname=0\nd-i clock-setup/utc boolean true\nd-i clock-setup/utc-auto boolean true\nd-i finish-install/reboot_in_progress note\nd-i grub-installer/only_debian boolean true\nd-i grub-installer/with_other_os boolean true\nd-i keymap select us\nd-i mirror/country string manual\nd-i mirror/http/directory string /debian\nd-i mirror/http/hostname string httpredir.debian.org\nd-i mirror/http/proxy string\n# Alternatively, you may specify a disk to partition. If the system has only\n# one disk the installer will default to using that, but otherwise the device\n# name must be given in traditional, non-devfs format (so e.g. /dev/sda\n# and not e.g. /dev/discs/disc0/disc).\n# For example, to use the first SCSI/SATA hard disk:\n#d-i partman-auto/disk string /dev/sda\n# In addition, you'll need to specify the method to use.\n# The presently available methods are:\n# - regular: use the usual partition types for your architecture\n# - lvm:     use LVM to partition the disk\n# - crypto:  use LVM within an encrypted partition\nd-i partman-auto/method string regular\n\n# If one of the disks that are going to be automatically partitioned\n# contains an old LVM configuration, the user will normally receive a\n# warning. This can be preseeded away...\nd-i partman-lvm/device_remove_lvm boolean true\n# The same applies to pre-existing software RAID array:\nd-i partman-md/device_remove_md boolean true\n# And the same goes for the confirmation to write the lvm partitions.\nd-i partman-lvm/confirm boolean true\nd-i partman-lvm/confirm_nooverwrite boolean true\n\n# For LVM partitioning, you can select how much of the volume group to use\n# for logical volumes.\n#d-i partman-auto-lvm/guided_size string max\n#d-i partman-auto-lvm/guided_size string 10GB\n#d-i partman-auto-lvm/guided_size string 50%\n\n# You can choose one of the three predefined partitioning recipes:\n# - atomic: all files in one partition\n# - home:   separate /home partition\n# - multi:  separate /home, /var, and /tmp partitions\nd-i partman-auto/choose_recipe select atomic\nd-i partman-basicfilesystems/no_swap boolean false\nd-i partman-auto/expert_recipe string \\\n    single-root :: \\\n\t\t  1000 50 -1 ext4 \\\n      $primary{ } \\\n\t\t\t$bootable{ } \\\n\t\t\tmethod{ format } \\\n      format{ } \\\n\t\t\tuse_filesystem{ } \\\n\t\t\tfilesystem{ ext4 } \\\n      mountpoint{ / } .\nd-i partman-auto/choose_recipe select single-root\nd-i partman/mount_style select uuid\nd-i partman/choose_partition select finish\nd-i partman/confirm boolean true\nd-i partman/confirm_nooverwrite boolean true\nd-i partman/confirm_write_new_label boolean true\nd-i passwd/root-login boolean false\nd-i passwd/root-password-again password password\nd-i passwd/root-password password password\nd-i passwd/user-fullname string builderbot\nd-i passwd/user-uid string 1000\nd-i passwd/user-password password password\nd-i passwd/user-password-again password password\nd-i passwd/username string builderbot\nd-i pkgsel/include string openssh-server cryptsetup build-essential libssl-dev libreadline-dev zlib1g-dev linux-source dkms nfs-common open-vm-tools\nd-i pkgsel/install-language-support boolean false\nd-i pkgsel/update-policy select none\nd-i pkgsel/upgrade select full-upgrade\n# Prevent packaged version of VirtualBox Guest Additions being installed:\nd-i preseed/early_command string sed -i \\\n  '/in-target/idiscover(){/sbin/discover|grep -v VirtualBox;}' \\\n  /usr/lib/pre-pkgsel.d/20install-hwpackages\nd-i time/zone string UTC\nd-i user-setup/allow-password-weak boolean true\nd-i user-setup/encrypt-home boolean false\nd-i preseed/late_command string sed -i '/^deb cdrom:/s/^/#/' /target/etc/apt/sources.list\napt-cdrom-setup apt-setup/cdrom/set-first boolean false\napt-mirror-setup apt-setup/use_mirror boolean true\npopularity-contest popularity-contest/participate boolean false\ntasksel tasksel/first multiselect standard, ssh-server"
  }
}'
```

> The above command returns JSON structured like getting a single preseed script: 

### HTTP Request

`POST https://api.gomorpheus.com/api/preseed-scripts`

### JSON Parameters

Parameter | Default | Description
--------- | ------- | -----------
fileName      |  | A name for the preseed script
content      |  | The script content

## Update a Preseed Script

```shell
curl -XPUT "https://api.gomorpheus.com/api/preseed-scripts/1" \
  -H "Authorization: BEARER access_token" \
  -H "Content-Type: application/json" \
  -d '{
  "preseedScript": {
    "fileName": "good ubuntu"
  }
}'
```

> The above command returns JSON structured like getting a single preseed script: 

### HTTP Request

`PUT https://api.gomorpheus.com/api/preseed-scripts/1`

### URL Parameters

Parameter | Description
--------- | -----------
ID | The ID of the preseed script

### JSON Parameters

See [Create](#create-a-preseed-script).

## Delete a Preseed Script

```shell
curl -XDELETE "https://api.gomorpheus.com/api/preseed-scripts/1" \
  -H "Authorization: BEARER access_token"
```

> The above command returns JSON Structured like this:

```json
{
  "success": true
}
```

Will delete a preseed script from the system and make it no longer usable.

### HTTP Request

`DELETE https://api.gomorpheus.com/api/preseed-scripts/:id`

### URL Parameters

Parameter | Description
--------- | -----------
ID | The ID of the preseed script
