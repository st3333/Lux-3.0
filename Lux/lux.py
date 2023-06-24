import config, webbrowser, os, random, time
from stt import Lux as lux
from tts import listen
from fuzzywuzzy import fuzz
from datetime import datetime
from num2words import num2words
import pyautogui as pg
import openai

print(f"{config.NAME} (v{config.VERSION}) готов к работе...")
lux("Здравствуйте")

sounds = ['запрос выполнен', 'будет сделано', 'как пожелайте']

def response(voice: str):
    print(voice)
    if voice.startswith(config.ALIAS):
        cmd=recognize_cmd(filter_cmd(voice))

        if cmd['cmd'] not in config.CMD_LIST.keys():
            lux("запрос не распознан")
        else:
            execute_cmd(cmd['cmd'])

def filter_cmd(raw_voice: str):
    cmd = raw_voice

    for i in config.ALIAS:
        cmd = cmd.replace(i,'').strip()

    for i in config.TBR:
        cmd = cmd.replace(i,'').strip()
    return cmd

def recognize_cmd(cmd: str):
    rc ={'cmd': '', 'percent': 0}

    for s,a in config.CMD_LIST.items():

        for i in a:
            vrt = fuzz.ratio(cmd, i)
            if vrt > rc['percent']:
                rc['cmd']=s
                rc['percent'] = vrt
    return rc

def execute_cmd(cmd: str):
    ans = lux(random.choice(sounds))
    if cmd == 'ctime':
        now = datetime.now()
        lux("Сейчас: " + num2words(now.hour, lang='ru') + num2words(now.minute, lang='ru'))
    elif cmd == 'viber':
        ans
        pg.hotkey('Winleft')
        pg.write('viber', 0)
        pg.hotkey('enter')
    elif cmd == 'joke':
        jokes = ['Почти каждый программист имеет своего верного компаньона – чашку кофе, которая служит источником бодрости и вдохновения', 'Если программист смотрит на экран с непониманием, это значит, что код находится в активной фазе "самообучения"', 'Программисты – это мастера в создании невидимых мостов между человеческими мыслями и компьютерным миром', 'Для программистов проблемы – это как головоломки, которые они не могут не решить. Они продолжают биться над ними, пока не найдут идеальное решение', 'Программисты – настоящие ловцы багов. Они ищут их, словно охотники, и радуются, когда могут их поймать и исправить', 'Воображение программиста – это его кисть, а код – его полотно. С его помощью они создают произведения искусства в виде программ', 'Программисты умеют читать и писать на языках, которые не существуют в реальном мире – языках программирования', 'Если программист говорит, что он "просто что-то проверяет" или "делает небольшую правку", скорее всего, он пропадет в своем кодовом лабиринте на несколько часов', 'Для программиста нет ничего более удовлетворительного, чем видеть, как его код работает безупречно и решает реальные проблемы людей', 'Программисты – это люди, которые могут создать что-то из ничего. Их творчество – это код, который может изменить мир в лучшую сторону']

        lux(random.choice(jokes))

    elif cmd == 'youtube':
        ans
        webbrowser.open('http://www.youtube.com/')
    elif cmd == 'language':
        ans
        pg.hotkey('shift', 'alt')
    elif cmd == 'poweroff':
        ans
        lux('досвидания сэр')
        os.system('shutdown /s /t 0')
    elif cmd == 'restart':
        ans
        lux('Увидимся')
        os.system('shutdown /r /t 0')
    elif cmd == 'pause_and_continue':
        ans
        pg.hotkey('space')
    elif cmd == 'fullscreen':
        ans
        pg.hotkey('f')
    

listen(response)