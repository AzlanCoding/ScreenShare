# ScreenShare
### A simple browser to browser screen sharing application between 2 devices.
ScreenShare is a simple screen sharing application between 2 desktop browsers through using WebRTC. It was created as a prototype for a component in the Integrated Classroom Hub (another prototype that has not been released yet).
## Installation
You can fork and run this project on [Repl.it](https://repl.it) through this [link](https://screenshare.azlancoding.repl.co).<br>
Alternatively, you can use the commands below to clone this repo to run it locally from your computer.
```
git clone https://github.com/AzlanCoding/ScreenShare
cd ScreenShare
```
After cloning, you must:
1. Ensure TCP Port 443 and all UDP Ports are allowed to pass through your devices firewall if you are planning to share your screen outside the laptop. 
2. Turn on the device Wifi Hotspot if you are planning to share your screen outside the laptop.
3. Modify `main.py`. Change
 ```python
 app.run(host='0.0.0.0', port=81)
 ```
 in line 115 to 
 ```
 app.run(host='192.168.137.1', port=443, ssl_context='adhoc')
 ```
 where `192.168.137.1` is the IP address where your hotspot is running on.
 <br>
 Once completed, you can run the server using the command
 ```
 python3 main.py
 ```
 ## Note
 ScreenShare requires HTTPS to run, therefore the ad-hoc server is required to allow ScreenShare to run. Without HTTPS [`getDisplayMedia()`](https://developer.mozilla.org/en-US/docs/Web/API/MediaDevices/getDisplayMedia) may not work.
 