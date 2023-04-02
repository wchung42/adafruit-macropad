from adafruit_macropad import MacroPad
from adafruit_led_animation.animation.rainbow import Rainbow
from adafruit_led_animation.animation.rainbowchase import RainbowChase
from adafruit_led_animation.animation.rainbowsparkle import RainbowSparkle
from adafruit_led_animation.animation.rainbowcomet import RainbowComet

def init():
    global macropad
    macropad = MacroPad()
    macropad.display.auto_refresh = False
    macropad.pixels.auto_write = False
    
    # Set default brightness
    macropad.pixels.brightness = 0.5

    # Initialize lighting modes
    global lighting_modes
    lighting_modes = ['MACROS', 'RAINBOW', 'CHASE', 'COMET', 'SPARKLE', 'LIGHTSOUT']
    global current_lighting_mode
    current_lighting_mode = 0

    global rainbow
    rainbow = Rainbow(macropad.pixels, speed=0.2, step=5, period=4)
    global rainbow_chase
    rainbow_chase = RainbowChase(macropad.pixels, speed=0.3, step=10, size=1, spacing=2)
    global rainbow_sparkle 
    rainbow_sparkle = RainbowSparkle(macropad.pixels, speed=0.1, num_sparkles=15)
    global rainbow_comet
    rainbow_comet = RainbowComet(macropad.pixels, speed=0.15, tail_length=8, bounce=True)