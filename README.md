## **Astrapad**
---
A 7 key macropad with a rotary encoder, OLED screen, and 16 WS2812B LED’s. Currently runs on KMK firmware

### **Features**
---
- Two Piece 3D Printable Case
- 128x32 OLED Display
- EC11 Rotary encoder
- 16 WS2812B RGB LEDs, probably waaayyy too much, but the more the merrier I guess
- 7 Keys

### **CAD Model**
---
The case is held together by 4 M3 Bolts and heatset inserts, 1 in each corner. The bottom half of the case has a built in tilt. Originally I designed this with see-through plastic “windows” in mind, but as of now those windows have been replaced with direct holes looking into the PCB. Maybe I’ll add them later.

<img src=Images/Case_Image.png alt="Case" width="500"/>

### **PCB**
---
I made my PCB in KiCad, and I got my silkscreen arts from the [Zenless Zone Zero Fandom Sticker Page](https://zenless-zone-zero.fandom.com/wiki/Stickers)

- Schematic:

  <img src=Images/Schematic.png alt="Schematic" width="500"/>
- Schematic:

  <img src=Images/PCB.png alt="PCB" width="500"/>
- My favorite part of the whole project tbh, made me feel very smart. Also if your interested the numbers at the very bottom are binary, although it doesn’t spell out anything that interesting

### **Firmware**
---
Currently Astrapad runs on KMK, but I plan on switching to QMK later because I want to add [VIA](https://caniusevia.com/) support
- The rotary encoder changes the volume, and you can tap it to toggle mute
- The top left and top right keys skips forward or backward respectively in the playback queue
- The top middle button and bottom 3 buttons act as WASD keys, with the top middle button being the W Key
- The bottom right button is currently mapped to a custom shortcut I have on my computer that opens Spotify
- I have a list of features I want to add commented in the KMK main.py file if you're interested in that
### **BOM**
---
- 1x Seeed XIAO RP2040
- 1x 0.91 inch OLED displays 
- 1x EC11 rotary encoders
- 1x Case (2 3D printed parts)
- 1x 3D printed EC11 (Rotary Encoder) Knob
- 4x M3x5x4 Heatset inserts
- 4x M3x16mm screws
- 7x Cherry MX Switches
- 7x DSA keycaps
- 8x Through-hole 1N4148 Diodes
- 16x SK6812 MINI-E LEDs

### **Extra Stuff**
---
The example I’m basing this README off of had this section, so I’m adding it too. 
Thanks a lot to the Blueprint Hackclub slack, I probably wouldn’t have finished this project without their help.
Ummm yeah, that’s it I guess. 
