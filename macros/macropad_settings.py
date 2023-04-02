from adafruit_macropad import MacroPad

# -----------------------------
# Button functions
# -----------------------------
def increaseBrightness(macropad: MacroPad = None):
    if macropad.pixels.brightness >= 1.0:
        return
    if 1.0 - macropad.pixels.brightness < 0.05:
        macropad.pixels.brightness += 1.0 - macropad.pixels.brightness
        return
    macropad.pixels.brightness += 0.05


def decreaseBrightness(macropad: MacroPad = None):
    if macropad.pixels.brightness <= 0.0:
        return
    if macropad.pixels.brightness < 0.05:
        macropad.pixels.brightness = 0.0
        return
    macropad.pixels.brightness -= 0.05


def setModeMacros(macropad: MacroPad) -> int:
    return 0 # MACROS


def setModeRainbow(macropad: MacroPad) -> int:
    return 1 # RAINBOW


def setModeChase(macropad: MacroPad) -> int:
    return 2 # CHASE


def setModeComet(macropad: MacroPad) -> int:
    return 3 # COMET


def setModeSparkle(macropad: MacroPad) -> int:
    return 4 # SPARKLE


def setModeLightsout(macropad: MacroPad) -> int:
    return 5 # LIGHTSOUT


app = {                             # REQUIRED dict, must be named 'app'
    'name' : 'Macropad Settings',   # Application name
    'macros' : [                    # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0xFFFFFF, 'Bright+', [increaseBrightness]),
        (0x000000, '', []),
        (0xFFFFFF, 'Rainbow', [setModeRainbow]),
        # 2nd row ----------
        (0xFFFFFF, 'Bright-', [decreaseBrightness]),
        (0x000000, '', []),
        (0xFFFFFF, 'Chase', [setModeChase]),
        # 3rd row ----------
        (0x000000, '', []),
        (0xFFFFFF, 'Macros', [setModeMacros]),
        (0xFFFFFF, 'Comet', [setModeComet]),
        # 4th row ----------
        (0x000000, '', []),
        (0xFFFFFF, 'Dark', [setModeLightsout]),
        (0xFFFFFF, 'Sparkle', [setModeSparkle]),
        # Encoder button ---
        (0x000000, '', [])
    ]
}

