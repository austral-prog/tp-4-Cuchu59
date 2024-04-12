def line():
    import math
    
    A = float(input('Ingrese el coeficiente A: '))
    B = float(input('Ingrese el coeficiente B: '))
    X1 = float(input('Ingrese el coeficiente X1: '))
    X2 = float(input('Ingrese el coeficiente X2: '))

    Y1 = (A * X1) + B
    Y2 = (A * X2) + B
    
    P1 = [X1, Y1]
    P2 = [X2, Y2]

    distance = math.dist(P1,P2)

    print(f"""     
El coeficiente A de su ecuación de la recta es: {A} 
El coeficiente B de su ecuación de la recta es: {B} 
El coeficiente X1 de su ecuación de la recta es: {X1} 
El coeficiente X2 de su ecuación de la recta es: {X2}

Para la siguiente ecuación:
        Y = {A}x + {B}

Dados los siguientes puntos:
        P1 ({X1}, {Y1})
        P2 ({X2}, {Y2})

La distancia entre ellos es: {distance}
    """)
