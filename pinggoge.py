import subprocess
import tempfile
import os
from pathlib import Path
import glob
import logging
import sys
import shutil

            
processes = []
for num in range(0,180):
    f = tempfile.TemporaryFile()

    p = subprocess.Popen(
                    'ping 8.8.8.8 -c 6'
        ,shell=True, stderr=subprocess.STDOUT,stdout=f
    )
    
    processes.append((p, f, num))
for p, f, n in processes:
        
        p.wait()
        f.seek(0)
        with open('pring.test.home.vpn.log', 'a+') as specieslogfile:
            specieslogfile.write(f.read().decode('utf-8'))

