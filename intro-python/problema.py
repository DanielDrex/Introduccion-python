#Agrupar parentesis que abre y que cierra de forma que tengan la misma cantidad de cada uno
class Solution:
    def solve(self, s):
        lista = list(s)
        pc = ''
        cont = 0
        index = 0
        listaR = []
        while index < len(lista):
            if lista[index] == '(':
                pc = pc + '('
                cont +=1
                index+=1 
            elif lista[index] == ')' and cont == 1:
                pc = pc + lista[index]
                listaR.append(pc)
                index+=1
                cont-=1
                pc = ''
            else:
                pc = pc + lista[index]
                cont-=1
                index+=1       
        return listaR

sol = Solution()
print(sol.solve('()()()(((())))(())'))