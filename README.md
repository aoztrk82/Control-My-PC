
# Control My PC
 Its simple flask web server can be run from background and control from your pc from any LAN device with browser.İts tested on Windows PC and some features probably not available in other platforms.
 
![Screenshot](/static/screenshot1.png)

## Features

 1. Media Controls(Volume Up/Down/Mute, Playback Buttons)
 2. Arrow Keys
 3. Hotspot On/Off
 4. Youtube Music
 5. Pc Power Controls (Shotdown/Sleep/Restart)
 
## Usage
 You can use app with 2 ways one in Virtual Environment and other one is native usage.
 
 1. Virtual Environment
 Open Powershell in app folder
 Activate Virtual Environment with `.\Scripts\activate`
 Then `py server.pyw` it will start running access from 127.0.0.1:5000 or host ip adress from other device.
 2. Native
 Install dependencies with `pip install -r requirements.txt`
 Best way is match .pyw files with your pythonw.exe then double click file. 
 But if you need to stop app you need to stop from task manager. İf you choose this way you can make this app start with boot. To do this make a scheduled task.

 
**Credits**

 - [PsTools](https://docs.microsoft.com/en-us/sysinternals/downloads/pstools)
 - [HotSpot On/Off Script From This Comment](https://stackoverflow.com/a/65912082)
 - [Handyman Icon](https://material.io/resources/icons/?style=baseline)

