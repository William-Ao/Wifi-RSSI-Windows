# RSSI Python module

Based on Juan Antonio Villagomez's existing RSSI Python library, adapted for Windows. In Linux utilizing the iwlist command with sudo forces a new scan of network devices, while on Windows a restart of the wlansvc service through Powershell must be done every time. This library attempts to automate that process.

Upcoming changes/features
- [ ] Finish implementing baseline scanning and scraping of WAP data. 
- [ ] Create class for localization
- [ ] Create documentation
- [ ] Create Pip package
- [ ] Create examples

Feature requests and recoomendations are welcome!

From Villagomez's Readme: "With IoT projects at an all time high, there is a continuous need for positioning and localization systems in places where 
GPS localiztion is not available. RSSI-based localization offers the ability to find an unknown position using the 
RSSI (relative received signal strength) of nearby access-points (wifi routers). RSSI-based localiztion algortihms require 'n' number
of access points, where 'n' >= 3 access points. With the development of wireless are networks and smart devices, the number
of WIFI access point in buildings is increasing, as long as a mobile smart device can detect three or more
known WIFI hotspots’ positions, it would be relatively easy to realize self-localization (Usually WIFI access points
locations are fixed, but modifications can be made for moving access points)."

This library will be very similar to his for sake of simplicity, containing two classes, 'winRSSI' and 'rssiLocalizer'.

winRSSI is used to find and return information on all available access points, within range.
A 'networks' list can be provided as an argument to filter networks of interest (WIP).

rssiLocalizer is used for self-localization, using the information returned by winRSSI. this 
class can NOT be used, without the use of THREE or more known accesspoints (WIP).

The algorithm used in this module is based off of 'Indoor Positioning Techniques using RSSI from Wireless Devices' by Asif Ahmed Sohan et al. https://ieeexplore.ieee.org/document/9038591

I'm building this library just to fulfill the needs of Windows users who may want to play around with RSSI localization but don't have a suitable Linux device to do so. I discovered during a Hackathon that the VM I was running didn't allow for scanning of networks on the virtual network card, so my team was stuck with a very hacked together solution that just pulled cached RSSI values. While this implementation isn't very elegant due to operating system limitations, I hope this library will be helpful for someone. 

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

A Python interpreter will be neccesary to run this module. Package is compatible with Python 2.x or 3.x.

The NumPy library will need to be installed, before using this package. We will be updating this package to include the NumPy dependency. See 'Built With' section for installation of NumPy.

### Installing

The RSSI package can be installed by cloning this GitHub repo. Future releases will include a pip package.
```
git clone https://github.com/William-Ao/Wifi-RSSI-Windows.git
```
### Classes


