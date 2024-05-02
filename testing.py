num = 15
prem = "4x50, 3x500, 1x500"
pos_num = prem.find(str(num) + "x")
if prem.find(str(num) + "x") > -1:
    while len(prem) > 0:
        pos_coma = prem.find(",", pos_num)
        if pos_coma<0:
            pos_coma = pos_num + 6
        valor_premio = prem[pos_num:pos_coma]
        pos_x = valor_premio.find("x")
        if num == int(valor_premio[:pos_x]):
            print(int(valor_premio[pos_x + 1:40]))
            break
        else:
            print(30)
            break
else:
    print(30)