# MACROPAD Gaming hotkeys

from adafruit_hid.consumer_control_code import ConsumerControlCode  # For mediacontrols
from adafruit_hid.keycode import Keycode    # For keypresses

app = {                             # REQUIRED dict, must be named 'app'
    'name' : 'Gaming',            # Application name
    'macros' : [                    # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x000000, '', []),
        (0x000000, '', []),
        (0x000000, '', []),
        # 2nd row ----------
        (0x000000, '', []),
        (0xFFFF00, 'STFU', [Keycode.CONTROL, Keycode.SHIFT, 'm']),
        (0x000000, '', []),
        # 3rd row ----------
        (0x000000, '', []),
        (0xFF0000, 'GTFO', [Keycode.ALT, Keycode.F4]),
        (0x000000, '', []),
        # 4th row ----------
        (0x000000, '', []),
        (0x000000, '', []),
        (0x000000, '', []),
        # Encoder button ---
        (0x000000, '', [])
    ]
}
