# MACROPAD Hotkeys example: Consumer Control codes (media keys)

from adafruit_hid.consumer_control_code import ConsumerControlCode

app = {               # REQUIRED dict, must be named 'app'
    'name' : 'Media', # Application name
    'macros' : [      # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x000000, '', []),
        (0x31AAFF, 'Vol+', [[ConsumerControlCode.VOLUME_INCREMENT]]),
        (0xFF000A, 'Mute', [[ConsumerControlCode.MUTE]]),
        # 2nd row ----------
        (0xFFAA00, '<<', [[ConsumerControlCode.REWIND]]),
        (0x31AAFF, 'Vol-', [[ConsumerControlCode.VOLUME_DECREMENT]]),
        (0xFFAA00, '>>', [[ConsumerControlCode.FAST_FORWARD]]),
        # 3rd row ----------
        (0xE6E6FA, '|<', [[ConsumerControlCode.SCAN_PREVIOUS_TRACK]]),
        (0x0AFAA0, 'Play/Pause', [[ConsumerControlCode.PLAY_PAUSE]]),
        (0xE6E6FA, '>|', [[ConsumerControlCode.SCAN_NEXT_TRACK]]),
        # 4th row ----------
        (0x000000, '', []),
        (0x000000, '', []),
        (0x000000, '', []),
        # Encoder button ---
        (0x000000, '', [])
    ]
}
