# -----------------
# |  BIRKA  JÁTÉK  |
# -----------------

# Birkák mozgatása lövésnél
# Ha eléri a falat, vesztés
# Halott birkák
# sérült birkák
# szeretne-e még játszani?

import os
import random

# Milyen birkak lehetnek es hol
van_birka = 'o'
nincs_birka = '.'
halott_birka = 'x'
serult_birka = 's'
birka = []


def jatekos_udvozlese():
    file_obj = open('sheep.txt')
    tartalom = file_obj.read()
    print(tartalom)
    file_obj.close()
    input(' ')
    print("Üdv a Birka lövő játékban!")
    input(' ')
    print('Ha nem szereted ezeket a szegény jószágokat, vagy csak szeretsz lövöldözni, ez a neked való játék!')
    input(' ')
    print('Minden o jelzés egy birkát jelöl, aki szeretné, ha békén hagynád, de te nem fogod.')
    print('Az oszlop (A,B,C...)és sor (1,2,3...) koordináták segítségével tudod leadni a lövéseidet.')
    input(' ')
    print(
        'Ne bízd el magad! A leadott lövéseidet meghallják és odébb ugranak. Ha valamelyikük eléri a karám szélét\nvesztettél!')
    input(' ')
    print(
        'Nem biztos, hogy mindig jól célzol... Előfordulhatnak sérült birkák is (S), akik ugyanúgy küzenek az életükért.')
    input(' ')
    print('Lássuk mire vagy képes...')


def tabla_megjelenites(birka):
    os.system('cls||clear')
    print('')
    print('')
    print('     A  B  C  D  E  F  G  H  I  J  K')
    print('   |---------------------------------|')
    print(' 1 | ' + birka[0] + '  ' + birka[1] + '  ' + birka[2] + '  ' + birka[3] + '  ' + birka[4] + '  ' + birka[
        5] + '  ' + birka[6] + '  ' + birka[7] + '  ' + birka[8] + '  ' + birka[9] + '  ' + birka[10] + ' |')
    print(
        ' 2 | ' + birka[11] + '  ' + birka[12] + '  ' + birka[13] + '  ' + birka[14] + '  ' + birka[15] + '  ' + birka[
            16] + '  ' + birka[17] + '  ' + birka[18] + '  ' + birka[19] + '  ' + birka[20] + '  ' + birka[21] + ' |')
    print(
        ' 3 | ' + birka[22] + '  ' + birka[23] + '  ' + birka[24] + '  ' + birka[25] + '  ' + birka[26] + '  ' + birka[
            27] + '  ' + birka[28] + '  ' + birka[29] + '  ' + birka[30] + '  ' + birka[31] + '  ' + birka[32] + ' |')
    print(
        ' 4 | ' + birka[33] + '  ' + birka[34] + '  ' + birka[35] + '  ' + birka[36] + '  ' + birka[37] + '  ' + birka[
            38] + '  ' + birka[39] + '  ' + birka[40] + '  ' + birka[41] + '  ' + birka[42] + '  ' + birka[43] + ' |')
    print(
        ' 5 | ' + birka[44] + '  ' + birka[45] + '  ' + birka[46] + '  ' + birka[47] + '  ' + birka[48] + '  ' + birka[
            49] + '  ' + birka[50] + '  ' + birka[51] + '  ' + birka[52] + '  ' + birka[53] + '  ' + birka[54] + ' |')
    print(
        ' 6 | ' + birka[55] + '  ' + birka[56] + '  ' + birka[57] + '  ' + birka[58] + '  ' + birka[59] + '  ' + birka[
            60] + '  ' + birka[61] + '  ' + birka[62] + '  ' + birka[63] + '  ' + birka[64] + '  ' + birka[65] + ' |')
    print(
        ' 7 | ' + birka[66] + '  ' + birka[67] + '  ' + birka[68] + '  ' + birka[69] + '  ' + birka[70] + '  ' + birka[
            71] + '  ' + birka[72] + '  ' + birka[73] + '  ' + birka[74] + '  ' + birka[75] + '  ' + birka[76] + ' |')
    print(
        ' 8 | ' + birka[77] + '  ' + birka[78] + '  ' + birka[79] + '  ' + birka[80] + '  ' + birka[81] + '  ' + birka[
            82] + '  ' + birka[83] + '  ' + birka[84] + '  ' + birka[85] + '  ' + birka[86] + '  ' + birka[87] + ' |')
    print(
        ' 9 | ' + birka[88] + '  ' + birka[89] + '  ' + birka[90] + '  ' + birka[91] + '  ' + birka[92] + '  ' + birka[
            93] + '  ' + birka[94] + '  ' + birka[95] + '  ' + birka[96] + '  ' + birka[97] + '  ' + birka[98] + ' |')
    print('10 | ' + birka[99] + '  ' + birka[100] + '  ' + birka[101] + '  ' + birka[102] + '  ' + birka[103] + '  ' +
          birka[104] + '  ' + birka[105] + '  ' + birka[106] + '  ' + birka[107] + '  ' + birka[108] + '  ' + birka[
              109] + ' |')
    print('   |---------------------------------|')
    print('')


