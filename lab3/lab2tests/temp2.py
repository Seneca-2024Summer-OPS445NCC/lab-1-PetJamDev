#!/usr/bin/env python3


import os
ls_return = os.popen('ls')
print('The contents of ls_return:',ls_return)
whoami_return = os.popen('whoami')
print('The contents of whoami_return:',whoami_return)
ifconfig_return = os.popen('ifconfig')
print('The contents of ifconfig_return:',ifconfig_return)

import os
whoami_return=os.popen('whoami')
whoami_contents = whoami_return.read()
print('whoami_contents:',whoami_contents)
