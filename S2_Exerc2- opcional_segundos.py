total = input("Por favor, entre com o número de segundos que deseja converter: ")
total_seg = int(total)

dias = total_seg // 86400
resta1 = total_seg % 86400
horas = resta1 // 3600
resta2 = resta1 % 3600
minutos = resta2 // 60
segundos = resta2 % 60
print(dias, "dia(s),", horas, "hora(s),", minutos, "minuto(s) e", segundos, "segundo(s)")
