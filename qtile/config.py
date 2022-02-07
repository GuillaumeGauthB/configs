# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from typing import List  # noqa: F401

from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

mod = "mod4"
terminal = guess_terminal()

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod, "shift"], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
    Key([mod, "shift"], "r", lazy.qtilecmd(), desc="Spawn a command using Qtile widget"),

    # Personal Keybindings
    Key([mod], "b", lazy.spawn("brave"), desc="Spawn brave"),
    Key([mod, "shift"], "b", lazy.spawn("brave --kiosk"), desc="Spawn brave in kiosk mode until i get alternative"),
    Key([mod], "q", lazy.spawn("alacritty --command  vim /home/guillaumeg/.config/qtile/config.py"), desc="Spawn qtile config"),
    Key([mod], "a", lazy.spawn("alacritty --command  vim /home/guillaumeg/.config/alacritty/alacritty.yml"), desc="Spawn alacritty config"),
    Key([mod], "space", lazy.spawn("spectacle"), desc="Take a screenshot"),
    Key([mod], "p", lazy.spawn("alacritty --command /home/guillaumeg/scripts/useful/wallpaper-qtile.sh"), desc="Change wallpapers qtile"),
    Key([mod], "s", lazy.spawn("surf /home/guillaumeg/git/start-page/html-test/html/homepage.html"), desc="Spawn surf homepage"),
    Key([mod, "control"], "a", lazy.spawn("alacritty --command  /home/guillaumeg/git/ani-cli/./ani-cli"), desc="Spawn ani-cli"),
    Key([mod], "f", lazy.widget["keyboardlayout"].next_keyboard(), desc="Next keyboard layout."),
]

groups = [Group(i) for i in "123456789"]

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
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )

layout_theme = {"border_width": 2,
                "margin": 10,
                "border_focus": "elacff",
                "border_normal": "1D2330"
                
                }

layouts = [
    layout.Columns(
    #border_focus_stack=["#d75f5f", "#8f3d3d"], border_width=4
    **layout_theme
    ),
    layout.Max(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
     layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
     layout.TreeTab(),
     layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font="sans",
    fontsize=12,
    padding=5,
    #background-color: 0xffffff,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.CurrentLayout(),
                widget.GroupBox(),
                widget.Prompt(
                background="#ffffff",
                cursor_color="#000000",
                foreground="#000000",
                padding=5
                ),
                widget.TaskList(
                    #background="#141414",
                    max_title_widt=150,
                ),
                #widget.WindowName(),
                #extension.Dmenu(),
                #widget.Backlight(),
                #widget.KeyBoardKbdd(),
                widget.KeyboardLayout(
                    configured_keyboards=["us", "ca,fr"],
                    display_map={'us':'us', 'ca,fr':'fr'},
                ),
                widget.Chord(
                    chords_colors={
                        "launch": ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                #widget.Backlight(),
                #widget.Bluetooth(),
                widget.CheckUpdates(
                    color_have_updates="#ff0000",
                ),
                widget.Sep(),
                widget.Volume(
                    volume_app="pulse",
                    foreground="#E7625F"
                ),
                widget.Sep(),
                widget.OpenWeather(
                    app_key='c6844051286fa2eda562a5fe7719ae06a',
                    cityid='6077243',
                    #update_interval=15,
                    metric=True
                    #location='Montreal',
                    #url='http://api.openweathermap.org/data/2.5/weather?id=6077243&units=metric&appid=c6844051286fa2eda562a5fe7719ae06a'
                ),
                widget.Net(
                    use_bits=True,
                    foreground="#d75f5f"
                ),
                #widget.TextBox("default config", name="default"),
                #widget.TextBox("Press &lt;M-r&gt; to spawn", foreground="#d75f5f"),
                widget.Systray(),
                widget.Clock(format="%Y-%m-%d %a %I:%M %p"),
                widget.QuickExit(foreground="#8155BA"),
            ],
            25,
            #background=["#000000", "#191919"],
            background="#2e3440",
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["2e3440", "2e3440", "2e3440", "2e3440"],  # Borders are magenta
            # drop_shadow=["5", "5", "5", "#2e3440"]
        ),
        #background=["#000000", "#191919"],
        wallpaper='/home/guillaumeg/Pictures/currentwp/currentImage0',
        wallpaper_mode='fill'
    ),
    Screen(
        top=bar.Bar(
            [
                widget.CurrentLayout(),
                widget.GroupBox(),
                widget.Prompt(),
                #widget.WindowName(),
                widget.TaskList(
                    #background="#141414",
                    max_title_widt=150,
                ),
                widget.Chord(
                    chords_colors={
                        "launch": ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                widget.Notify(),
                widget.Sep(),
                widget.Volume(
                    volume_app="pulse",
                    foreground="#E7625F"
                ),
                widget.Sep(),
                #widget.TextBox("default config", name="default"),
                #widget.TextBox("Press &lt;M-r&gt; to spawn", foreground="#d75f5f"),
                widget.Systray(),
                widget.Clock(format="%Y-%m-%d %a %I:%M %p"),
                widget.QuickExit(),
            ],
            25,
            #background=["#000000", "#191919"],
            background="#2e3440",
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["2e3440", "2e3440", "2e3440", "2e3440"]
        ),
        wallpaper='/home/guillaumeg/Pictures/currentwp/currentImage1',
        wallpaper_mode='fill'
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
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

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
