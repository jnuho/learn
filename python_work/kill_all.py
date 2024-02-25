
import psutil
import subprocess

# Kill all open/active processes
for proc in psutil.process_iter():
    proc.kill()