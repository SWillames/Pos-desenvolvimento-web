#coding: utf-8
t = float(raw_input("Digite a temperatura em Fahrenheit: "))

def fahrenheit_celsius(f=0):
    return round(5. * (f - 32.) / 9., 2)

print "A temperatura %.2f em Fahrenheit é: %.2f Celsius" % (t, fahrenheit_celsius(t))
