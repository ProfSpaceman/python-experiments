import subprocess
import os

HOME = os.environ['HOME']
DOTFILES = os.environ['DOTFILES']

cmd2 = ['cp', HOME + '/.config/i3/config', DOTFILES + '/i3/']
cmd3 = ['cp', HOME + '/.config/compton.conf', DOTFILES + '/compton/']
cmd4 = ['cp', HOME + '/.Xresources', DOTFILES]
cmd5 = ['cp', HOME + '/.bashrc', DOTFILES]
cmd6 = ['cp', HOME + '/.vimrc', DOTFILES]
cmd = ['ls', HOME]

commands = [cmd2,cmd3,cmd4,cmd5,cmd6,cmd]
command_string = ''

proc = subprocess.Popen('/bin/bash', stdin=subprocess.PIPE ,stdout=subprocess.PIPE, stderr=subprocess.PIPE)
for i in range(6):
    for j in range(len(commands[i])):
        command_string = command_string + ' ' + commands[i][j]
    command_string = command_string + '\n'

o,e = proc.communicate(command_string.encode('utf-8'))
print('Output: ' + o.decode('ascii'))
print('Error: ' + e.decode('ascii'))
print('code: ' + str(proc.returncode))
