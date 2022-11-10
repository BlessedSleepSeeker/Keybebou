# Project Keybébou

- [Project Keybébou](#project-keybébou)
  - [Concept](#concept)
  - [Layout](#layout)
    - [Physical Layout](#physical-layout)
    - [Design Philosophy](#design-philosophy)
  - [Modes](#modes)
    - [Mode Switching](#mode-switching)
    - [0.1 Switch Mode](#01-switch-mode)
    - [0.2 Debug](#02-debug)
    - [1. Extended Numpad](#1-extended-numpad)
    - [2. Destop](#2-destop)
    - [3. Aseprite](#3-aseprite)
    - [4. VSCode](#4-vscode)
    - [5. FGC](#5-fgc)
  - [Hardware](#hardware)
  - [Software Tools](#software-tools)
  - [Realisation](#realisation)
    - [Goals](#goals)
  - [Production History](#production-history)
    - [October 2022](#october-2022)
    - [November 7 2022](#november-7-2022)
    - [November 10 2022](#november-10-2022)

## Concept

A Custom Keyboard with 12 keys, dedicated for quick actions & shortcuts, with programmable modes and quick switch between them.

## Layout

### Physical Layout

```text
789
456
123
ULM  
```

- `U` (Upper) and `L` (Lower) : 2 modifiers keys changing the key input
- `M` : Mode Change Key/Wildcard Key
- `1` to `9` : programmable keys

This is the most optimal layout for key diversity giving us 36 (9 base + 9 modX + 9 modY + 9 modX modY) different keys per mode, with 36 modes, for a total of 1296 individual programmable keys.

For the rest of the document, `^` means that the key is pressed.  
*Example : `U^` mean that the **Upper** modifier key is pressed.*

### Design Philosophy

The physical layout and the mode layout have been designed with a few guidelines in mind :

- > We are an addon
  - The goal is not to supplant but to enhance the utilisation of a regular keyboard.
  - I'm using a 60% Keyboard so I'm a little biased on what is missing/needed. Everything should be customisable in the end (it doesn't even matter :musical_note:), so you will be able to configure your own modes anyway.
- > Allow for maximum possibility in the lowest amount of physical key while keeping it simple enough.
  - This is why we don't have more modifier even though we could have gone for 3.
- > The more a key is going to be used, the less modifier it require.
  - Nobody would want to press 3 buttons to get a single character displayed.
- > The more a key has impact on the system, the more modifier it require.
  - You don't want to press your "kill X, Y and Z" script by mistake.
- > Make 3 and more keys combination shortcuts available in only one or 2 key press.
  - This is why on some modes we don't have any bindings to double modifier.
- > Everything should be open-source and customisable easily.

## Modes

### Mode Switching

Press the mode switching combination (`U + L + M`, press `M` while both modifier are held down) to enter the "switch mode" then press a number between 0 & 36

### 0.1 Switch Mode

*No Modifiers*

```text
7 8 9
4 5 6
1 2 3
U L 0
```

***Upper** Modifier*

```text
16 17 18
13 14 15
10 11 12
U^ L  M
```

***Lower** Modifier*

```text
25 26 27
22 23 24
19 20 21
U  L^ M
```

***Upper** and **Lower** Modifier*

```text
34 35 36
31 32 33
28 29 30
U^ L^ M
```

### 0.2 Debug

Print Output to a file on the keyboard raspberry.

### 1. Extended Numpad

It's a numpad with a little bit more symbols cause we had free space.  
The double modifier row (`U^ L^`) is fully empty (for the moment). Most of these symbols are already available on the number row in only 1 modifier (either `Ctrl` or `Alt Gr`) on a regular keyboard and adding them here would serve no purpose than anything else.  
If you have any suggestions regarding this spot, do not hesitate !

*No Modifiers*

```text
7 8 9
4 5 6
1 2 3
U L 0
```

***Upper** Modifier*

```text
^  %  #
/  .  ²
+  -  *
U^ L  Enter
```

***Lower** Modifier*  

```text
$  €  £
<  >  °
(  )  =
U  L^ Enter
```

***Upper** and **Lower** Modifier*  

```text
Empty Empty Empty 
Empty Empty Empty 
Empty Empty Empty 
U^ L^ M
```

### 2. Destop

A Mode for regular work & desktop usage  
Facilitate useful Windows & Office shorcut  
*Raw ideas only for the moment*

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

My reflexion here was simply "fuck my keyboard is too big i need only lil' keyb for aseprite usage"
*Raw ideas only for the moment*

- Tool Row
  - Select Paintbrush
  - Selection Tool
  - Bucket
- Layer Row
  - New Frame
  - New Layer
  - Onion Skin
- Save
- Re Export File

### 4. VSCode

*Insert useful vscode shortcut*

### 5. FGC

*Raw ideas only for the moment*
*Mostly a funny meme*

Motions inputs ! Individual Keypress won't do anything (except 1) and you will have to do the motion input + a modifier to activate the shortcut linked to it.

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

## Software Tools

- Raspberry Pico : [CircuitPython](https://circuitpython.org/)
- GUI : ???

## Realisation

### Goals

1. [ ] Build a custom numpad.
2. [ ] Change the namepad to other custom commands like Ctrl Alt Suppr.
3. [ ] Implement the modifier logic.
4. [ ] Implement the whole mode switching logic and the first mode (see [Modes](#modes)).
5. [ ] Get a template script for mode development.
6. [ ] Implement Macros & Scripts. Example : You press a button and 3 things launch, your chill playlist is playing and your notifications are off.
7. [ ] Develop a GUI where you will be able to program your mini keyboard as you desire.
8. [ ] Add RGB LED(s) to help with understanding which mode is on.

## Production History

### October 2022

- Got the idea

### November 7 2022

- Started Repository

### November 10 2022

- Readme Tweaks :
  - Got the modifier idea and modified layout & goals accordingly
  - Removed the Prototype & Release part. Will appear again at relevant milestone
  - Mode Switching part added to the readme
  - Added Design Philosophy
  - Added Table of Content
