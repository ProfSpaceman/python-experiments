import subprocess
import os

HOME = os.environ['HOME']
DOTFILES = os.environ['DOTFILES']

'''
cmd = ['ls', HOME]
proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
o,e = proc.communicate()

print('Output: ' + o.decode('ascii'))
print('Error: ' + e.decode('ascii'))
print('code: ' + str(proc.returncode))
'''

cmd2 = ['cp', HOME + '/.config/i3/config', DOTFILES + '/i3/']
proc2 = subprocess.Popen(cmd2, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
o,e = proc2.communicate()

print('Output: ' + o.decode('ascii'))
print('Error: ' + e.decode('ascii'))
print('code: ' + str(proc2.returncode))


cmd3 = ['cp', HOME + '/.config/compton.conf', DOTFILES + '/compton/']
proc3 = subprocess.Popen(cmd3, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
o,e = proc3.communicate()

print('Output: ' + o.decode('ascii'))
print('Error: ' + e.decode('ascii'))
print('code: ' + str(proc3.returncode))


cmd4 = ['cp', HOME + '/.Xresources', DOTFILES]
proc4 = subprocess.Popen(cmd4, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
o,e = proc4.communicate()

print('Output: ' + o.decode('ascii'))
print('Error: ' + e.decode('ascii'))
print('code: ' + str(proc4.returncode))


cmd5 = ['cp', HOME + '/.bashrc', DOTFILES]
proc5 = subprocess.Popen(cmd5, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
o,e = proc5.communicate()

print('Output: ' + o.decode('ascii'))
print('Error: ' + e.decode('ascii'))
print('code: ' + str(proc5.returncode))


cmd6 = ['cp', HOME + '/.vimrc', DOTFILES]
proc6 = subprocess.Popen(cmd6, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
o,e = proc6.communicate()

print('Output: ' + o.decode('ascii'))
print('Error: ' + e.decode('ascii'))
print('code: ' + str(proc6.returncode))






cmd = ['ls', DOTFILES]
proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
o,e = proc.communicate()

print('Output: ' + o.decode('ascii'))
print('Error: ' + e.decode('ascii'))
print('code: ' + str(proc.returncode))

