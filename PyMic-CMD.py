import os
from os import listdir
from os.path import isfile, join
from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'


version = 1

import urllib.request, json


try:
    from pygame._sdl2 import get_num_audio_devices, get_audio_device_name
    from pygame import mixer
    import gtts

except Exception as e:
    print("<=============== Installing Packages ===============>")
    os.system("pip install pygame")
    os.system("pip install gtts")
    

from pygame._sdl2 import get_num_audio_devices, get_audio_device_name
from pygame import mixer
mixer.init()

print("=="*20)
print("type in /help for more info")
print("")

jsongithub_link = "https://blaze005.github.io/items.json"
with urllib.request.urlopen(jsongithub_link) as url: 
   json_data = json.loads(url.read().decode())
   message = json_data["message"]
   vr = json_data["version"]
   ancmnts = json_data["updates"]

if vr == version:
    print(f"You are on version: {version}, Server Version: {vr}")
    print("You are up to date")

else:
    print(f"You are behind please update to version: {vr}")
    input("Please press enter to agnoledge this.")


print("")
print(f"Daily Message: {message}")
print(f"Creators Corner: {ancmnts}")
print("")
print("=="*20)



def start():
    
    dir = 'sound/'
    for x in os.listdir(dir):
        os.remove(os.path.join(dir, x))

    global user
    global num
    global mic
    num = 0
    mic = 0

    try:
        global f
        f =  open('cogs/mic.txt', 'r')
        mic = f.read()
        
        
    except Exception as e:
        print(f"{e} // No mic is chosen")
        print("list of mics:")
        print(f"==="*20)
        a = [get_audio_device_name(x, 0).decode() for x in range(get_num_audio_devices(0))]
        print(* a, sep = "\n")
        print(f"==="*20)
       
        f =  open('cogs/mic.txt', 'w')
        user = input("please choose a mic: ")
        f.write(user)
        mic = user


    print("--"*20)
    print(f"Using Device: {mic}")
    
    while True:
        try:
            from gtts import gTTS
            print("--"*20)
            f = input("Convert text and say: ")

            if f == "/play":
                user = input("choose a file to play from effects: ")
                mixer.quit()
                mixer.init(devicename=mic)
                mixer.music.load(f"effects/{user}.mp3")
                mixer.music.play()
                start()

            elif f == "/config mic":
                print("list of mics:")
                print(f"==="*20)
                a = [get_audio_device_name(x, 0).decode() for x in range(get_num_audio_devices(0))]
                print(* a, sep = "\n")

                dir = 'cogs/'
                for x in os.listdir(dir):
                    os.remove(os.path.join(dir, x))

                try:
                    global w
                    w =  open('cogs/mic.txt', 'r')
                    mic = w.read()
        
        
                except Exception as e:
                    print(f"==="*20)
                    w =  open('cogs/mic.txt', 'w')
                    user = input("please choose a mic: ")
                    w.write(user)
                    mic = user

            elif f == "/list effects":
                directory_path = 'effects/'
                files = [f for f in listdir(directory_path) if isfile(join(directory_path, f))]
                print(*files, sep= "\n")

            elif f == "/help":
                print(
                """
                /help -- shows this message

                /about -- About the app

                /play -- Allows the user to pick a mp3 file to play from the effects directory

                /config mic -- Allows user to change virtual microphones

                /list effects -- lists all the mp3 files in the effects library

                /exit -- Will exit the pogram

                """    
                )

            elif f == "/about":
                print(f"""
                
                Created By Will Payne 
                License: MIT
                Version: {version}

                This app was created for Discord. It can be used if you have a broken mic.
                
                """
                )

            elif f == "/exit":
                import sys
                sys.exit()

            else:            
                print("Reading & converting")
                t = gTTS(f, lang='en')
                num += 1
                t.save(f"sound/yo{num}.mp3")
                print("--"*20)
                mixer.quit()
                mixer.init(devicename=mic)
                mixer.music.load(f"sound/yo{num}.mp3")
                mixer.music.play()

        except Exception as e:
            print(e)
                        
start()


