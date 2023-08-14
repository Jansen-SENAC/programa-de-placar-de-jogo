TEAM1 = int(input("Digíte quantos gols o time 1 fez: "))
TEAM2 = int(input("Dígite quantos gols o time 2 fez: "))
if TEAM1>TEAM2:
   print ("Time 1 ganhador e time 2 perdedor ")
if TEAM2>TEAM1:
   print ("Time 2 ganhador e time 1 perdedor ")
elif TEAM1 == TEAM2:
   print ("empate!!")