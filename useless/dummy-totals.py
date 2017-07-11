def go():
    foo = input("Press enter to continue...")
print("╔═════════════════════════════════════════╗")
print("║            record.txt totals            ║")
c = 0
i = 0
e = 0
with open('dummy.txt', 'r') as inF:
    for line in inF:
        e = e + 1
        pass
        if 'Correct' in line:            
            c = c + 1
        elif 'Incorrect' in line:
            i = i + 1
perc = float(c / e)
perc = perc * float(100)
peri = float(i / e)
peri = peri * float(100)
print("║                                         ║")
print("║Lines:              : " + str(e) + "\t\t  ║")
print("║                                         ║")
print("║Correct             : " + str(c) + "\t\t  ║")
print("║Percentage Correct  : " + str(perc) + "% ║")
print("║                                         ║")
print("║Incorrect           : " + str(i) + "\t\t  ║")
print("║Percentage Incorrect: " + str(peri) + "%║")
print("║                                         ║")
print("╚═════════════════════════════════════════╝")
go()