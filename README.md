
# Control My PC
 Its simple flask web server can be run from background and control from your pc from any LAN device with browser.İts tested on Windows PC and some features probably not available in other platforms.
 
 <p align="center">
  <img src="/static/screenshot1.jpg" width="350" title="Screenshot">
  <img src="/static/screenshot2.jpg" width="350" title="Screenshot2">
</p>


## Features

 1. Media Controls(Volume Up/Down/Mute, Playback Buttons)
 2. Arrow Keys
 3. Mouse Control
 4. Text type
 5. Url Open
 6. 'F' for Fullscreen
 7. Hotspot On/Off
 8. Youtube Music
 9. Pc Power Controls (Shotdown/Sleep/Restart)
 
## Usage
 You can use app with 2 ways one in Virtual Environment and other one is native usage.
 
 1. Virtual Environment
 
 -Open Powershell in app folder
 
 -Before activate you may need to write this code `set-executionpolicy remotesigned`
 
 -Activate Virtual Environment with `.\Scripts\activate`
 
 -Then `py server.pyw` it will start running access from 127.0.0.1:5000 or host ip adress from other device.
 
 2. Native

 -Install dependencies with `pip install -r requirements.txt`
 
 -Best way is match .pyw files with your pythonw.exe then double click file. 
 
 -But if you need to stop app you need to stop from task manager. İf you choose this way you can make this app start with boot. To do this make a scheduled task.

Note: For sleep button work you need to download PsTools and copy psshutdown.exe to C drive, and browser is default mozilla i didn't try with other ones if buttons dont work pls change code or install mozilla.

**Credits**

 - [PsTools](https://docs.microsoft.com/en-us/sysinternals/downloads/pstools)
 - [HotSpot On/Off Script From This Comment](https://stackoverflow.com/a/65912082)
 - [Handyman Icon](https://material.io/resources/icons/?style=baseline)
 - [Bootstrap](https://getbootstrap.com)

