#Leer la nota de un estudiante y decir si aprobo o reprobo

from colorama import Fore, Style

grade = int(input("Ingrese la nota del estudiante: "))

if (grade >= 70):
    print (Fore.GREEN + "Usted está aprobado")
else:
    print (Fore.RED + "Su aprendizaje es inicial")
print (Style.RESET_ALL)