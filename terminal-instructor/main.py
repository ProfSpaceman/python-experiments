import subprocess
import os


HOME = os.environ['HOME']

cmd = ['ls', HOME]
proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
o,e = proc.communicate()

print('Output: ' + o.decode('ascii'))
print('Error: ' + e.decode('ascii'))
print('code: ' + str(proc.returncode))

cmd2 = ['touch', HOME + '/python_tests/dotfile-manager/potato2']
proc2 = subprocess.Popen(cmd2, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
o,e = proc2.communicate()

print('Output: ' + o.decode('ascii'))
print('Error: ' + e.decode('ascii'))
print('code: ' + str(proc.returncode))
