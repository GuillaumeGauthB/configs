from libqtile import bar
from .widgets import *
from libqtile.config import Screen
from modules.keys import terminal
import os

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
        wallpaper='/home/guillaumeg/git/sync/wallpapers/currentwp/currentImage0',
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
        wallpaper='/home/guillaumeg/git/sync/wallpapers/currentwp/currentImage2',
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
        wallpaper='/home/guillaumeg/git/sync/wallpapers/currentwp/currentImage1',
        wallpaper_mode='fill'
    ),
]