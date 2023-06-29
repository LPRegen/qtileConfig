# Imports for startup
import os
import subprocess

# Imports of PY Libraries
from libqtile import bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy

# from libqtile.utils import guess_terminal


# Hook for startup
@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser("~/.config/qtile/scripts/autostart.sh")
    subprocess.Popen([home])


# Variables
mod = "mod4"
terminal = "kitty"
ranger = "{terminal} -e ranger".format(terminal=terminal)

# Color variables
color_focus = "#cf590a"
color_normal = "#bda68a"
color_inactive = "#f5bf8c"
color_active = "#eb7050"
other_current_screen_color_inactive = "#3478d1"

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between monitors
    Key([mod], "Tab", lazy.next_screen(), desc="Next monitor"),
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    # Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key(
        [mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"
    ),
    Key(
        [mod, "shift"],
        "l",
        lazy.layout.shuffle_right(),
        desc="Move window to the right",
    ),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key(
        [mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"
    ),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    # Key(
    #     [mod, "shift"],
    #     "Return",
    #     lazy.layout.toggle_split(),
    #     desc="Toggle between split and unsplit sides of stack",
    # ),
    # Spawn terminal
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    # Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    # Kill focused window.
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    # Reload Qtile configuration
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    # Shutdown Qtile
    # Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    # launcher
    # Key([mod], "r", lazy.spawncmd(prompt='Launch'), desc="Spawn a command using a prompt widget"),
    # Launch dmenu
    Key([mod], "r", lazy.spawn("dmenu_run")),
    # Launch powermenu
    Key(
        [mod], "x", lazy.spawn("rofi -show power-menu -modi power-menu:rofi-power-menu")
    ),
    # Volume Control
    Key(
        [],
        "XF86AudioLowerVolume",
        lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ -5%"),
    ),
    Key(
        [],
        "XF86AudioRaiseVolume",
        lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ +5%"),
    ),
    Key([], "XF86AudioMute", lazy.spawn("pactl set-sink-mute @DEFAULT_SINK@ toggle")),
    # Play/pause audio
    Key([], "XF86AudioPlay", lazy.spawn("playerctl play-pause")),
    # XF86AudioNext
    Key([], "XF86AudioNext", lazy.spawn("playerctl next")),
    # XF86AudioPrev
    Key([], "XF86AudioPrev", lazy.spawn("playerctl previous")),
    # Screen brightness
    Key([], "XF86MonBrightnessUp", lazy.spawn("light -A 10")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("light -U 10")),
    # Toggle keyboard variants
    Key(
        [mod],
        "space",
        lazy.widget["keyboardlayout"].next_keyboard(),
        desc="Next KB layout.",
    ),
    # Programs
    Key([mod, "shift"], "f", lazy.spawn(ranger)),
    Key([mod, "shift"], "w", lazy.spawn("firefox-developer-edition")),
    Key([mod, "shift"], "b", lazy.spawn("blueberry")),
]

groups = []

group_names = [
    "1",
    "2",
    "3",
]

group_labels = [
    "  ",
    "  ",
    "  ",
]

for i in range(len(group_names)):
    groups.append(
        Group(
            name=group_names[i],
            label=group_labels[i],
        )
    )

for i in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            # Key(
            #     [mod, "shift"],
            #     i.name,
            #     lazy.window.togroup(i.name, switch_group=True),
            #     desc="Switch to & move focused window to group {}".format(i.name),
            # ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name),
                desc="move focused window to group {}".format(i.name),
            ),
        ]
    )

# Layouts
layouts = [
    layout.Columns(
        border_focus=[color_focus],
        border_normal=[color_normal],
        border_width=2,
        margin=2,
        insert_position=1,
    ),
    # layout.MonadTall(border_focus=color_focus, border_normal=color_normal),
]

widget_defaults = dict(
    font="Hasklug Nerd Font",
    fontsize=15,
    padding=3,
)

extension_defaults = widget_defaults.copy()

spacer = widget.Spacer()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.Spacer(length=2),
                widget.GroupBox(
                    fontsize=24,
                    spacing=8,
                    padding_x=0,
                    padding_y=-1.5,
                    borderwidth=2,
                    inactive=color_inactive,
                    highlight_method="line",
                    active=color_active,
                    this_current_screen_border=color_focus,
                    this_screen_border=color_normal,
                    other_current_screen_border=color_focus,
                    other_screen_border=other_current_screen_color_inactive,
                ),
                spacer,
                widget.Systray(),
                # CPU thermal sensor
                widget.ThermalSensor(
                    tag_sensor="CPU",
                    format="{temp:.0f} 󰔄",
                    threshold=50,
                    foreground_alert="ff4a4a",
                ),
                # separator
                widget.Sep(padding=10),
                # Memory
                widget.Memory(format="󰍛{MemUsed: .0f}MB"),
                widget.Sep(padding=10),
                # Battery
                widget.Battery(
                    format="{char} {percent:2.0%} {hour:d}:{min:02d} {watt:.2f} W",
                    full_char="",
                    charge_char="",
                ),
                widget.Sep(padding=10),
                # Volume
                widget.Volume(fmt="Vol: {}"),
                widget.Sep(padding=10),
                # Network
                widget.Net(prefix="M", format="󰮏 {down}"),
                widget.Sep(padding=10),
                # Clock
                widget.Clock(format="  %d/%m - %a %I:%M"),
                widget.Spacer(length=30),
                # Keyboard layout
                widget.KeyboardLayout(
                    configured_keyboards=["us", "us colemak", "latam"],
                    display_map={
                        "us": "  us",
                        "us colemak": "  co",
                        "latam": "  la",
                    },
                ),
                widget.Spacer(length=30),
            ],
            30,
            # border_width=[0, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["000000", "000000", "ff00ff", "000000"]
            # Borders are magenta
        ),
    ),
]

# Drag floating layouts.
# mouse = [
#     Drag(
#         [mod],
#         "Button1",
#         lazy.window.set_position_floating(),
#         start=lazy.window.get_position(),
#     ),
#     Drag(
#         [mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()
#     ),
#     Click([mod], "Button2", lazy.window.bring_to_front()),
# ]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False

floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
