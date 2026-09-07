class Solution:
    def combinationSum(self, candidates, target):
        # forma que parece melhor incialmente, é construir array que codifica todas possibilidade que soma qualquer numero.

        # eu nao construo array que codifica a existencia ou nao de um numero, senao, pra n numeros terei 2^n combinacoes.

        # cada pos da minha matriz codifica possibilidades de somar aquele numero.
        # problema é que eu preciso armazenar as solucoes em si em algum lugar, entao nao posso so fazer isso, eu preciso verdadeiramente codificar as solucoes.

        # como candidates length é 30, entao 2^30 nao é tao ruim. seria 1gb de dados.
        # candidates podem ser usados numero ilimitado de vezes.
        # eu sei que target <=40, entao posso guardar todas as somas de cada numero de 1 até 40.
        #
        # exemplo: candidates = [2,3,6,7], target = 7

        # target = 1, possibilities = 0
        # target = 2, possibilities = 1 (possibilities 1 * possibilities 1) + (2)
        # target = 3, possibilities = 1 (possibilities 1 * possibilities 2) + (3)
        # target = 4, possibilities = 1 (possibilities 1 * possibilities 3) + (possibilities 2 * possibilities 2) + (4)
        # target = 5, possibilities = 1 (possibilities 1 * possibilities 4) + (possibilities 2 * possibilities 3) + (5)
        # target = 6, possibilities = 3 (possibilities 1 * possibilities 5) + (possibilities 2 * possibilities 4) + (possibilities 3 * possibilities 3) + (6)
        # target = 7, possibilities = 3 (possibilities 1 * possibilities 6) + (possibilities 2 * possibilities 5) + (possibilities 3 * possibilities 4) + (7)
        
        # nao posso guardar como valores, preciso guardar como conjuntos. E entao realizo operacoes sobre conjuntos.

        possibilites = [set() for _ in range(target + 1)] # inclui 0

        for number in range(target+1):
            if number in candidates:
                possibilites[number].add(tuple([number]))

            for left_number in range(1, int(number/2)+1):
                right_number = number - left_number
                for left in possibilites[left_number]:
                    for right in possibilites[right_number]:
                        # print("right_numb: ", right_number, "   number: ", number)
                        possibilites[number].add(tuple(sorted(left+right)))

        possibilites_final = [list(p) for p in possibilites[target]]

        return possibilites_final


s = Solution()

print(s.combinationSum([2,3,5], 8))