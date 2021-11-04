.. _Release Packages:

***************************
|morphver| Release Packages
***************************

|morpheus| Appliance Packages
=============================

The |morpheus| Appliance Package is the main install package used to install and upgrade |morpheus| Appliances. 

|morpheus| Repository Packages
==============================

The |morpheus| Repository Packages contain the Node and VM Node Packages required to install and upgrade the |morpheus| agent and provision Docker Hosts.

|morpheus| Supplemental Appliance Packages
==========================================

The |morpheus| Supplemental Appliance Packages contain all of the |morpheus| Repository Packages as well as additional packages required to install |morpheus| Appliance Packages in environments that cannot access |repo_host_url|

..
 {
  "manifest_format": 2,
  "software": {
    "preparation": {
      "locked_version": "1.0.0",
      "locked_source": null,
      "source_type": "project_local",
      "described_version": "1.0.0",
      "license": "project_license"
    },
    "config_guess": {
      "locked_version": "84f04b02a7e2fc8eaa9d52deee5f6d57b06fe447",
      "locked_source": {
        "git": "https://github.com/chef/config-mirror.git"
      },
      "source_type": "git",
      "described_version": "master",
      "license": "GPL-3.0 (with exception)"
    },
    "ncurses": {
      "locked_version": "5.9",
      "locked_source": {
        "md5": "8cb9c412e5f2d96bc6f459aa8c6282a1",
        "url": "https://ftp.gnu.org/gnu/ncurses/ncurses-5.9.tar.gz"
      },
      "source_type": "url",
      "described_version": "5.9",
      "license": "MIT"
    },
    "libedit": {
      "locked_version": "20120601-3.0",
      "locked_source": {
        "md5": "e50f6a7afb4de00c81650f7b1a0f5aea",
        "url": "http://www.thrysoee.dk/editline/libedit-20120601-3.0.tar.gz"
      },
      "source_type": "url",
      "described_version": "20120601-3.0",
      "license": "BSD-3-Clause"
    },
    "pcre": {
      "locked_version": "8.38",
      "locked_source": {
        "md5": "8a353fe1450216b6655dfcf3561716d9",
        "url": "http://downloads.sourceforge.net/project/pcre/pcre/8.38/pcre-8.38.tar.gz"
      },
      "source_type": "url",
      "described_version": "8.38",
      "license": "BSD-2-Clause"
    },
    "cacerts": {
      "locked_version": "2019-10-16",
      "locked_source": {
        "url": "https://curl.haxx.se/ca/cacert-2019-10-16.pem",
        "sha256": "5cd8052fcf548ba7e08899d8458a32942bf70450c9af67a0850b4c711804a2e4"
      },
      "source_type": "url",
      "described_version": "2019-10-16",
      "license": "MPL-2.0"
    },
    "openssl": {
      "locked_version": "1.1.1g",
      "locked_source": {
        "url": "https://www.openssl.org/source/openssl-1.1.1g.tar.gz",
        "extract": "lax_tar",
        "sha256": "ddb04774f1e32f0c49751e21b67216ac87852ceb056b75209af2443400636d46"
      },
      "source_type": "url",
      "described_version": "1.1.1g",
      "license": "OpenSSL"
    },
    "zlib": {
      "locked_version": "1.2.11",
      "locked_source": {
        "sha256": "c3e5e9fdd5004dcb542feda5ee4f0ff0744628baf8ed2dd5d66f8ca1197cb1a1",
        "url": "https://zlib.net/fossils/zlib-1.2.11.tar.gz"
      },
      "source_type": "url",
      "described_version": "1.2.11",
      "license": "Zlib"
    },
    "erlang": {
      "locked_version": "22.3",
      "locked_source": {
        "url": "https://github.com/erlang/otp/archive/OTP-22.3.tar.gz",
        "sha256": "886e6dbe1e4823c7e8d9c9c1ba8315075a1a9f7717f5a1eaf3b98345ca6c798e"
      },
      "source_type": "url",
      "described_version": "22.3",
      "license": "Apache-2.0"
    },
    "libiconv": {
      "locked_version": "1.15",
      "locked_source": {
        "url": "https://ftp.gnu.org/pub/gnu/libiconv/libiconv-1.15.tar.gz",
        "sha256": "ccf536620a45458d26ba83887a983b96827001e92a13847b45e4925cc8913178"
      },
      "source_type": "url",
      "described_version": "1.15",
      "license": "LGPL-2.1"
    },
    "pkg-config": {
      "locked_version": "0.28",
      "locked_source": {
        "md5": "aa3c86e67551adc3ac865160e34a2a0d",
        "url": "https://pkgconfig.freedesktop.org/releases/pkg-config-0.28.tar.gz"
      },
      "source_type": "url",
      "described_version": "0.28",
      "license": "Unspecified"
    },
    "libtirpc": {
      "locked_version": "1.2.6",
      "locked_source": {
        "sha256": "4278e9a5181d5af9cd7885322fdecebc444f9a3da87c526e7d47f7a12a37d1cc",
        "url": "https://downloads.sourceforge.net/libtirpc/libtirpc-1.2.6.tar.bz2"
      },
      "source_type": "url",
      "described_version": "1.2.6",
      "license": "BSD-3-Clause"
    },
    "mysql": {
      "locked_version": "5.7.32",
      "locked_source": {
        "url": "https://dev.mysql.com/get/Downloads/MySQL-5.7/mysql-boost-5.7.32.tar.gz",
        "sha256": "9a8a04a2b0116ccff9a8d8aace07aaeaacf47329b701c5dfa9fa4351d3f1933b"
      },
      "source_type": "url",
      "described_version": "5.7.32",
      "license": "Unspecified"
    },
    "openjdk-elasticsearch": {
      "locked_version": "14.0.2+12",
      "locked_source": {
        "url": "https://github.com/AdoptOpenJDK/openjdk14-binaries/releases/download/jdk-14.0.2%2B12/OpenJDK14U-jdk_x64_linux_hotspot_14.0.2_12.tar.gz",
        "sha256": "7d5ee7e06909b8a99c0d029f512f67b092597aa5b0e78c109bd59405bbfa74fe"
      },
      "source_type": "url",
      "described_version": "14.0.2+12",
      "license": "Unspecified"
    },
    "libtool": {
      "locked_version": "2.4.2",
      "locked_source": {
        "md5": "d2f3b7d4627e69e13514a40e72a24d50",
        "url": "https://ftp.gnu.org/gnu/libtool/libtool-2.4.2.tar.gz"
      },
      "source_type": "url",
      "described_version": "2.4.2",
      "license": "GPL-2.0"
    },
    "libffi": {
      "locked_version": "3.2.1",
      "locked_source": {
        "md5": "83b89587607e3eb65c70d361f13bab43",
        "url": "ftp://sourceware.org/pub/libffi/libffi-3.2.1.tar.gz"
      },
      "source_type": "url",
      "described_version": "3.2.1",
      "license": "MIT"
    },
    "libyaml": {
      "locked_version": "0.1.7",
      "locked_source": {
        "sha256": "8088e457264a98ba451a90b8661fcb4f9d6f478f7265d48322a196cec2480729",
        "url": "https://pyyaml.org/download/libyaml/yaml-0.1.7.tar.gz"
      },
      "source_type": "url",
      "described_version": "0.1.7",
      "license": "MIT"
    },
    "ruby": {
      "locked_version": "2.5.7",
      "locked_source": {
        "sha256": "0b2d0d5e3451b6ab454f81b1bfca007407c0548dea403f1eba2e429da4add6d4",
        "url": "https://cache.ruby-lang.org/pub/ruby/2.5/ruby-2.5.7.tar.gz"
      },
      "source_type": "url",
      "described_version": "2.5.7",
      "license": "BSD-2-Clause"
    },
    "rubygems": {
      "locked_version": "2.7.9",
      "locked_source": null,
      "source_type": "project_local",
      "described_version": "2.7.9",
      "license": "MIT"
    },
    "bundler": {
      "locked_version": "1.16.6",
      "locked_source": null,
      "source_type": "project_local",
      "described_version": "1.16.6",
      "license": "MIT"
    },
    "ohai": {
      "locked_version": "14.14.0",
      "locked_source": {
        "url": "https://github.com/chef/ohai/archive/v14.14.0.tar.gz",
        "sha256": "3c25b72b6949f4446218a4d32ee79ae37324576c14b26eebc3e0a7cff7368a2f"
      },
      "source_type": "url",
      "described_version": "14.14.0",
      "license": "Apache-2.0"
    },
    "appbundler": {
      "locked_version": "d2a4a3f2569bdb3977f9ef9172656ecffb9aaa1d",
      "locked_source": {
        "git": "https://github.com/chef/appbundler.git"
      },
      "source_type": "git",
      "described_version": "master",
      "license": "Apache-2.0"
    },
    "openjdk-jre": {
      "locked_version": "8u275",
      "locked_source": {
        "url": "https://github.com/AdoptOpenJDK/openjdk8-binaries/releases/download/jdk8u275-b01/OpenJDK8U-jre_x64_linux_hotspot_8u275b01.tar.gz",
        "sha256": "a044da8bf198ad756b2bbb83f3d48ddeeffb934b9a9974d9b9bb6d0034413a83"
      },
      "source_type": "url",
      "described_version": "8u275",
      "license": "Unspecified"
    },
    "popt": {
      "locked_version": "1.16",
      "locked_source": {
        "url": "ftp://anduin.linuxfromscratch.org/BLFS/popt/popt-1.16.tar.gz",
        "sha256": "e728ed296fe9f069a0e005003c3d6b2dde3d9cad453422a10d6558616d304cc8"
      },
      "source_type": "url",
      "described_version": "1.16",
      "license": "MIT"
    },
    "rsync": {
      "locked_version": "3.1.1",
      "locked_source": {
        "md5": "43bd6676f0b404326eee2d63be3cdcfe",
        "url": "https://rsync.samba.org/ftp/rsync/src/rsync-3.1.1.tar.gz"
      },
      "source_type": "url",
      "described_version": "3.1.1",
      "license": "GPL-3.0"
    },
    "tomcat": {
      "locked_version": "9.0.39",
      "locked_source": {
        "sha512": "307ca646bac267e529fb0862278f7133fe80813f0af64a44aed949f4c7a9a98aeb9bd7f08b087645b40c6fefdd3a7fe519e4858a3dbf0a19c38c53704f92b575",
        "url": "https://archive.apache.org/dist/tomcat/tomcat-9/v9.0.39/bin/apache-tomcat-9.0.39.tar.gz"
      },
      "source_type": "url",
      "described_version": "9.0.39",
      "license": "Unspecified"
    },
    "morpheus-crypto-cli": {
      "locked_version": "0.0.1",
      "locked_source": null,
      "source_type": "project_local",
      "described_version": "0.0.1",
      "license": "Unspecified"
    },
    "mysql2-gem": {
      "locked_version": "0.3.18",
      "locked_source": null,
      "source_type": "project_local",
      "described_version": "0.3.18",
      "license": "Unspecified"
    },
    "mixlib-versioning-gem": {
      "locked_version": "1.1.0",
      "locked_source": null,
      "source_type": "project_local",
      "described_version": "1.1.0",
      "license": "Unspecified"
    },
    "morpheus-config-template": {
      "locked_version": "1.0.0",
      "locked_source": {
        "path": "/root/workspace/morpheus-appliance-packages/files/morpheus-config-template"
      },
      "source_type": "path",
      "described_version": "1.0.0",
      "license": "Unspecified"
    },
    "omnibus-ctl": {
      "locked_version": "c514d1d4ecb24e30fdbd310b2dd038b2192b4fa7",
      "locked_source": {
        "git": "git://github.com/chef/omnibus-ctl.git"
      },
      "source_type": "git",
      "described_version": "0.3.6",
      "license": "Unspecified"
    },
    "elastic-util-gem": {
      "locked_version": "0.1.6",
      "locked_source": null,
      "source_type": "project_local",
      "described_version": "0.1.6",
      "license": "Unspecified"
    },
    "nginx": {
      "locked_version": "1.19.3",
      "locked_source": {
        "url": "https://nginx.org/download/nginx-1.19.3.tar.gz",
        "sha256": "91e5b74fa17879d2463294e93ad8f6ffc066696ae32ad0478ffe15ba0e9e8df0"
      },
      "source_type": "url",
      "described_version": "1.19.3",
      "license": "BSD-2-Clause"
    },
    "rabbitmq": {
      "locked_version": "3.8.9",
      "locked_source": {
        "url": "https://github.com/rabbitmq/rabbitmq-server/releases/download/v3.8.9/rabbitmq-server-generic-unix-3.8.9.tar.xz",
        "sha256": "fe1f1ef9b1bd8362421d689ec9b73cb33c8aaf96acf990df6549e3c0275b7aa0"
      },
      "source_type": "url",
      "described_version": "3.8.9",
      "license": "MPL-2.0"
    },
    "elasticsearch": {
      "locked_version": "7.8.1",
      "locked_source": {
        "url": "https://bertramlabs-chef.s3.us-west-1.amazonaws.com/files/elasticsearch/elasticsearch-oss-7.8.1-no-jdk-linux-x86_64.tar.gz",
        "sha256": "504fe9a4bd70526dcc60eb59098506554192eeea32529292664448f59719d218"
      },
      "source_type": "url",
      "described_version": "7.8.1",
      "license": "Unspecified"
    },
    "chef": {
      "locked_version": "14.14.29",
      "locked_source": {
        "url": "https://github.com/chef/chef/archive/v14.14.29.tar.gz",
        "sha256": "c892bd1406571118928d7cf176a5324a857c45214876ab3341910a66dd850b5e"
      },
      "source_type": "url",
      "described_version": "14.14.29",
      "license": "Apache-2.0"
    },
    "runit": {
      "locked_version": "2.1.1",
      "locked_source": {
        "md5": "8fa53ea8f71d88da9503f62793336bc3",
        "url": "http://smarden.org/runit/runit-2.1.1.tar.gz"
      },
      "source_type": "url",
      "described_version": "2.1.1",
      "license": "BSD-3-Clause"
    },
    "morpheus-check-server": {
      "locked_version": "2.0.0",
      "locked_source": {
        "url": "https://jenkins.prod.den.bertramlabs.com/downloads/morpheus-check-server-2.0.0.jar",
        "sha256": "198cfbc6727008b6a7f07bad5c902f6f9f76254db7c6aea74f19a1dfa84df237"
      },
      "source_type": "url",
      "described_version": "2.0.0",
      "license": "Unspecified"
    },
    "morpheus-ui": {
      "locked_version": "5.2.1",
      "locked_source": null,
      "source_type": "project_local",
      "described_version": "5.2.1",
      "license": "Unspecified"
    },
    "morpheus-cookbooks": {
      "locked_version": "1.0.0",
      "locked_source": {
        "path": "/root/workspace/morpheus-appliance-packages/files/morpheus-cookbooks"
      },
      "source_type": "path",
      "described_version": "1.0.0",
      "license": "Unspecified"
    },
    "morpheus-ctl": {
      "locked_version": "1.0.0",
      "locked_source": {
        "path": "/root/workspace/morpheus-appliance-packages/files/morpheus-ctl-commands"
      },
      "source_type": "path",
      "described_version": "1.0.0",
      "license": "Unspecified"
    },
    "ruby-cleanup": {
      "locked_version": null,
      "locked_source": null,
      "source_type": "project_local",
      "described_version": null,
      "license": "project_license"
    },
    "version-manifest": {
      "locked_version": "0.0.1",
      "locked_source": null,
      "source_type": "project_local",
      "described_version": "0.0.1",
      "license": "project_license"
    }
  },
  "build_version": "5.2.1",
  "build_git_revision": "0fb72ff2c0a63b5ffd1430bc4fed5d091aa8ea7c",
  "license": "Unspecified"
 }
