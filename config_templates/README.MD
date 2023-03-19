# Config Generator

## This repo have multiple L2 switch config template's. Please click on required template and input value's. As a result, full config of switch will be generated and saved under config directory as a {{ Serial Number }}.cfg. This repo is getting mainly used for open PNP.

## Below are the list of roles (templates)

- [admin_only](https://git.cloud.com/NetworkInfrastructure/netcfg-generator/blob/master/roles/admin_only/vars/main.yml)
- [admin_voice](https://git.cloud.com/NetworkInfrastructure/netcfg-generator/blob/master/roles/admin_voice/vars/main.yml)
- [admin_wireless](https://git.cloud.com/NetworkInfrastructure/netcfg-generator/blob/master/roles/admin_wireless/vars/main.yml)
- [admin_voice_wireless](https://git.cloud.com/NetworkInfrastructure/netcfg-generator/blob/master/roles/admin_voice_wireless/vars/main.yml)
- [wireless_only](https://git.cloud.com/NetworkInfrastructure/netcfg-generator/blob/master/roles/wireless_only/vars/main.yml)
- [server_only](https://git.cloud.com/NetworkInfrastructure/netcfg-generator/blob/master/roles/server_only/vars/main.yml)
- [plant_only](https://git.cloud.com/NetworkInfrastructure/netcfg-generator/blob/master/roles/plant_only/vars/main.yml)
- [rma_only](https://git.cloud.com/NetworkInfrastructure/netcfg-generator/blob/master/roles/rma_only/vars/main.yml)
- [L3_only](https://git.cloud.com/NetworkInfrastructure/netcfg-generator/blob/master/roles/L3_only/vars/main.yml)

## For each type of template we expect to have different input values. Input values are getting captured in "var.yml" file of each role

## Admin-only, "var.yml" file looks like below, file has 2 sections, configuration section and cmdb section

### Configuration section

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

dhcp_subnet is the subnet which will be used to assing DHCP IP to new switch. Most of time this subnet will be admin subnet on existing L3 swithch.
if we select "plant_only" template to configure plant switch still the value for this variable will be "Admin" L3 switch subnet as DHCP ramge might not be avalible
for plant L3 switch subnet.

```
dhcp_subnet: 10.31.93.0/24

```

Serial Number of switch, if its stack please enter master switch Serial Number

```
Serial_Number: ADMINONLY
```

Hostname of switch

```
Hostname: edinalab43-swt
```

Domain name of the switch, kindly ensure you write correct domain as most of the region depend variables will be applied based on domain main, available domains are
gw.na.xyz.com,
gw.sg.xyz.com,
gw.eu.xyz.com,
gw.la.xyz.com

```
Domain_Name: gw.na.xyz.com
```

SVI IP address, mask and VLAN ID

```
Vlans:
  Admin:
    Primary_Address: 10.31.92.2
    Vlan_Id: 92
    mask: 255.255.255.0
```

If switch has 2 uplinks with port channel then need to add value's for port_channel, local_po, remote_po and Uplinks

```
port_channel: 'Yes'

local_po: '1'

remote_po: '2'

Uplinks:
- number: 1/0/23
  remote_SW_int: Gig 1/0/8
  type: GigabitEthernet
- number: 1/0/24
  remote_SW_int: Gig 1/0/9
  type: GigabitEthernet
```

If switch has single uplink with no port channel then need to add value only for port_channel and Uplinks

```
port_channel: 'No'

Uplinks:
- number: 1/0/23
  remote_SW_int: Gig 1/0/8
  type: GigabitEthernet
```

Uplink L3 switch name without domain name

```
remote_hostname_short: edinalab1-lcs
```

Admin Switch interface with port security please enter values for start_number, end_number with type of ports based on the switch model and number of switch ports to be configured.
Note: Selected ports range will be applied to each switch of stack.

```
admin_port_range:
  end_number: 15
  start_number: 1
  type: GigabitEthernet
```

Define the number of printer will be connected to switch, if its zero then value for printer_count variable need to add as a 0.

```
printer_count: 1
```

if printer_count: 1 or 2 or 3 below should be value for printer_ports if we have more printers please repeat sequence under printer_ports

```
printer_ports:
- name: abc123printer
  number: 1/0/17
  type: GigabitEthernet

printer_ports:
- name: abc123printer_1
  number: 1/0/17
  type: GigabitEthernet
- name: abc123printer_2
  number: 1/0/18
  type: GigabitEthernet

printer_ports:
- name: abc123printer_1
  number: 1/0/17
  type: GigabitEthernet
- name: abc123printer_2
  number: 1/0/18
  type: GigabitEthernet
- name: abc123printer_3
  number: 1/0/19
  type: GigabitEthernet
```

Similarly for WAP ports (Required for wireless_only, admin_wireless, admin_voice_wireless templates)

```
wap_ports_count: 3

wap_ports:
  - type: GigabitEthernet
    number: 2/0/16
    wap_name: edinalab45-wap
    wap_int: Gig 0/0
  - type: GigabitEthernet
    number: 2/0/17
    wap_name: edinalab46-wap
    wap_int: Gig 0/0
  - type: GigabitEthernet
    number: 2/0/19
    wap_name: edinalab47-wap
    wap_int: Gig 0/0
```

Similarly for static ports

```
static_ports_count: 1

static_ports:
- name: clock_1
  number: 1/0/18
  type: GigabitEthernet
```

Similarly for lobby_phone, with additional variable called lobby phone mac address

```
lobby_phone_count: 1

lobby_phone_ports:
- name: lobby_phone_1
  number: 1/0/16
  type: GigabitEthernet
  phone_mac_address: 1111.2222.333.4444
```

Define count for stack switch if its standalone switch it will be always 1

```
switch_number_in_stack: 1
```

if switch_number_in_stack is 1 or 2 or 3 below should be value for switch_number_in_stack_list ,

```
switch_number_in_stack_list:
- 1

switch_number_in_stack_list:
- 1
- 2

switch_number_in_stack_list:
- 1
- 2
- 3
```

Switch model of each switch,
if not a stack switch then,

```
switch_model_1: C9200-24P-E
```

If its stack of switches

```
switch_model_1: C9200-24P-E
switch_model_2: C9200-24P-E
switch_model_3: C9200-24P-E ans so on.
```

Default gateway of switch

```
ip_default_gateway: 10.31.92.1
```

Location of switch, follow SNMP location config guide below for more detail

```
snmp_location: '#r_NA#c_US#s_edina#b_Corporate#Bd_Excelsior_Blvr#Ro_Lab/1st_fl#Sh_Rack1'
```

Smart license token

```
smart_license_token: abc123
```

## SNMP location config guide

The new format is required to be used as base for CMDB updates. ! Use InfoQuest to get site details. This website is often updated by BRM;  
SNMP location format:
```
#r_Region#c_Country#s_Site#Bd_Building-Name#Ro_Room-Name-Floor>#Sh_Shaft-or-Rack
where

# r_Region: Region is one of the Standard NA, LATAM, EMEA, APAC;
# c_Country: Country is the International 2-digit code (ISO-Alpha 2) refer to (https://www.nationsonline.org/oneworld/country_code_list.html) E.g. United States – US;
# s_Site: Site is Site name in text format;
# Bd_Building-Name: Building Name is in text format (also numeric where applicable);
# Ro_Room-Name/ Floor: Room Name/ Floor is in text format (also numeric where applicable);
# Sh_Shaft-or-Rack: Shaft/Rack is in text format (also numeric where applicable);
```

For Ex.
```
#r_NA#c_US#s_ElkGrove#b_Corporate#Bd_Excelsior-Blvr#Ro_Lab/4th-fl#Sh_Rack1
where

# r_NA:North America
# c_US: United States of America
# s_edina: 76th Street Edina
# Ro_Lab/4th_fl: Lab, 4th floor
# Sh_Rack_1: Rack 1
```

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# *********CMDB_Section***********

This section creates the new entry in CMDB with status as "Being Assembled". Once the device is in network 
(post implementation) device status has to update manually. 

There is limitations from remedy, throught automation only new CI can be created, update on existing CI can not be done

If you use "rma_only" role then new CI entry will be created in CMDB with new switch SN. Faulty device SN entry should be marked as "return to vendor" manually as existing CI update can not be done due to remedy limitations
```
add_device:
  - Name: edinalab700-swt.gw.na.xyz.com -- switch_1
      SerialNumber: 5_TEST_REMEDY
      ShortDescription: "Network switch"
      Model: "WS-C9200L-24P"
      ManufacturerName: "Cisco Systems"
      SupportedBy: "L2_Ops"
      OwnedBy: "harshad"
      Status: "Being Assembled"
      PrimaryUsage: "Access Point"
      Room: "Storage"
      Floor: "1st"
      Impact: "3-Moderate/Limited"
      IsVirtual: "No"
      Capability: "Appliance"
      Site: "edina-MN-9320 Edina_BOULEVARD"
      Urgency: "3-Medium"
      Environment: "Production"
  - Name: edinalab700-swt.gw.na.xyz.com -- switch_2
      SerialNumber: 6_TEST_REMEDY
      ShortDescription: "Network switch"
      Model: "WS-C9200L-24P"
      ManufacturerName: "Cisco Systems"
      SupportedBy: "L2_Ops"
      OwnedBy: "harshad"
      Status: "Being Assembled"
      PrimaryUsage: "Access Point"
      Room: "Storage"
      Floor: "1st"
      Impact: "3-Moderate/Limited"
      IsVirtual: "No"
      Capability: "Appliance"
      Site: "edina-MN-9320 Edina_BOULEVARD"
      Urgency: "3-Medium"
      Environment: "Production"
```
