import pyautogui as pa
import time

def calc_decena(numero):
    if numero == 0:
        return 0
    elif numero/12 - numero//12 == 0:
        return numero//12
    else:
        return numero // 12 + 1


def calc_familia(numero):
    seccion_1 = "32-15-19-04-21-02-25-17-34-06-27-13"
    seccion_2 = "36-11-30-08-23-10-05-24-16-33-01-20"
    seccion_3 = "14-31-09-22-18-29-07-28-12-35-03-26"
    if seccion_1.find(numero) < 0:
        if seccion_2.find(numero) < 0:
            if seccion_3.find(numero) < 0:
                return 3
            else:
                return 2
        else:
            return 1
    else:
        return 0


def find_win(list_win, numero):
    if list_win.find(numero) < 0:
        return False
    else:
        return True


def play_number(list_wins, df_coordenadas):
    while len(list_wins) > 0:
        val_num = list_wins[:2]
        pos_X = df_coordenadas['Coord_X'][int(val_num)]
        pos_Y = df_coordenadas['Coord_Y'][int(val_num)]
        pa.moveTo(x=pos_X, y=pos_Y)
        time.sleep(0.2)
        pa.click()
        list_wins = list_wins[list_wins.find("-") + 1: 500]


def make_list(num, df_numbers, df_dozen, df_colors):
    numb_list = df_numbers["lista_win"][num]
    dezen = df_dozen["lista_win"][num]
    dezen.find("-")
    de_0 = float(dezen[0: dezen.find("-")])
    dezen = dezen[dezen.find("-") + 1: 50]
    de_1 = float(dezen[0: dezen.find("-")])
    dezen = dezen[dezen.find("-") + 1: 50]
    de_2 = float(dezen[0: dezen.find("-")])
    de_3 = float(dezen[dezen.find("-") + 1: 50])
    many_chips = 6

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
    if list_wins.find("00") < 0:
        list_wins = ""

    for i in range(0, 5):
        val_num = numb_list[0: numb_list.find("-")]
        if list_wins.find(val_num) < 0:
            list_wins = list_wins + "-" + val_num

        numb_list = numb_list[numb_list.find("-") + 1: 500]

    while len(numb_list) > 0:
        val_num = numb_list[0: numb_list.find("-")]
        if val_num != "00" and list_wins.find(val_num) < 0:
            if deze_1 and int(val_num) < 13:
                list_wins = list_wins + "-" + val_num
                many_chips += 1

            if deze_2 and int(val_num) > 12 and int(val_num) < 25:
                list_wins = list_wins + "-" + val_num
                many_chips += 1

            if deze_3 and int(val_num) > 24:
                list_wins = list_wins + "-" + val_num
                many_chips += 1

        if numb_list.find("-") < 0:
            break
        numb_list = numb_list[numb_list.find("-") + 1: 500]
    return list_wins, many_chips

def buscar_premio(num, prem):
    pos_num = prem.find(" " + str(num) + "x")
    if prem.find(str(num) + "x") > -1:
        while len(prem) > 0:
            pos_coma = prem.find(",", pos_num)
            if pos_coma < 0:
                pos_coma = pos_num + 6
            valor_premio = prem[pos_num:pos_coma]
            pos_x = valor_premio.find("x")
            if num == int(valor_premio[:pos_x]):
                return int(valor_premio[pos_x + 1:40])
                break
            else:
                return 30
                break
    else:
        return 30