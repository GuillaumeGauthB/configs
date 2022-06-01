from libqtile.lazy import lazy
from libqtile.config import Key

mod = "mod4"
terminal = "alacritty"

keys = [
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    # Key([mod],
    #     "space",
    #     lazy.layout.next(),
    #     desc="Move window focus to other window"),

    Key([mod], "r", lazy.spawn("rofi -show combi"), desc="spawn rofi"),

    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"],
        "h",
        lazy.layout.shuffle_left(),
        desc="Move window to the left"),
    Key([mod, "shift"],
        "l",
        lazy.layout.shuffle_right(),
        desc="Move window to the right"),
    Key([mod, "shift"],
        "j",
        lazy.layout.shuffle_down(),
        desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),

    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"],
        "h",
        lazy.layout.grow_left(),
        # lazy.layout.shrink(),
        # lazy.layout.decrease_ratio(),
        # lazy.layout.add(),
        desc="Grow window to the left"),
    Key([mod, "control"],
        "l",
        lazy.layout.grow_right(),
        # lazy.layout.grow(),
        # lazy.layout.increase_ratio(),
        # lazy.layout.delete(),
        desc="Grow window to the right"),
    Key([mod, "control"],
        "j",
        lazy.layout.grow_down(),
        # lazy.layout.shrink(),
        # lazy.layout.increase_nmaster(),
        # lazy.layout.delete(),
        desc="Grow window down"),
    Key([mod, "control"], 
        "k", 
        lazy.layout.grow_up(),
        # lazy.layout.grow(),
        # lazy.layout.decrease_nmaster(),
        # lazy.layout.delete(), 
        desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack"),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "shift", "control"], "h", lazy.layout.swap_column_left()),
    Key([mod, "shift", "control"], "l", lazy.layout.swap_column_right()),
    Key([mod, "shift"], "space", lazy.layout.flip()),
    Key([mod, "control"], "r", lazy.restart(), desc="Restart Qtile"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod, "shift"],
        "r",
        lazy.spawncmd(),
        desc="Spawn a command using a prompt widget"),
    # Key([], "XF86AudioRaiseVolume",lazy.spawn("amixer set Master 3%+")),
    # Key([], "XF86AudioLowerVolume",lazy.spawn("amixer set Master 3%-")),
    # Key([], "XF86AudioMute",lazy.spawn("amixer set Master toggle")),

    # Personal Keybinds
    Key([mod], "b", lazy.spawn("brave"), desc="Spawn brave"),
    # Key([mod, "shift"], "b", lazy.spawn("brave --kiosk"), desc="Spawn brave in kiosk mode until i get alternative"),
    Key([mod], "q", lazy.spawn("code /home/guillaumeg/.config/qtile"), desc="Spawn qtile config"),
    Key([mod], "a", lazy.spawn("code /home/guillaumeg/.config/alacritty/alacritty.yml"), desc="Spawn alacritty config"),
    Key([mod], "space", lazy.spawn("flameshot gui"), desc="Take a screenshot"),
    Key([mod], "p", lazy.spawn("alacritty --command /home/guillaumeg/scripts/useful/wallpaper-qtile.sh"), desc="Change wallpapers qtile"),
    # Key([mod], "s", lazy.spawn("surf /home/guillaumeg/git/start-page/html-test/html/homepage.html"), desc="Spawn surf homepage"),
    Key([mod, "control"], "a", lazy.spawn("alacritty --command  /home/guillaumeg/git/ani-cli/./ani-cli"), desc="Spawn ani-cli"),
    Key([mod], "f", lazy.widget["keyboardlayout"].next_keyboard(), desc="Next keyboard layout."),
]
