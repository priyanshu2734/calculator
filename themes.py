"""
themes.py
---------

Application themes.
"""

LIGHT = {

    "bg": "#F5F5F5",

    "fg": "#000000",

    "button_bg": "#FFFFFF",

    "button_fg": "#000000",

    "display_bg": "#FFFFFF",

    "display_fg": "#000000"

}

DARK = {

    "bg": "#1E1E1E",

    "fg": "#FFFFFF",

    "button_bg": "#2D2D2D",

    "button_fg": "#FFFFFF",

    "display_bg": "#111111",

    "display_fg": "#00FFAA"

}


class ThemeManager:

    def __init__(self):
        self.theme = LIGHT

    def light(self):
        self.theme = LIGHT

    def dark(self):
        self.theme = DARK

    def current(self):
        return self.theme