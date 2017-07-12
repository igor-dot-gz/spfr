from time import sleep
import os
while True:
    os.system('cls')
    print("╔═════════════════════════════════════════╗")
    print("║            record.txt totals            ║")
    c = 0
    i = 0
    e = 0
    with open('record.txt', 'r') as inF:
        for line in inF:
            e = e + 1
            if 'Correct' in line:            
                c = c + 1
            elif 'Incorrect' in line:
                i = i + 1
    if e >= 0:
        perc = float(c / e)
        perc = perc * float(100)
        peri = float(i / e)
        peri = peri * float(100)
        print("║                                         ║")
        print("║Entries:            : " + str(e) + "\t\t║")
        print("║                                         ║")
        print("║Correct             : " + str(c) + "\t\t  ║")
        print("║Percentage Correct  : " + str(perc) + "% ║")
        print("║                                         ║")
        print("║Incorrect           : " + str(i) + "\t\t  ║")
        print("║Percentage Incorrect: " + str(peri) + "%║")
        print("║                                         ║")
        print("╚═════════════════════════════════════════╝")
    else:
        print("║Oh no!                                   ║")
        print("╚═════════════════════════════════════════╝")
    sleep(1)