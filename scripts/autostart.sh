#!/bin/bash

# notifications
dunst &
# set bg
$HOME/.fehbg &
# keyboard remaps
$HOME/.config/qtile/scripts/keyboard.sh

# Kill if already running
# killall -9 picom xfce4-power-manager ksuperkey duns

# Launch notification daemon
# dunst -config $HOME/.config/qtile/dunstrc &

# power manager and picom start
# xfce4-power-manager &
# picom --config $HOME/.config/qtile/picom.conf &

# if [[ ! `pidof xfce-polkit` ]]; then
# /usr/lib/xfce-polkit/xfce-polkit &
# fi
