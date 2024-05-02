import urllib.request
import json
import time
import os
import pandas as pd
import pyautogui as pa

import Tools_program
import Organiza_Serie_numeros
#url = 'https://api.casinoscores.com/svc-evolution-game-events/api/immersiveroulette/latest'
#url = 'https://api.casinoscores.com/svc-evolution-game-events/api/xxxtremelightningroulette/latest'
#url = 'https://api.casinoscores.com/svc-evolution-game-events/api/frenchroulettegold/latest'

amount_chips = 0.20
balance = 174 / amount_chips
take_profit = balance + (balance * 0.25)
loos_profit = balance - (balance * 0.40)

wait_ball = 250
max_ball = 50
many_ball_play = 0
many_ball_wait = 0
play = True
play_real = True
list_wins = ""
chips_play = 0

file_numbers = "Luis_numeros.xlsx"
file_dozen = "Luis_decenas.xlsx"
file_colors = "Luis_colores.xlsx"
file_family = "Luis_familia.xlsx"
file_coordenadas = "coordenadas.xlsx"

Organiza_Serie_numeros.organiza_series()

df_numbers = pd.read_excel(file_numbers)
df_dozen = pd.read_excel(file_dozen)
df_colors = pd.read_excel(file_colors)
df_family = pd.read_excel(file_family)
df_coordenadas = pd.read_excel(file_coordenadas)

url = 'https://api.casinoscores.com/svc-evolution-game-events/api/lightningroulette/latest'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

id_list = []
fileName = r"juansagaz.txt"
if os.path.exists(fileName):
    k = open("juansagaz.txt", "r")
    last_numero = k.readlines()[-1]
    nuevo = False
    continuar = False
    if last_numero == "":
        nuevo = True
    else:
        continuar = True
    k.close()
else:
    nuevo = True
    continuar = False

print("Start Balance: " + str(balance))
while True:
    f = open("ballhistory.txt", "a")
    g = open("juansagaz.txt", "a")

    time.sleep(5)
    req = urllib.request.Request(url=url, headers=headers)
    response = urllib.request.urlopen(req)
    json_data = json.loads(response.read())

    # If the id doesn't exist
    if json_data['id'] not in id_list:
        id_list.append(json_data['id'])
        if int(str(json_data["data"]["result"]["outcome"]["number"])) < 10:
            numero = "0" + str(json_data["data"]["result"]["outcome"]["number"]) + ","
        else:
            numero = str(json_data["data"]["result"]["outcome"]["number"]) + ","
        list_premio = json_data["data"]["result"]["luckyNumbersList"]
        premio = ""
        for i in range(0,len(list_premio)):
            if premio != "":
                premio = premio + ", "
            premio = premio \
                     + str(json_data["data"]["result"]["luckyNumbersList"][i]["number"]) \
                     + "x" + str(json_data["data"]["result"]["luckyNumbersList"][i]["roundedMultiplier"])
        num_juan = str(json_data["data"]["result"]["outcome"]["number"]) + " - " + premio + "\n"
        if int(numero[:2]) < 10:
            numero = '0'+str(int(numero[:2]))
        else:
            numero = str(int(numero[:2]))
        f.write(numero+",")
        g.write(num_juan)
        print(len(id_list), "data points")
        print("ganador:" + numero + "   Premios:" + premio)
        if many_ball_play == 0:
            many_ball_play = 1
            continue

        if play:
            list_preview = list_wins
            list_wins, chips_play = Tools_program.make_list(int(numero[:2]), df_numbers, df_dozen, df_colors)
            print("Play List: " + list_wins)
            print("Cantidad de Fichas Jugadas: " + str(chips_play))
            if many_ball_play > 1:
                if list_preview.find(numero) >= 0:
                    val_premio = Tools_program.buscar_premio(int(numero), premio)
                    balance = balance + val_premio
                    print("WIN!!!!!!")
                else:
                    print("loss  ??????????")
            print()
            balance -= chips_play
            print("New Balance: " + str(balance))

            if max_ball > many_ball_play:
                #if balance > loos_profit and balance < take_profit:
                if loos_profit < balance < take_profit:
                    many_ball_play += 1
                    time.sleep(1)
                    if play_real:
                        #Tools_program.play_number(list_wins, df_coordenadas)
                        pass
                else:
                    many_ball_wait += 1
                    play = False
                    many_ball_play = 0
            else:
                many_ball_wait += 1
                play = False
                many_ball_play = 0
        else:
            many_ball_wait += 1
            if many_ball_wait >= max_ball:
                play = True
                many_ball_wait = 0
                take_profit = balance - balance * 0.25
                loos_profit = balance + balance * 0.20

    f.close()
    g.close()


