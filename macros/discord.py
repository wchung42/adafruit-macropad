# MACROPAD Discord hotkeys

from adafruit_hid.keycode import Keycode

app = {               # REQUIRED dict, must be named 'app'
    'name' : 'Discord', # Application name
    'macros' : [      # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0xFFAA00, 'Mute', [Keycode.CONTROL, Keycode.SHIFT, 'm']),
        (0x000000, '', []),
        (0xFF0000, 'Deafen', [Keycode.CONTROL, Keycode.SHIFT, 'd']),
        # 2nd row ----------
        (0x00FF00, 'Answer', [Keycode.CONTROL, Keycode.ENTER]),
        (0x000000, '', []),
        (0xFF0000, 'Decline', [Keycode.ESCAPE]),
        # 3rd row ----------
        (0xE6E6FA, 'Delete', [Keycode.UP_ARROW, 0.05, Keycode.CONTROL, 'a', 0.05, Keycode.BACKSPACE, Keycode.ENTER, 0.5, Keycode.ENTER]),
        (0x000000, '', []),
        (0x0AFAA0, 'Explorer', [Keycode.CONTROL, 'k']),
        # 4th row ----------
        (0x000000, '', []),
        (0x000000, '', []),
        (0x000000, '', []),
        # Encoder button ---
        (0x000000, '', [])
    ]
}
