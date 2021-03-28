#imports
from flask import Flask, render_template, request
from pynput.keyboard import Key, Controller as KeyboardController
from pynput.mouse import Button, Controller as MouseController
from waitress import serve
from PIL import Image
import subprocess, os , webbrowser


app = Flask(__name__)
hosts_allow = []
kb = KeyboardController()
m = MouseController()
def url_open(url):
    firefox_path = 'C:/Program Files/Mozilla Firefox/firefox.exe %s'
    wb = webbrowser.get(firefox_path)
    wb.open(url,new=0,autoraise=True)

#Webserver Codes
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
        elif  request.form.get('ymusic'):
            url_open("https://music.youtube.com/watch?v=-mLpe7KUg9U&list=RDAMVM-mLpe7KUg9U")
            print("youtube music opened")
        elif  request.form.get('open_url'):
            wanted_url = request.form["wanted_url"]
            url_open(wanted_url)
            print("wanted url opened")
        elif  request.form.get('send_text'):
            wanted_text = request.form["wanted_text"]
            kb.type(wanted_text)
            print("text sended= " + wanted_text)
        elif  request.form.get('f'):
            kb.tap('f')
            print("f")
#Mause Controlss
# -----------------------------------------------        
        elif  request.form.get('m_move_-3_3'):
            m.move(-100, -101)
            print("m_move_-3_3")
        elif  request.form.get('m_move_ust3'):
            m.move(0, -100)
            print("m_move_ust3")
        elif  request.form.get('m_move_3_3'):
            m.move(100, -100)
            print("m_move_2_2")
        elif  request.form.get('m_move_-2_2'):
            m.move(-50, -50)
            print("m_move_-2_2")
        elif  request.form.get('m_move_ust2'):
            m.move(0, -50)
            print("m_move_ust2")
        elif  request.form.get('m_move_2_2'):
            m.move(50, -50)
            print("m_move_2_2")
        elif  request.form.get('m_move_-1_1'):
            m.move(-10, -10)
            print("m_move_-1_1")
        elif  request.form.get('m_move_ust1'):
            m.move(0, -10)
            print("m_move_ust1")
        elif  request.form.get('m_move_1_1'):
            m.move(10, -10)
            print("m_move_1_1")
        elif  request.form.get('m_move_sol3'):
            m.move(-100, 0)
            print("m_move_sol3")
        elif  request.form.get('m_move_sol2'):
            m.move(-50, 0)
            print("m_move_sol2")
        elif  request.form.get('m_move_sol1'):
            m.move(-10, 0)
            print("m_move_sol1")
        elif  request.form.get('m_move_sag3'):
            m.move(100, 0)
            print("m_move_sag3")
        elif  request.form.get('m_move_sag2'):
            m.move(50, 0)
            print("m_move_sag2")
        elif  request.form.get('m_move_sag1'):
            m.move(10, 0)
            print("m_move_sag1")
        elif  request.form.get('m_move_-1_-1'):
            m.move(-10, 10)
            print("m_move_-1_-1")
        elif  request.form.get('m_move_alt1'):
            m.move(0, 10)
            print("m_move_alt1")
        elif  request.form.get('m_move_1_-1'):
            m.move(10, 10)
            print("m_move_1_-1")
        elif  request.form.get('m_move_-2_-2'):
            m.move(-50, 50)
            print("m_move_-2_-2")
        elif  request.form.get('m_move_alt2'):
            m.move(0, 50)
            print("m_move_alt2")
        elif  request.form.get('m_move_2_-2'):
            m.move(50, 50)
            print("m_move_2_-2")
        elif  request.form.get('m_move_-3_-3'):
            m.move(-100, 100)
            print("m_move_-3_-3")
        elif  request.form.get('m_move_alt3'):
            m.move(0, 100)
            print("m_move_alt3")
        elif  request.form.get('m_move_3_-3'):
            m.move(100, 100)
            print("m_move_3_-3")
        elif  request.form.get('m_left_click'):
            m.click(Button.left)
            print("m_left_click")
        elif  request.form.get('m_right_click'):
            m.click(Button.right)
            print("m_right_click")
# ----------------------------------------------- 
        else:
            print("undefined")
            return render_template("main.html")
    elif request.method == 'GET':
            print("No Post Back Call")
    return render_template('main.html', name=name)

serve(app, host='0.0.0.0', port=5000, threads=1)#WAITRESS!
