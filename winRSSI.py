import subprocess
import elevatePS

name = "win-rssi"
filePath = 'C:\Users\William Ao\Github\Wifi-RSSI-Windows\elevate.ps1'  #path to elevate powershell script

from subprocess import Popen, PIPE
import numpy
from sys import version_info

class RSSI_Scan(object):
    def __init__(self, interface):
        self.interface

    def getRawNetworkScan(self):
        command = "netsh wlan show networks mode=bssid"
        ipconfig = subprocess.getoutput(command)
        splitoutput = ipconfig.splitlines()
        count = 0
        flag = True
        #count number of bssids to initialize dictionanry
        for i in range(len(splitoutput)):
            if ("BSSID" in splitoutput[i]):
                count+=1
        ssids = [dict() for x in range(count)]

        for i in range(len(splitoutput)):
            if ("SSID" in splitoutput[i]):
                ssids[count]["SSID"] = splitoutput[i].split()[3]
                flag = True
                while(flag)
                    ssids[count]["BSSID"] = splitoutput[i + 4].split()[2]
                    ssids[count]["Signal"] = splitoutput[i + 5].split()[2]
                    ssids[count]["Channel"] = splitoutput[i + 7].split()[2]

        elevatePS.netshRefresh(filePath)