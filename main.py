#!/usr/bin/env python

# This script will receive an online source and create the proper citations
# in APA format.
#
# Created by Jennifer and Wontez Morgan -- 25 November 2018


# Modules to be imported
import subprocess


# Declare Global Variables
lastName = 'Morgan'



# Clear the screen
subprocess.call('clear',shell=True)



# Enter Citation URL 
citeURL = raw_input("Enter Citation URL Here: ")

print (citeURL)

# Use wget to convert the website into a text document.
# *figure out a way to do this without using wget in the 
# future.

subprocess.call('wget '+ citeURL,shell=True)


