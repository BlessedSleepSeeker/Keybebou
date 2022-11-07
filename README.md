 # Project Keybébou

## Concept
A Custom Keyboard with no more than 12/15 keys, dedicated for quick actions

## Layout
```
789  
456  
123  
<>0  
```
- <> : 2 keys dedicated to mode change  
- 0 to 9 : programmable commands keys

## Modes

### 1. Number Mode
It's just a numpad

### 2. Destop Mode
A Mode for work & desktop usage  
Facilitate useful Windows shorcut  

- Ctrl Alt Suppr : Windows Menu
- Ctrl Shift Esc : Open Task Manager
- Windows Shift S : Capture Tool Expanded
- Media Key Triplet :
    - Pause/Play Media
    - Skip Media
    - Mute Self
- 

### 3. Aseprite Mode
- Tool Row
    - Select Paintbrush
    - Selection Tool
    - Bucket
- Layer Row
    - New Frame
    - New Layer
    - Onion Skin
- Export

## Hardware
- Gateron Clear Switch
- Raspberry Pico
    - Cheap (around 4€)
    - Has many pins
    - Programmable
- 12 keycaps

## Software
- Raspberry Pico : [CircuitPython](https://circuitpython.org/)
- GUI : ???

## Realisation

### Prototype
Use cable, Gateron Clear Switch & random keycaps

### 1.0
Custom PCB, Switch & Custom Keycaps

### Goals
1. Build a custom numpad. **<- I am here !**
2. Change the namepad to other custom commands like Ctrl Alt Suppr.
3. Implement the whole mode switching logic and the first mode (see [Modes](#modes)).
4. Add RGB LED to help with understanding which mode is on.
5. Develop a GUI where you will be able to program your mini keyboard as you desire.