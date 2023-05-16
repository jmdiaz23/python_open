#Escribe una función que pueda decirte si un año (número entero) es bisiesto o no
def bisiesto(year):
  if year%4==0 and (not(year%100==0) or year%400==0 ):
    texto='es bisiesto.'
  else:
    texto='es un año NO bisiesto.'
  return texto
year=int(input('Introduzca un año:'))
print(year,bisiesto(year))
