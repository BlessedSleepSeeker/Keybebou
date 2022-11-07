# Project Keybébou

## Concept
A Custom Keyboard with 12 keys, dedicated for quick actions & shortcuts, with programmable modes and quick switch

## Layout
```
<>0
789
456
123  
```
- <> : 2 keys dedicated to mode change
- 0 to 9 : programmable commands keys

## Modes

### 1. Numpad
It's just a numpad

### 2. Destop
A Mode for work & desktop usage  
Facilitate useful Windows shorcut  

- `Ctrl + Alt + Suppr` : Windows Menu
- `Ctrl + Shift + Esc` : Open Task Manager
- `Windows + Shift + S` : Capture Tool Expanded
- Media Key Triplet :
    - Pause/Play Media
    - Skip Media
    - Mute Self
- `Windows + ;` : Open Emoji Tab
- 3 free keys

### 3. Aseprite
- Tool Row
    - Select Paintbrush
    - Selection Tool
    - Bucket
- Layer Row
    - New Frame
    - New Layer
    - Onion Skin
- Re Export File
- 3 frees keys

### 4. VSCode
*Insert useful vscode shortcut*

### 5. FGC
Motions inputs ! Individual Keypress won't do anything (except 1) and you will have to do the motion input + 0 to activate the shortcut linked to it.
- Down Back `1`
- Fireball `236`
- Dragon `623`
- Pot Buster `632146`
- Sonic Boom `[4]6`

## Hardware
- 1 Raspberry Pico
    - Cheap (around 4€)
    - Has many pins (26)
    - Easily Programmable
- 12 Gateron Clear Switch
    - They're cool and I ordered 150 so I'm going to use them
- 12 keycaps
    - Used keycaps from my old keyboard


## Software
- Raspberry Pico : [CircuitPython](https://circuitpython.org/)
- GUI : ???

## Realisation

### Goals
1. Build a custom numpad. **<- I am Here**
2. Change the namepad to other custom commands like Ctrl Alt Suppr.
3. Implement the whole mode switching logic and the first mode (see [Modes](#modes)).
4. Implement Macros & Scripts. Example : You press a button and 3 things launch, your chill playlist is playing and your notifications are off.
5. Add RGB LED to help with understanding which mode is on.
6. Develop a GUI where you will be able to program your mini keyboard as you desire.

### Prototype Version
Use cables, Gateron Clear Switch & random keycaps. 3D Printed Case. Implement goal 1 & 2.

### Release 1.0
Use cables, Gateron Clear Switch & random keycaps. 3D Printed Case. Implement goal 1 to 4.

### Release 2.0
Use custom PCB, Gateron Clear Switch & custom keycaps. Quality Case. Implement goal 1 to 6. Final product.

## Production History

### October 2022
- Got the idea
### November 7 2022
- Started Repository