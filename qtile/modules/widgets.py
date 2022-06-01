from libqtile import widget
from libqtile import qtile

colors = [
	      ["#282c34", "#282c34"], # panel background
          ["#3d3f4b", "#434758"], # background for current screen tab
          ["#ffffff", "#ffffff"], # font color for group names
          ["#ff5555", "#ff5555"], # border line color for current tab
          ["#74438f", "#74438f"], # border line color for 'other tabs' and color for 'odd widgets'
          ["#4f76c7", "#4f76c7"], # color for the 'even widgets'
          ["#e1acff", "#e1acff"], # window name
          ["#ecbbfb", "#ecbbfb"]  # backbround for inactive screens
] 


widget_defaults = dict(
    font='Cantarell',
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()
class MyVolume(widget.Volume):
    def _configure(self, qtile, bar):
        widget.Volume._configure(self, qtile, bar)
        self.volume = self.get_volume()
        if self.volume <= 0:
            self.text = '🔇'
        elif self.volume <= 15:
            self.text = '🔈'
        elif self.volume < 50:
            self.text = '🔉'
        else:
            self.text = '🔊'
        # drawing here crashes Wayland

    def _update_drawer(self, wob=False):
        if self.volume <= 0:
            self.text = '🔇'
        elif self.volume <= 15:
            self.text = '🔈'
        elif self.volume < 50:
            self.text = '🔉'
        else:
            self.text = '🔊'
        self.draw()

        if wob:
            with open(self.wob, 'a') as f:
                f.write(str(self.volume) + "\n")

volume = MyVolume(
    # theme_path="./speaker-filled-audio-tool.png",
    fontsize=18,
    font='Font Awesome 5 Free',
    foreground=colors[4],
    background='#2f343f',
    mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn("pavucontrol")}
)

date = widget.Clock(
    format='🕒 %Y-%m-%d %a %I:%M %p',
    background="#2f343f",
    foreground='#9bd689'
)

to_dark_division = widget.TextBox(
    text = '',
    padding = 0,
    fontsize = 28,
    foreground='#404552',
    background='#2f343f'
)

to_light_division = widget.TextBox(
    text = '',
    padding = 0,
    fontsize = 28,
    foreground='#2f343f'
)