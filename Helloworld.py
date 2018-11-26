#!/usr/bin/env python

# This is where the description will go
# This script will print hello world using python3.5
#
# Created by Jennifer and Wontez Morgan -- 25 November 2018


# Modules to be imported
import os
import subprocess
from datetime import datetime


# Declare Global Variables
lastName = 'Morgan'



# Clear the screen
subprocess.call('clear',shell=True)



# Get input from the user
YourName = raw_input("What is your name? ")

print ("I'm " + YourName +' '+ lastName + ', Hello World!')

