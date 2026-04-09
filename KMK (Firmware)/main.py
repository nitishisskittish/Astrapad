import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.quickpin import QuickPin
from kmk.modules.encoder import Encoder
from kmk.modules.layers import Layers
from kmk.extensions.rgb import RGB, RGBModes
from kmk.extensions.display.volume import VolumeDisplay
from kmk.extensions.display import Display
from kmk.extensions.media_keys import MediaKeys

keyboard = KMKKeyboard()

keyboard.extensions.append(MediaKeys())

rgb = RGB(
    pixel_pin=board.D7,   # Adjust if needed
    num_pixels=16,
    mode=RGBModes.STATIC_COLOR,
    val_default=72
)
keyboard.extensions.append(rgb)

display_ext = Display(
    i2c_port=board.I2C(sda=board.D0, scl=board.D1),
    display=VolumeDisplay(),
)
keyboard.extensions.append(display_ext)

keyboard.modules.append(Layers())

keyboard.modules.append(
    Encoder(
        pins=((board.D4, board.D5, None),),  # D4/D5 are free for GPIO input
        on_clockwise=KC.VOLU,
        on_ccwise=KC.VOLD,
    )
)

keyboard.matrix = QuickPin(
    rows=(board.D2, board.D3),             # GP28, GP29
    cols=(board.D6, board.D7, board.D8, board.D9),  # GP0, GP1, GP2, GP4
)

keyboard.keymaps = [[
    KC.MPRV, KC.W, KC.MNXT, KC.MUTE,
    KC.A, KC.S, KC.D, KC.LGUI(KC.S)
]]

if __name__ == "__main__":
    keyboard.go()
