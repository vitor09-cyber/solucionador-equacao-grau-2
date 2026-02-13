from math import pow, sqrt

def resolution(a: float, b: float, c: float) -> tuple:
    if a == 0:
        return -c / b
    
    delta = pow(b, 2) - 4 * a * c
    
    if delta < 0:
        print(f'A equação {a}x^2 {b}x {c} = 0, não possui raiz real!!')
        return 0
    
    r1 = (-b) + sqrt(delta) / 2 * a
    r2 = (-b) - sqrt(delta) / 2 * a
    
    return r1, r2

if __name__ == '__main__':
    
    result = resolution(1, 6, 9)
    
    if type(result) is tuple:
        print(f'Resultado: R1: {result[0]}, R2: {result[1]}')
    else:
        print(f'Resultado: R: {result}')