import pandas as pd
import openpyxl
import pyautogui as pa
import time
print(pa.position())

file_numbers = "Luis_numeros.xlsx"
file_dozen = "Luis_decenas.xlsx"
file_colors = "Luis_colores.xlsx"
file_family = "Luis_familia.xlsx"
file_coordenadas = "coordenadas.xlsx"

df_numbers = pd.read_excel(file_numbers)
df_dozen = pd.read_excel(file_dozen)
df_colors = pd.read_excel(file_colors)
df_family = pd.read_excel(file_family)
df_coordenadas = pd.read_excel(file_coordenadas)
df_combinate = pd.DataFrame()
df_combinate["Number"] = None
df_combinate = df_combinate.assign(list=None)

num=30
#for num in range(0, 37):

numb_list = df_numbers["lista_win"][num]
dezen = df_dozen["lista_win"][num]
dezen.find("-")
de_0 = float(dezen[0 : dezen.find("-")])
dezen = dezen[dezen.find("-") + 1 : 50]
de_1 = float(dezen[0 : dezen.find("-")])
dezen = dezen[dezen.find("-") + 1 : 50]
de_2 = float(dezen[0 : dezen.find("-")])
de_3 = float(dezen[dezen.find("-") + 1 : 50])

if de_1 > de_2:
    deze_1 = True
elif de_1 > de_3:
    deze_1 = True
else:
    deze_1 = False

if de_2 > de_1:
    deze_2 = True
elif de_2 > de_3:
    deze_2 = True
else:
    deze_2 = False

if de_3 > de_1:
    deze_3 = True
elif de_3 > de_2:
    deze_3 = True
else:
    deze_3 = False

list_wins = "00"
pos_X = df_coordenadas['Coord_X'][0]
pos_Y = df_coordenadas['Coord_Y'][0]
pa.moveTo(x=pos_X, y=pos_Y)
pa.click()
time.sleep(0.2)
for i in range(0, 5):
    val_num = numb_list[0 : numb_list.find("-")]
    if list_wins.find(val_num) < 0:
        list_wins = list_wins + " - " + val_num
    pos_X = df_coordenadas['Coord_X'][int(val_num)]
    pos_Y = df_coordenadas['Coord_Y'][int(val_num)]
    pa.moveTo(x=pos_X, y=pos_Y)
    pa.click()
    time.sleep(0.1)

    numb_list = numb_list[numb_list.find("-") + 1 : 500]

while len(numb_list) > 0:
    val_num = numb_list[0 : numb_list.find("-")]
    if val_num != "00" and list_wins.find(val_num) < 0:
        if deze_1 and int(val_num) < 13:
            list_wins = list_wins + " - " + val_num
            pos_X = df_coordenadas['Coord_X'][int(val_num)]
            pos_Y = df_coordenadas['Coord_Y'][int(val_num)]
            pa.moveTo(x=pos_X, y=pos_Y)
            pa.click()
            time.sleep(0.1)
        if deze_2 and int(val_num) > 12 and int(val_num) < 25:
            list_wins = list_wins + " - " + val_num
            pos_X = df_coordenadas['Coord_X'][int(val_num)]
            pos_Y = df_coordenadas['Coord_Y'][int(val_num)]
            pa.moveTo(x=pos_X, y=pos_Y)
            pa.click()
            time.sleep(0.1)
        if deze_3 and int(val_num) > 24:
            list_wins = list_wins + " - " + val_num
            pos_X = df_coordenadas['Coord_X'][int(val_num)]
            pos_Y = df_coordenadas['Coord_Y'][int(val_num)]
            pa.moveTo(x=pos_X, y=pos_Y)
            pa.click()
            time.sleep(0.2)
    if numb_list.find("-") < 0:
        break
    numb_list = numb_list[numb_list.find("-") + 1 : 500]

new_row = {"Number": str(num) + "--->", "list": list_wins}
df_combinate = df_combinate._append(new_row, ignore_index=True)
df_combinate.to_excel("Luis_combinados.xlsx", index=False)
