#Agrupar parentesis que abre y que cierra de forma que tengan la misma cantidad de cada uno
from typing import Sized

class Solution:
    def solve(self, s):
        pc = ''
        cont = 0
        index = 0
        listaR = []
        for index in s:
            if index == '(':
                pc = pc + '('
                cont +=1
            elif index == ')' and cont == 1:
                pc = pc + index
                listaR.append(pc)
                cont-=1
                pc = ''
            else:
                pc = pc + index
                cont-=1         
        return listaR

    def solve1(self, n):
        s = str(n)
        result = 0
        for digit in s:
            result += int(digit)
            
        if len(str(result)) == 1:
            return result
        elif len(str(result)) >= 2:
            return Solution.solve1(self,result)
             

sol = Solution()
x = int(input('Ingresa un numero entero: '))
print('La suma de cada digito del numero en una sola cifra es:',sol.solve1(x))
print(sol.solve('()()()(())((()))(((())))()'))