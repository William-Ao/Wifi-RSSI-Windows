import subprocess
import sys

def netshRefresh(filePath):
    p = subprocess.Popen(
        [
            "powershell.exe",
            "-noprofile", "-c",
            r"""
            Start-Process -Verb RunAs -Wait powershell.exe -Arge "
                -noprofile -c Set-Location \'"$PWD\'"; & C:\Users\William Ao\Github\Wifi-RSSI-Windows\elevate.ps1
                "
            """
        ],
        stdout=sys.stdout
    )
    p.communicate