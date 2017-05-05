#coding: utf-8
t = float(raw_input("Digite a temperatura em Celsius: "))

def celsius_fahrenheit(c=0):
    # round(n, d) => arredonda n em d casas decimais
    return round(9. * c / 5. + 32., 2)

print "A temperatura em %.2f em graus celsius é %.2f fahrenheit " %(t, celsius_fahrenheit(t))
