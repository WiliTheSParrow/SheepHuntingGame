# -----------------
# |  BIRKA  JÁTÉK  |
# -----------------

# 	- Ki kell rajzolni egy pályát vonalakból
# 	- Magát a karámot lehessen megszabni mekkora legyen
# 	- A program létrehozza a birkákat a karámon belül, tetszőleges poziba rakja őket (pálya száma változik, nem lehet tele birkával)
# 	- Játékos annyit lát, h megjelenik neki a pálya a birkákkal
# 	- "Kérem lőjön a birkára", sor és oszlop azonosító szerint leadja a lövését
# 	- A birkák félénk állatok, lövés pillanatában a birka ugrik egyet, az, h milyen irányba, az véletlenszerű
# 	- Esetleg sikerül eltalálni, a birka nem biztos, h rögtön meghal. Véletlenszerű, hogy hogyan találom el. A birka sérült birka lesz. S betűvel jelölöm
# 	- Cél, h leszedjük a birkákat a pályáról, lehet a jele x
# 	- HA a birka eléri a karám szélét, akkor vesztettünk.

# Tábla kirajzolása
# Birkák elhelyezése a táblára (random)
# Birkák mozgatása lövésnél
# Ha eléri a falat, vesztés
# Halott birkák
# sérült birkák
# szeretne-e még játszani?

import os
import random

# Milyen birkak lehetnek
van_birka = 'o'
nincs_birka = ' '
serult_birka = 's'
halott_birka = 'x'


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
    print('A sor (1,2,3...) és oszlop (A,B,C...) koordináták segítségével tudod leadni a lövéseidet.')
    input(' ')
    print('Ne bízd el magad! A leadott lövéseidet meghallják és odébb ugranak. Ha valamelyikük eléri a karám szélét\nvesztettél!')
    input(' ')
    print('Nem biztos, hogy mindig jól célzol... Előfordulhatnak sérült birkák is (S), akik ugyanúgy küzenek az életükért.')
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
    random_birka_kirakas = []
    birka_vane = ['o', ' ']
    while len(random_birka_kirakas) < 110:
        if random_birka_kirakas.count('o') < 5:
            random_birka_kirakas.append(nincs_birka)
            random_birka_kirakas.append(nincs_birka)
            random_birka_kirakas.append(nincs_birka)
            birka_sorsolas = random.randint(0, 1)
            i = birka_vane[birka_sorsolas]
            random_birka_kirakas.append(i)
            random_birka_kirakas.append(nincs_birka)
            random_birka_kirakas.append(nincs_birka)
        else:
            i = nincs_birka
            random_birka_kirakas.append(i)
    return random_birka_kirakas

jatekos_udvozlese()
tabla_megjelenites(birkak_kipakolasa())

jatekos_koordinatak_megadasa = input('Add meg a lövés koordinátáid (sor/oszlop): ').lower()
