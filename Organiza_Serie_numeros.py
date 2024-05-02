import pandas as pd
import openpyxl
import Tools_program


def organiza_series():
    #file_name = "serie_luis.txt"
    file_name = "Serie_LightRoulett_Luis.txt"


    with open(file_name, "r") as archivo:
        datos = archivo.read()

    rojos = "01,03,05,07,09,12,14,16,18,19,21,23,25,27,30,32,34,36"
    tbl_result = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]

    tbl_decena= [[0,0,0,0,0],
                [0,0,0,0,0],
                [0,0,0,0,0],
                [0,0,0,0,0],
                [0,0,0,0,0],
                [0,0,0,0,0],
                [0,0,0,0,0],
                [0,0,0,0,0],
                [0,0,0,0,0],
                [0,0,0,0,0],
                [0,0,0,0,0],
                [0,0,0,0,0],
                [0,0,0,0,0],
                [0,0,0,0,0],
                [0,0,0,0,0],
                [0,0,0,0,0],
                [0,0,0,0,0],
                [0,0,0,0,0],
                [0,0,0,0,0],
                [0,0,0,0,0],
                [0,0,0,0,0],
                [0,0,0,0,0],
                [0,0,0,0,0],
                [0,0,0,0,0],
                [0,0,0,0,0],
                [0,0,0,0,0],
                [0,0,0,0,0],
                [0,0,0,0,0],
                [0,0,0,0,0],
                [0,0,0,0,0],
                [0,0,0,0,0],
                [0,0,0,0,0],
                [0,0,0,0,0],
                [0,0,0,0,0],
                [0,0,0,0,0],
                [0,0,0,0,0],
                [0,0,0,0,0]]

    tbl_color = [[0,0,0,0],
                [0,0,0,0],
                [0,0,0,0],
                [0,0,0,0],
                [0,0,0,0],
                [0,0,0,0],
                [0,0,0,0],
                [0,0,0,0],
                [0,0,0,0],
                [0,0,0,0],
                [0,0,0,0],
                [0,0,0,0],
                [0,0,0,0],
                [0,0,0,0],
                [0,0,0,0],
                [0,0,0,0],
                [0,0,0,0],
                [0,0,0,0],
                [0,0,0,0],
                [0,0,0,0],
                [0,0,0,0],
                [0,0,0,0],
                [0,0,0,0],
                [0,0,0,0],
                [0,0,0,0],
                [0,0,0,0],
                [0,0,0,0],
                [0,0,0,0],
                [0,0,0,0],
                [0,0,0,0],
                [0,0,0,0],
                [0,0,0,0],
                [0,0,0,0],
                [0,0,0,0],
                [0,0,0,0],
                [0,0,0,0],
                [0,0,0,0]]

    tbl_family = [[0,0,0,0,0],
                  [0,0,0,0,0],
                  [0,0,0,0,0],
                  [0,0,0,0,0],
                  [0,0,0,0,0],
                  [0,0,0,0,0],
                  [0,0,0,0,0],
                  [0,0,0,0,0],
                  [0,0,0,0,0],
                  [0,0,0,0,0],
                  [0,0,0,0,0],
                  [0,0,0,0,0],
                  [0,0,0,0,0],
                  [0,0,0,0,0],
                  [0,0,0,0,0],
                  [0,0,0,0,0],
                  [0,0,0,0,0],
                  [0,0,0,0,0],
                  [0,0,0,0,0],
                  [0,0,0,0,0],
                  [0,0,0,0,0],
                  [0,0,0,0,0],
                  [0,0,0,0,0],
                  [0,0,0,0,0],
                  [0,0,0,0,0],
                  [0,0,0,0,0],
                  [0,0,0,0,0],
                  [0,0,0,0,0],
                  [0,0,0,0,0],
                  [0,0,0,0,0],
                  [0,0,0,0,0],
                  [0,0,0,0,0],
                  [0,0,0,0,0],
                  [0,0,0,0,0],
                  [0,0,0,0,0],
                  [0,0,0,0,0],
                  [0,0,0,0,0]]


    tmp_data = {'numero':[], 'repetidos':[]}
    tmp_dece = {'numero':[], 'repetidos':[]}
    tmp_colo = {'numero':[], 'repetidos':[]}
    tmp_famy = {'numero':[], 'repetidos':[]}

    data_result = {'numero':[], 'lista_win': []}
    dece_result = {'numero':[], 'lista_win': []}
    colo_result = {'numero':[], 'lista_win': []}
    famy_result = {'numero':[], 'lista_win': []}

    pos = datos.find(",")
    valor = int(datos[0:pos])
    datos = datos[pos+1:len(datos)]
    long_serie = len(datos)
    ceros = 0
    cant_numeros = 0
    total = 0

    df_tmp = pd.DataFrame(tmp_data)
    de_tmp = pd.DataFrame(tmp_dece)
    co_tmp = pd.DataFrame(tmp_colo)
    fa_tmp = pd.DataFrame(tmp_famy)

    df_data_result = pd.DataFrame(data_result)
    df_dece_result = pd.DataFrame(dece_result)
    df_colo_result = pd.DataFrame(colo_result)
    df_famy_result = pd.DataFrame(famy_result)

    while len(datos) > 0:
        pos = datos.find(",")
        if pos >= 0:
            valor1 = int(datos[0:pos])
            tbl_result[valor][valor1] = tbl_result[valor][valor1] + 1
            decena = Tools_program.calc_decena(valor1)
            tbl_decena[valor][decena] = tbl_decena[valor][decena] + 1
            tbl_decena[valor][4] = tbl_decena[valor][4] + 1

            if datos[0:pos] == "00":
                color = 0
            else:
                if rojos.find(datos[0:pos]) < 0:
                    color = 1
                else:
                    color = 2
            tbl_color[valor][color] = tbl_color[valor][color] + 1
            tbl_color[valor][3] = tbl_color[valor][3] + 1

            familia = Tools_program.calc_familia(datos[0:pos])
            tbl_family[valor][familia] = tbl_family[valor][familia] + 1
            tbl_family[valor][4] = tbl_family[valor][4] + 1

            cant_numeros += 1
            if valor == valor1 and valor == 0:
                ceros += 1
            valor = valor1
            datos = datos[pos + 1:len(datos)]
            if len(datos) < 20:
                pass
        else:
            break

    print("Cantidad de jugadas: " + str(cant_numeros))
    for i in range(0, 37):
        c_n = 0
        for j in range(0, 37):
            lista = ""
            if tbl_result[i][j] > 0:
                new_record = {'numero': j, 'repetidos': tbl_result[i][j]}
                df_tmp = df_tmp._append(new_record, ignore_index=True)

        for j in range(0, 4):
            #if tbl_decena[i][j] > 0:
            new_record = {'numero': j, 'repetidos': tbl_decena[i][j]/tbl_decena[i][4]}
            de_tmp = de_tmp._append(new_record, ignore_index=True)

        for j in range(0, 3):
            #if tbl_color[i][j] > 0:
            new_record = {'numero': j, 'repetidos': tbl_color[i][j]/tbl_color[i][3]}
            co_tmp = co_tmp._append(new_record, ignore_index=True)

        for j in range(0, 4):
            #if tbl_family[i][j] > 0:
            new_record = {'numero': j, 'repetidos': tbl_family[i][j]/tbl_family[i][4]}
            fa_tmp = fa_tmp._append(new_record, ignore_index=True)

        df_1 = df_tmp.sort_values(by='repetidos', ascending=False)
        df_2 = de_tmp.sort_values(by='repetidos', ascending=False)
        df_2 = de_tmp
        df_3 = co_tmp
        df_4 = fa_tmp

        for h in range(0, len(df_1)):
            if int(df_1.values[h][0]) < 10:
                num = "0" + str(int(df_1.values[h][0]))
            else:
                num = str(int(df_1.values[h][0]))
            if lista == "":
                lista = num
            else:
                lista = lista + "-" + num
            if h>25:
                break
        lista_d=""
        for h in range(0,len(df_2)):
            num = str(round(df_2.values[h][1]*100,2))[:5]
            if lista_d == "":
                lista_d = num
            else:
                lista_d = lista_d + "-" + num

        lista_c=""
        for h in range(0,len(df_3)):
            num = str(round(df_3.values[h][1]*100,2))[:5]
            if lista_c == "":
                lista_c = num
            else:
                lista_c = lista_c + "-" + num

        lista_f = ""
        for h in range(0, len(df_4)):
            num = str(round(df_4.values[h][1] * 100, 2))[:5]
            if lista_f == "":
                lista_f = num
            else:
                lista_f = lista_f + "-" + num

        tmp_data = {'numero': [], 'repetidos': []}
        tmp_dece = {'numero': [], 'repetidos': []}
        tmp_colo = {'numero': [], 'repetidos': []}
        tmp_famy = {'numero': [], 'repetidos': []}

        df_tmp = pd.DataFrame(tmp_data)
        de_tmp = pd.DataFrame(tmp_dece)
        co_tmp = pd.DataFrame(tmp_dece)
        fa_tmp = pd.DataFrame(tmp_famy)

        new_record = {'numero': str(i), 'lista_win': lista}
        df_data_result = df_data_result._append(new_record, ignore_index=True)

        new_record = {'numero': str(i), 'lista_win': lista_d}
        df_dece_result = df_dece_result._append(new_record, ignore_index=True)

        new_record = {'numero': str(i), 'lista_win': lista_c}
        df_colo_result = df_colo_result._append(new_record, ignore_index=True)

        new_record = {'numero': str(i), 'lista_win': lista_f}
        df_famy_result = df_famy_result._append(new_record, ignore_index=True)

    #print(df_data_result)
    #print(df_dece_result)
    #print(df_colo_result)
    #print(df_famy_result)

    df_data_result.to_excel("Luis_numeros.xlsx", index= False)
    df_dece_result.to_excel("Luis_decenas.xlsx", index= False)
    df_colo_result.to_excel("Luis_colores.xlsx", index= False)
    df_famy_result.to_excel("Luis_familia.xlsx", index= False)