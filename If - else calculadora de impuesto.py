#si el ingreso del ciudadano no era superior a 85,528 pesos, el impuesto era igual al 18% del ingreso menos 556 pesos y 2 centavos.
#si el ingreso era superior a esta cantidad, el impuesto era igual a 14,839 pesos y 2 centavos, más el 32% del excedente sobre 85,528 pesos.
ingreso = int(input ("Hola, por favor digame su ingreso y yo le diré su impuesto "))
if ingreso <= 85528:
    impuesto = round((ingreso * 0.18) - 556 + 0.2) 
    
else: impuesto = round((ingreso - 85528) * 0.32 + (14.839+.2))
print ("Su impuesto es: " , impuesto)
