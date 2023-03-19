#### [7.2.0] - 2022-09-21

#### Removed
- NA

#### Added

- NA

#### Changed

- Few templates to resolve invalid command issue 


#### [7.1.0] - 2022-08-06

#### Removed
- NA

#### Added

- Sample config template files

#### Changed

- Few templates to resolve issue for all "60CX" models 

#### [7.0.0] - 2022-08-06

#### Removed
- NA

#### Added

- Sample config template files

#### Changed

- NA

#### [7.0.0] - 2022-05-06

#### Removed
- Temp removed L3 templates

#### Added

- NA

#### Changed

- Changes the few templates under templates dir so that they can be downloaded to switch security playbook


#### [6.0.0] - 2021-06-25

- NA

#### Added

- Adding new role/template for Cisco L3 switch configuration for 9300/9400 switches

#### Changed

- NA


#### [5.6.0] - 2021-06-25

- NA

#### Added

- NA

#### Changed

- Updated all main.yml var files for each config templates by moving remote_hostname variable under uplink interface so that eng can use separate hostnames in case of dual network

#### [5.5.0] - 2021-06-25

- NA

#### Added

- NA

#### Changed

- Updated all main.yml var files for each config templates by adding new variable to ask if device is already in network

#### [5.4.0] - 2021-06-25

- NA

#### Added

- NA

#### Changed

- Updated all main.j2 to remove smart template as we have seen issue with stack switches

#### [5.3.0] - 2021-06-25

- NA

#### Added

- NA

#### Changed

- Updated main.j2 to update PO config

### Fixed

- NA

#### [5.2.0] - 2021-06-24

- NA

#### Added

- NA

#### Changed

- Small changes on multiple files

### Fixed

- NA

#### [5.1.0] - 2021-06-23

- NA

#### Added

- NA

#### Changed

- README.MD

### Fixed

- NA

#### [5.0.0] - 2021-06-23

- <https://dev.azure.com/xyz-xyzGlobal/Global_Networks_Automation_Initiative/_workitems/edit/698796>

#### Added

- Addedd basic error checking using ping, if int vlan ip is reachable script will be aborded

#### Changed

- main.yml

### Fixed

- NA

#### [4.2.0] - 2021-06-18

- <https://dev.azure.com/xyz-xyzGlobal/Global_Networks_Automation_Initiative/_workitems/edit/585717>

#### Added

- Adding smart license template

#### Changed

-

### Fixed

- NA

#### [3.0.0] - 2021-05-24

- <https://dev.azure.com/xyz-xyzGlobal/Global_Networks_Automation_Initiative/_workitems/edit/585717>

#### Added

- NA

#### Changed

- Final templates

### Fixed

- NA

#### [2.0.0] - 2021-05-24

#### Added

- Adding multiple templates

#### Changed

- NA

### Fixed

- NA

#### [1.0.1] - 2021-05-23

- [569108](https://dev.azure.com/xyz-xyzGlobal/Global_Networks_Automation_Initiative/_workitems/edit/569108)

#### Added

- Created a template for a device which has admin_voice_wireelss and server VLAN's and it also has printer and clock ports

#### Changed

- Multiple files

### Fixed

- few bugs
