import random
import time


def seis(salaAgora):
    if salaAgora == 6:
        print('''        ╭══════════════════════════════════════════════════════════════════════════════════╮
            Você caiu em uma ravina e foi direcionado para a sala 8 e perdeu uma jogada
        ╰══════════════════════════════════════════════════════════════════════════════════╯
        ''')
        salaAgora = 8
        return salaAgora
    else:
        return salaAgora

print('''
    ●▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬ஜ۩۞۩ஜ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬●
    ☠                                Bem-vindo a Dungeon Final                        ☠
    ●▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬ஜ۩۞۩ஜ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬●
    ||           Tudo estava em paz quando, de repente, um grande mal desperta.       ||
    ||           Liderada pelo Senhor do Mal, uma horda de criaturas malignas         ||
    ||          está espalhando caos e destruição pelo mundo. Diante de tamanha       ||
    ||           ameaça, os reinos decidem se unir para recrutar heróis que           ||
    ||           possam defendê-los, enviando-os numa busca para encontrar uma        ||
    ||           forma de destruir o Senhor do Mal de uma vez por todas.              ||
    ||                                                                                ||
    ||                                ---==REGRAS==---                                ||
    ||              1.Você tem apenas 7 jogadas para chegar até a sala 9.             ||
    ||              2.Você só poderá escolher entre red ou black.                     ||
    ||              3.Divirtam-se.                                                    ||
    ||                                                                                ||
    ||                                ---==DICA==---                                  ||
    ||                   Muito cuidado, ao caminho escolher,                          ||
    ||                   comum em dungeons armadilhas ter!!!                          ||
    ||                                                                                ||
    ●▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬ஜ۩۞۩ஜ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬●
    ☠                                    Boa Sorte                                    ☠
    ●▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬ஜ۩۞۩ஜ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬●
                                         Loading…
    ''')
time.sleep(0.5)
print('''                                ███████████████████████████
                                ███████▀▀▀░░░░░░░▀▀▀███████''')
time.sleep(0.6)
print('''                                ████▀░░░░░░░░░░░░░░░░░▀████
                                ███│░░░░░░░░░░░░░░░░░░░│███''')
time.sleep(0.6)
print('''                                ██▌│░░░░░░░░░░░░░░░░░░░│▐██
                                ██░└┐░░░░░░░░░░░░░░░░░┌┘░██''')
time.sleep(0.6)
print('''                                ██░░└┐░░░░░░░░░░░░░░░┌┘░░██
                                ██░░┌┘▄▄▄▄▄░░░░░▄▄▄▄▄└┐░░██''')
time.sleep(0.6)
print('''                                ██▌░│██████▌░░░▐██████│░▐██
                                ███░│▐███▀▀░░▄░░▀▀███▌│░███''')
time.sleep(0.6)
print('''                                ████▄─┘██▌░░░░░░░▐██└─▄████
                                █████░░▐█─┬┬┬┬┬┬┬─█▌░░█████''')
time.sleep(0.6)
print('''                                ████▌░░░▀┬┼┼┼┼┼┼┼┬▀░░░▐████
                                █████▄░░░└┴┴┴┴┴┴┴┘░░░▄█████''')
time.sleep(0.6)
print('''                                ███████▄░░░░░░░░░░░▄███████
                                ██████████▄▄▄▄▄▄▄██████████''')
time.sleep(0.6)
print('''                                         Loading…
                                        ███▒▒▒▒▒▒▒
                                           30%
    ''')

time.sleep(0.6)
print('''                                         Loading…
                                        █████▒▒▒▒▒
                                           50%
    ''')
time.sleep(0.6)
print('''                                         Loading…
                                        ██████████
                                           100%
    ''')
time.sleep(1)


room_options = {}

room_options[1] = {'red': 2, 'black': 3}
room_options[2] = {'red': 3, 'black': 4}
room_options[3] = {'red': 4, 'black': 5}
room_options[4] = {'red': 5, 'black': 6}
room_options[5] = {'red': 6, 'black': 7}
room_options[7] = {'red': 8, 'black': 9}
room_options[8] = {'red': 9, 'black': -1}

jogadas = 0
my_room = 1

while my_room != 9:
    my_options = room_options[my_room]
    print("╔════════════•ೋೋ•════════════╗")
    print(f"         ۩ SALA {my_room} ۩ \nVocê tem as opções: ")
    for option in my_options:
        print(f"[{option}] ir para caminho {option}")

    user_option = input("Sua opção: ")
    while user_option != 'red' and user_option != 'black':
        user_option = input("Opção não é válida, digite black ou red: : ")

    room_selected = room_options[my_room][user_option]
    print("╚════════════•ೋೋ•════════════╝")
    print("▬▬▬▬▬▬▬▬▬INDO PARA SALA ", room_selected)
    time.sleep(0.7)

    my_room = room_selected
    jogadas = jogadas + 1

    my_room = seis(my_room)

    print('')
    print("Total de jogadas:", jogadas)
    if (jogadas >= 7):
        print('''                █████████
                █▄█████▄█
                █▼▼▼▼▼
                █
                █ Você perdeu!
                █▲▲▲▲▲
                █████████
                ██ ██
                    ''')
        break
    elif (my_room == -1):
        print('''
             .,-:;//;:=,
         . :H@@@MM@M#H/.,+%;,
      ,/X+ +M@@M@MM%=,-%HMMM@X/,
     -+@MM; $M@@MH+-,;XMMMM@MMMM@+-
    ;@M@@M- XM@X;. -+XXXXXHHH@M@M#@/.
  ,%MM@@MH ,@%=            .---=-=:=,.
  -@#@@@MX .,              -%HX$$%%%+;
 =-./@M@M$                  .;@MMMM@MM:
 X@/ -$MM/                    .+MM@@@M
.H@@@@M@+,                    %MM+..%#$.
 /MMMM@MMH/.                  XM@MH; -;
  /%+%$XHH@$=              , .H@@@@MX,
   .=--------.           -%H.,@@@@@MX,
   .%MM@@@HHHXX$$$%+- .:$MMX -M@@MM%.
     =XMMM@MM@MM#H;,-+HMM@M+ /MMMX=
       =%@M@M#@$-.=$@MM@@@M; %M%=
         ,:+$+-,/H#MMMMMMM@- -,
               =++%%%%+/:-.

    Você acabou de cair em um portal.....\n''')
        my_room = random.randint(1, 5)
''''
TA FORA DO LAÇO
||
||
||
||
||
\/
'''
if (my_room == 9):
    print('')
    print('''
      Y O U
    ╲╭━━━━╮╲╲
    ╲┃╭╮╭╮┃╲╲
    ┗┫┏━━┓┣┛╲
    ╲┃╰━━╯┃
    ╲╰┳━━┳╯╲╲
     W I N
    ''')
