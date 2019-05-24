![logo of the cancer project](https://raw.githubusercontent.com/areee/cAnceR/master/cAnceR-icon.png)

# cAnceR

> Showing cancer types visualized by augmented reality

Information Visualization & Interactive techniques course project work at Tampere University, Finland

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

You need these things to install our software:

- Meta 2 – Augmented Reality Glasses
- A very powerful gaming computer (see [Minimum System Requirements](#minimum-system-requirements))
- The latest Meta 2 SDK
- Unity development platform, version 2017.3.0f3 (e.g. via Unity Hub)
- _(Optional)_ Visual Studio 2017 or newer – for coding scripts

### Minimum System Requirements

- OS: Windows 10 (64 bit)
- Processor: Intel Core i7 6700 Processor or AMD FX 9590, or better
- Memory: 16 GB RAM DDR4 or more
- Graphics: NVIDIA GeForce GTX 1050 TI or AMD Radeon RX 480 or better
  - Please Note: AMD is only supported in Extended Mode, not in Direct Mode
- Free Hard Drive space: 10 GB
- Video Output: 1x HDMI 1.4b port
- USB: 1x USB 3.0 port

### Installing

- Download Meta 2 SDK from [Metavision's website](https://www.metavision.com/)
- Download this repository as [ZIP](https://github.com/areee/cAnceR/archive/master.zip)
- Extract the zip file and open ``MetacAnceR`` project folder in Unity
- Plug in Meta glasses and wait until the fan is silencing
- Press the play button to run the AR environment
- Wait until the Meta glasses have initialized themselves and the mapping is ready (mapping may be run twice in the beginning)

## How to use it

![a typical view of the cancer environment](https://raw.githubusercontent.com/areee/cAnceR/master/cAnceR-environment.png)
_Image 1: A view of the cAnceR environment when all body parts are selected and all graphs are visible._

### Hand interactions

Put your hand on the near side of the mainikin and angle your wrist so that the back of your hand is parallel to your face. Now put your hand up to the edge of the manikin and observe the visual change to the status indicator floating on the back of your hand. Finally, gently make a closed fist. An audio cue will play to indicate a successful grab.

**Two-handed hand gestures**
- The manikin can be turned
- Its size can be changed

**One-handed hand gestures**
- The manikin can be moved
- Its body part can be selected by pointing the necessary body part
  - The graph of the desired body part can be seen and hidden

### Viewing objects with Meta glasses
- The person using the glasses can move closer to the manikin and the graphs 
while these objects remain stationary

### Keyboard of the computer
- The visualization camera can be moved with the arrow keys (along the x and y 
axes), to zoom in and out of the objects with the A and S keys (along the z 
axis), and to rotate the view with the Q and W keys

### Mouse of the computer
- Bar chart points can be clicked and seen as a scatter plot for age variance 
associated with selected cancer type

## What is included in this repository

- ``MetacAnceR`` – Unity project folder
- ``cAnceRVisuals`` – Python files for generating Bokeh visualizations
- ``docs`` – published HTML visualizations

## Team 

| <a href="https://github.com/areee" target="_blank">**Arttu Ylhävuori**</a>|  <a href="https://github.com/hhanna12" target="_blank">**Hanna-Riikka Rantamaa**</a>|
|:-------------:|:-------------:|
| [![Arttu's avatar](https://avatars2.githubusercontent.com/u/10089872?v=4&s=350)](https://github.com/areee)    | [![Hanna's avatar](https://avatars2.githubusercontent.com/u/32436932?s=200&v=4)](https://github.com/hhanna12) |

## License
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE.md](LICENSE.md) file for details
