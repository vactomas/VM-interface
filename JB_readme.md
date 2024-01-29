# Usage of QAD
* QAD is a http network protocol that allows you to communicate with the real HW
* check the repo for more details: https://gitlab.com/CodethinkLabs/qad/qad
* By following the instruction you can build your own `./qad` application

## Build your own QAD
* I was unable to build my own qad application without a container usage -> tons of libraries needed
* I built the QAD using the image in the QAD repo: `registry.gitlab.com/codethinklabs/qad/qad:bb504d5c-20230412T1336`
    1. Run the container and clone QAD repository
    2. Run `./compile.sh` in the cloned repo (probably some libraries will be needed to install - `libdrm` or ` libunistring-dev`)
    3. `cp -r /wayland-ivi-extension/ /qad/src`
    4. Clone repository `https://github.com/DaveGamble/cJSON` to the `/qad/src` -> rename to folder `cjson`
    5. `git reset --hard cb8693b0`
    6. `./compile.sh` -> this shall build `./qad` application
* Also build on raspberry ubuntu:
    1. image id `a96a9eb5ef71`
    2. just follow the steps described in the image (sometimes there are errors with CMakeLists something - ignore)
    3. some library files probably not needed (`pkg-config`, `libweston-9-dev`)
    4. follow the steps in the upper description

## Usage of QAD application on VM
* Copy QAD application to your VM
* Run QAD application `sudo ./qad` this shall automatically create QAD server on port `8080`
* In the VM setting, enable port forwarding on host ip `127.0.0.1:8080` to guest `10.0.2.15:8080`
* From windows run commnad: `curl http://127.0.0.1:8080/screen/2 --output test.png` - this should capture the screenshot of the VM
    * I was unable to generate screenshot (**Error getting CRCT**) -> maybe problem with VM display??
    * Touch the screen and button inputs works well
* also try on the raspberry pi ubunt
    * connect a physcial hdmi display
    * you must run weston also as sudo with `XDG_RUNTIME_DIR=/run/user/1000`
    * then another error occurs `Error getting CRTC '0': Operation not supported`
* make sure that `/etc/gdm3/custom.conf` has `WaylandEnable=False`
* then it somehow works


## Usage of QAD application on raspberry pi
* connect HDMI monitor to port HDMI1
* `XPG_RUNTIME_DIR=/run/user/100 ./qad -k card1`
* install `apt-get install libdrm-tests`
* run `modetest`
    * find encoder ID of your HDMI and find a mapping of encoder ID with crtc
    * this crtc use in commnad `curl http://127.0.0.1:8080/screen/97 --output test.png`
## Running ILM
1) weston must be running by `XDG_RUNTIME_DIR=/run/ser/1000 weston` as sudo
2) Run `XDG_RUNTIME_DIR=/run/user/1000 ./qad -s ilm`
3) does not work yet



## Misc
- to get qad architecture -> `file ./qad`
- weston service must run...
* have en
