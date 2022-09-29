# tigattack's CarPi Setup

### [ansible](/ansible/)

This directory contains an Ansible playbook to provision the Pi from a stock install of OpenAuto.

### [openauto](/openauto/)

This directory contains my OpenAuto configuration files.

Information regarding OpenAuto system configuration can be found [here](https://bluewavestudio.io/community/thread-2042.html).

[openauto_license.dat.SAMPLE](OpenAuto/openauto_license.dat.SAMPLE) is an example file. To use it, the contents should be replaced with your key and the file should be renamed to not include `.SAMPLE`.

### [pi-boot](/pi-boot/)

This directory contains files to configure the Pi's display, WiFi, and SSH.

Copy all files to the boot partion, **except** those marked 'no copy' or 'sample'.

### [scripts](/scripts/)

This directory contains scripts to be copied to the Pi, once the OS has been installed.
