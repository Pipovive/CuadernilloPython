par = []
impar = []
numeros = [1,2,3,4,5,6,7,8,9]
def separador_listas (numeros): 
    for i in numeros:
        if (i % 2) == 0:
            par.append(i)
        else :
            impar.append(i)
            
separador_listas(numeros)
print(par)
print(impar) 
