#!/usr/bin/env python3

#Author ID: pdevos

import subprocess

def free_space():
	total_space = subprocess.check_output("df -h | grep '/$' | awk '{print $4}'", shell=True).decode('utf-8')
	return total_space.strip()

print(free_space())