def birkak_kipakolasa():
    birka_vane = ['o', '.']
    while len(birka) < 110:
        if birka.count('o') < 5:
            birka.append(nincs_birka)
            birka.append(nincs_birka)
            birka.append(nincs_birka)
            birka_sorsolas = random.randint(0, 1)
            i = birka_vane[birka_sorsolas]
            birka.append(i)
            birka.append(nincs_birka)
            birka.append(nincs_birka)
        else:
            i = nincs_birka
            birka.append(i)
    return birka


def birkaloves():
    # <editor-fold desc="Koordinatak es birkak">
    # a1 = birka[0]
    # b1 = birka[1]
    # c1 = birka[2]
    # d1 = birka[3]
    # e1 = birka[4]
    # f1 = birka[5]
    # g1 = birka[6]
    # h1 = birka[7]
    # i1 = birka[8]
    # j1 = birka[9]
    # k1 = birka[10]
    # a2 = birka[11]
    # b2 = birka[12]
    # c2 = birka[13]
    # d2 = birka[14]
    # e2 = birka[15]
    # f2 = birka[16]
    # g2 = birka[17]
    # h2 = birka[18]
    # i2 = birka[19]
    # j2 = birka[20]
    # k2 = birka[21]
    # a3 = birka[22]
    # b3 = birka[23]
    # c3 = birka[24]
    # d3 = birka[25]
    # e3 = birka[26]
    # f3 = birka[27]
    # g3 = birka[28]
    # h3 = birka[29]
    # i3 = birka[30]
    # j3 = birka[31]
    # k3 = birka[32]
    # a4 = birka[33]
    # b4 = birka[34]
    # c4 = birka[35]
    # d4 = birka[36]
    # e4 = birka[37]
    # f4 = birka[38]
    # g4 = birka[39]
    # h4 = birka[40]
    # i4 = birka[41]
    # j4 = birka[42]
    # k4 = birka[43]
    # a5 = birka[44]
    # b5 = birka[45]
    # c5 = birka[46]
    # d5 = birka[47]
    # e5 = birka[48]
    # f5 = birka[49]
    # g5 = birka[50]
    # h5 = birka[51]
    # i5 = birka[52]
    # j5 = birka[53]
    # k5 = birka[54]
    # a6 = birka[55]
    # b6 = birka[56]
    # c6 = birka[57]
    # d6 = birka[58]
    # e6 = birka[59]
    # f6 = birka[60]
    # g6 = birka[61]
    # h6 = birka[62]
    # i6 = birka[63]
    # j6 = birka[64]
    # k6 = birka[65]
    # a7 = birka[66]
    # b7 = birka[67]
    # c7 = birka[68]
    # d7 = birka[69]
    # e7 = birka[70]
    # f7 = birka[71]
    # g7 = birka[72]
    # h7 = birka[73]
    # i7 = birka[74]
    # j7 = birka[75]
    # k7 = birka[76]
    # a8 = birka[77]
    # b8 = birka[78]
    # c8 = birka[79]
    # d8 = birka[80]
    # e8 = birka[81]
    # f8 = birka[82]
    # g8 = birka[83]
    # h8 = birka[84]
    # i8 = birka[85]
    # j8 = birka[86]
    # k8 = birka[87]
    # a9 = birka[88]
    # b9 = birka[89]
    # c9 = birka[90]
    # d9 = birka[91]
    # e9 = birka[92]
    # f9 = birka[93]
    # g9 = birka[94]
    # h9 = birka[95]
    # i9 = birka[96]
    # j9 = birka[97]
    # k9 = birka[98]
    # a10 = birka[99]
    # b10 = birka[100]
    # c10 = birka[101]
    # d10 = birka[102]
    # e10 = birka[103]
    # f10 = birka[104]
    # g10 = birka[105]
    # h10 = birka[106]
    # i10 = birka[107]
    # j10 = birka[108]
    # k10 = birka[109]

    # </editor-fold>

    mezok = {
        'a1': birka[0],
        'b1': birka[1],
        'c1': birka[2],
        'd1': birka[3],
        'e1': birka[4],
        'f1': birka[5],
        'g1': birka[6],
        'h1': birka[7],
        'i1': birka[8],
        'j1': birka[9],
        'k1': birka[10],
        'a2': birka[11],
        'b2': birka[12],
        'c2': birka[13],
        'd2': birka[14],
        'e2': birka[15],
        'f2': birka[16],
        'g2': birka[17],
        'h2': birka[18],
        'i2': birka[19],
        'j2': birka[20],
        'k2': birka[21],
        'a3': birka[22],
        'b3': birka[23],
        'c3': birka[24],
        'd3': birka[25],
        'e3': birka[26],
        'f3': birka[27],
        'g3': birka[28],
        'h3': birka[29],
        'i3': birka[30],
        'j3': birka[31],
        'k3': birka[32],
        'a4': birka[33],
        'b4': birka[34],
        'c4': birka[35],
        'd4': birka[36],
        'e4': birka[37],
        'f4': birka[38],
        'g4': birka[39],
        'h4': birka[40],
        'i4': birka[41],
        'j4': birka[42],
        'k4': birka[43],
        'a5': birka[44],
        'b5': birka[45],
        'c5': birka[46],
        'd5': birka[47],
        'e5': birka[48],
        'f5': birka[49],
        'g5': birka[50],
        'h5': birka[51],
        'i5': birka[52],
        'j5': birka[53],
        'k5': birka[54],
        'a6': birka[55],
        'b6': birka[56],
        'c6': birka[57],
        'd6': birka[58],
        'e6': birka[59],
        'f6': birka[60],
        'g6': birka[61],
        'h6': birka[62],
        'i6': birka[63],
        'j6': birka[64],
        'k6': birka[65],
        'a7': birka[66],
        'b7': birka[67],
        'c7': birka[68],
        'd7': birka[69],
        'e7': birka[70],
        'f7': birka[71],
        'g7': birka[72],
        'h7': birka[73],
        'i7': birka[74],
        'j7': birka[75],
        'k7': birka[76],
        'a8': birka[77],
        'b8': birka[78],
        'c8': birka[79],
        'd8': birka[80],
        'e8': birka[81],
        'f8': birka[82],
        'g8': birka[83],
        'h8': birka[84],
        'i8': birka[85],
        'j8': birka[86],
        'k8': birka[87],
        'a9': birka[88],
        'b9': birka[89],
        'c9': birka[90],
        'd9': birka[91],
        'e9': birka[92],
        'f9': birka[93],
        'g9': birka[94],
        'h9': birka[95],
        'i9': birka[96],
        'j9': birka[97],
        'k9': birka[98],
        'a10': birka[99],
        'b10': birka[100],
        'c10': birka[101],
        'd10': birka[102],
        'e10': birka[103],
        'f10': birka[104],
        'g10': birka[105],
        'h10': birka[106],
        'i10': birka[107],
        'j10': birka[108],
        'k10': birka[109]
    }

    jatekos_koordinatak_megadasa = input('Add meg a lövés koordinátáid (oszlop/sor): ').lower()

    "".join([mezok.get(val, "") for val in jatekos_koordinatak_megadasa])

    print(jatekos_koordinatak_megadasa)

    if jatekos_koordinatak_megadasa == 'a1' or 'b1' or 'c1' or 'd1' or 'e1' or 'f1' or 'g1' or 'h1' or 'i1' or 'j1' or 'k1' or 'a2' or 'b2' or 'c2' or 'd2' or 'e2' or 'f2' or 'g2' or 'h2' or 'i2' or 'j2' or 'k2' or 'a3' or 'b3' or 'c3' or 'd3' or 'e3' or 'f3' or 'g3' or 'h3' or 'i3' or 'j3' or 'k3' or 'a4' or 'b4' or 'c4' or 'd4' or 'e4' or 'f4' or 'g4' or 'h4' or 'i4' or 'j4' or 'k4' or 'a5' or 'b5' or 'c5' or 'd5' or 'e5' or 'f5' or 'g5' or 'h5' or 'i5' or 'j5' or 'k5' or 'a6' or 'b6' or 'c6' or 'd6' or 'e6' or 'f6' or 'g6' or 'h6' or 'i6' or 'j6' or 'k6' or 'a7' or 'b7' or 'c7' or 'd7' or 'e7' or 'f7' or 'g7' or 'h7' or 'i7' or 'j7' or 'k7' or 'a8' or 'b8' or 'c8' or 'd8' or 'e8' or 'f8' or 'g8' or 'h8' or 'i8' or 'j8' or 'k8' or 'a9' or 'b9' or 'c9' or 'd9' or 'e9' or 'f9' or 'g9' or 'h9' or 'i9' or 'j9' or 'k9' or 'a10' or 'b10' or 'c10' or 'd10' or 'e10' or 'f10' or 'g10' or 'h10' or 'i10' or 'j10' or 'k10':

        if mezok[jatekos_koordinatak_megadasa] == 'o':
            x = random.randint(0, 1)
            if x == 0:
                print("Birka találat!")
                mezok[jatekos_koordinatak_megadasa] = '.'

            else:
                print("Eltaláltad, de nem volt pontos a célzás. Sérült birka.")
                mezok[jatekos_koordinatak_megadasa] = 's'
        else:
            print("Nem talált!")
    else:
        print("Kérem adjon meg rendes koordinátákat!")


# jatekos_udvozlese()
while True:
    tabla_megjelenites(birkak_kipakolasa())
    birkaloves()
