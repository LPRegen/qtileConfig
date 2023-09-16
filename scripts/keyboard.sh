#!/bin/bash

# Remap caps lock to backspace.
setxkbmap -option caps:backspace
setxkbmap -option shift:both_capslock
xmodmap -e "clear Lock"
