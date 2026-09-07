class Solution:
    def exist(self, board, word):

        # pra primeira letra, guarda todas as posicoes que possuem ela. (em listas de tamanho 1 das coords)
        # vai pra proxima letra. na proxima letra, para cada posicao da lista anterior, analizar vizinhos e guardar todos todos as listas de posicao anterior + novo vizinho
        # repete ate o fim

        possibilities = [[] for _ in range(len(word))]

        n_lists = len(board)
        n_cells_list = len(board[0])

        #print(n_lists)
        #print(n_cells_list)

        for list_pos in range(n_lists):
            for cell_pos in range(n_cells_list):
                # print(cell_pos, ", ", list_pos)
                if board[list_pos][cell_pos] == word[0]:
                    possibilities[0].append([(list_pos,cell_pos)]) # guardo posicao

        '''
        for letter in range(1, len(word)):
            for list in range(n_lists):
                for cell in range(n_cells_list):
                    if board[list][cell] == word[letter]:
                        possibilities[letter].append((list,cell)) # guardo posicao
        '''


        for letter in range(len(word)-1):
            #print(possibilities)
            for possibility in possibilities[letter]:
                # possibility é uma array, entao pego o ultimo elemento pra consultar vizinhos
                list_pos,cell_pos = possibility[-1]

                neighbors_pos = self.neighbors(n_lists, n_cells_list, (list_pos, cell_pos))
                #print(possibility[-1])
                #print(neighbors_pos, "aa")

                for pos in neighbors_pos:
                    #print(pos, word[letter])
                    #print(n_lists, n_cells_list)
                    
                    # se o vizinho tiver a letra correta e nao tiver sido usado anteriormente nessa mesma array.
                    if board[pos[0]][pos[1]] == word[letter+1] and pos not in possibility:
                        possibilities[letter+1].append(possibility+[pos])
                    #else:
                        #print(board[pos[0]][pos[1]], pos, word[letter], "FAIL", possibility)




        return len(possibilities[-1]) > 0

    
    def neighbors(self, n_lists, n_cells_list, pos):
        row, col = pos

        neighbors_list = []

        # Up
        if row > 0:
            neighbors_list.append((row - 1, col))

        # Down
        if row < n_lists - 1:
            neighbors_list.append((row + 1, col))

        # Left
        if col > 0:
            neighbors_list.append((row, col - 1))

        # Right
        if col < n_cells_list -1:
            neighbors_list.append((row, col + 1))

        return neighbors_list

s = Solution()

board = [
  ["A","B","C","D"],
  ["S","A","A","T"],
  ["A","C","A","E"]
]
word = "CAT"

#print(s.exist(board,word))

board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]


word = "ABCB"

print(s.exist(board,word))
