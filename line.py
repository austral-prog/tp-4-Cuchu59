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

    print(f'El coeficiente A de su ecuación de la recta es: {A}')
    print(f'El coeficiente B de su ecuación de la recta es: {B}')
    print(f'El coeficiente X1 de su ecuación de la recta es: {X1}')
    print(f'El coeficiente X2 de su ecuación de la recta es: {X2}')
    print('')
    print('Para la siguiente ecuación:')
    print(f'\tY = {A}X + {B}')
    print('')
    print('Dados los siguientes puntos:')
    print(f'\tP1 ({P1[0]}, {P1[1]})')
    print(f'\tP2 ({P2[0]}, {P2[1]})')
    print('')
    print(f'La distancia entre ellos es: {distance}')
