# Project Keybébou

## Concept
A Custom Keyboard with 12 keys, dedicated for quick actions

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

### 1. Numpad
It's just a numpad

### 2. Destop
A Mode for work & desktop usage  
Facilitate useful Windows shorcut  

- Ctrl + Alt + Suppr : Windows Menu
- Ctrl + Shift + Esc : Open Task Manager
- Windows + Shift + S : Capture Tool Expanded
- Media Key Triplet :
    - Pause/Play Media
    - Skip Media
    - Mute Self
- Windows + ; : Open Emoji Tab

### 3. Aseprite
- Tool Row
    - Select Paintbrush
    - Selection Tool
    - Bucket
- Layer Row
    - New Frame
    - New Layer
    - Onion Skin
- Export

### 4. VSCode
*Insert useful vscode shortcut*
### 5. FGC
Motions inputs !

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

### Prototype Version
Use cable, Gateron Clear Switch & random keycaps. Implement goal 1 to 3.

### Release 1.0
Custom PCB, Switch & Custom Keycaps. Implement goal 1 to 6.

### Goals
1. Build a custom numpad. **<- I am here !**
2. Change the namepad to other custom commands like Ctrl Alt Suppr.
3. Implement the whole mode switching logic and the first mode (see [Modes](#modes)).
4. Implement Macros & Scripts. You press a button and 3 things launch, your chill playlist is playing.
5. Add RGB LED to help with understanding which mode is on.
6. Develop a GUI where you will be able to program your mini keyboard as you desire.