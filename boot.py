import board
import digitalio
import storage

key = digitalio.DigitalInOut(board.KEY1)
key.direction = digitalio.Direction.INPUT
key.pull = digitalio.Pull.UP

if key.value:
    storage.disable_usb_drive()

key.deinit()