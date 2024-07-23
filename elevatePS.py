import subprocess
import sys

def netshRefresh(filePath):
    arg = r"""
            Start-Process -Verb RunAs -Wait powershell.exe -Arge "
                -noprofile -c Set-Location \'"$PWD\'"; & {0}
                "
            """
    arg = arg.format(filePath)
    p = subprocess.Popen(
        [
            "powershell.exe",
            "-noprofile", "-c",
            arg
        ],
        stdout=sys.stdout
    )
    p.communicate()
