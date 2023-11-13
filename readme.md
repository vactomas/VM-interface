# OpenQA

This repository contains files for my Bachelor's thesis regarding automated visual app testing with the OpenQA framework.

## Single instance container setup using docker-compose

 - Install Podman Desktop - https://podman.io/

 - Clone the repository
 
 `git clone github.com/vactomas/openqa-app-testing.git`

 - Go into the directory and create folders iso and tests

 `cd openqa-app-testing/ && mkdir iso && mkdir tests`

 - Create the containers using the docker compose engine 

 `docker-compose up -d`

 - Inside Podman Desktop go to the Containers tab

 ![Alt text](images/podman-containers-tab.png)

 - Select the openqa-single-instance-1 container

 - Go to the Logs

 ![Alt text](images/podman-container-logs.png)

 - Find the API Key and Secret value and write it down

 ![Alt text](images/podman-api-key-secret.png)

 - Go to the Terminal tab

 ![Alt text](images/podman-terminal.png)

 - This example will use the OpenSUSE Live environment. To download OpenSUSE factory tests, use the following commands

 `/usr/share/openqa/script/fetchneedles`
 `/var/lib/openqa/share/tests/opensuse/products/opensuse/templates --apikey APIKEY --apisecret APISECRET` - replace APIKEY and APISECRETS with values you extracted earlier from Logs
 
 - Download the ISO file you want to test and copy it to the ./iso/ folder located in the folder, where docker-compose.yml is located. 

 - Copy the ISO file from /iso-images/ to /var/lib/openqa/share/factory/iso/

 - Use the following command to start the test of the iso

 `openqa-cli api -X POST isos \
         ISO=ISONAME.iso \
         DISTRI=opensuse \
         VERSION=Tumbleweed \
         FLAVOR=KDE-Live \
         ARCH=x86_64 \
         LIVECD = true \
         BUILD=BUILDID`

ISONAME and BUILDID are variables that need to be changed. The rest of this command presumes that you are using KDE-Live version of Tumbleweed.
