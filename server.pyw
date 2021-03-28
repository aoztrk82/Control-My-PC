from flask import Flask, render_template, request
from pynput.keyboard import Key, Controller
from waitress import serve
import subprocess
import os

app = Flask(__name__)
hosts_allow = []
kb = Controller()

@app.route('/', methods=['GET', 'POST'])
def main(name=None):
    print(request.method)
    if request.method == 'POST':
        if request.form.get("vup"):
            print("volume increased")
            kb.tap(Key.media_volume_up)
        elif  request.form.get("vdown"):
            kb.tap(Key.media_volume_down)
            print("volume decreased")
        elif  request.form.get('mute'):
            kb.tap(Key.media_volume_mute)
            print("volume muted")
        elif  request.form.get('previus'):
            kb.tap(Key.media_previous)
            print("previus")
        elif  request.form.get('play'):
            kb.tap(Key.media_play_pause)
            print("play/pause")
        elif  request.form.get('next'):
            kb.tap(Key.media_next)
            print("next")
        elif  request.form.get('up'):
            kb.tap(Key.up)
            print("up")
        elif  request.form.get('down'):
            kb.tap(Key.down)
            print("down")
        elif  request.form.get('left'):
            kb.tap(Key.left)
            print("left")
        elif  request.form.get('right'):
            kb.tap(Key.right)
            print("right")
        elif  request.form.get('sdown'):
            os.system("shutdown /s /t 1")
            print("shutting down")
        elif  request.form.get('restart'):
            os.system("shutdown /r /t 1")
            print("restarting")
        elif  request.form.get('sleep'):
            os.system("C:\psshutdown.exe -d -t 0")
            print("sleeping")
        elif  request.form.get('hotspot'):
            subprocess.call([r'hotspot.bat'])
            print("hotspot on/off")
        else:
            print("undefined")
            return render_template("main.html")
    elif request.method == 'GET':
            print("No Post Back Call")
    return render_template('main.html', name=name)

serve(app, host='0.0.0.0', port=5000, threads=1) #WAITRESS!