import sys
import time
import math



from tile import Tile

class Halma():


    def __init__(self, b_size=16, t_limit=60, c_player=Tile.P_RED):
        br = []
        f = open("/Users/asharanikota/PycharmProjects/homework/input.txt", "r")
        global st
        st = f.readline()
        #print(st)
        global val
        val = f.readline()
        val = val.strip()

        t_limit = float(f.readline())
        t_limit = 8
        for i in range(16):
            br.append(f.readline().split())
        for i in range(16):
            word = br[i][0]
            br[i] = [word[i:i + 1] for i in range(0, len(word), 1)]

        mb = [['B', 'B', 'B', 'B', 'B', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], ['B', 'B', 'B', 'B', 'B', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], ['B', 'B', 'B', 'B', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], ['B', 'B', 'B', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], ['B', 'B', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'W', 'W'], ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'W', 'W', 'W'], ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'W', 'W', 'W', 'W'], ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'W', 'W', 'W', 'W', 'W'], ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'W', 'W', 'W', 'W', 'W']]

        for i in range(len(br)):
            for j in range(len(br[i])):
                if (br[i][j] == 'B'):
                    br[i][j] = 2
                elif (br[i][j] == 'W'):
                    br[i][j] = 1
                else:
                    br[i][j] = 0
        for i in range(len(br)):
            for j in range(len(br[i])):
                if (mb[i][j] == 'B'):
                    mb[i][j] = 2
                elif (mb[i][j] == 'W'):
                    mb[i][j] = 1
                else:
                    mb[i][j] = 0
        a = 'BLACK'
        b = 'WHITE'


        board = [[None] * b_size for _ in range(b_size)]




        for row in range(b_size):
            for col in range(b_size):
                if br[row][col]==1:
                    if (row>10) and (row+col)>=25 and row!=15:
                        element = Tile(1,1,0,row,col)
                    elif (row>10) and (row+col)>25 and row==15:
                        element = Tile(1, 1, 0, row, col)
                    elif (row+col) <= 5 and (row<5) and row!=0:
                        element = Tile(2,1,0,row,col)
                    elif (row+col) < 5 and (row<5) and row==0:
                        element = Tile(2, 1, 0, row, col)
                    else:
                        element = Tile(0,1,0,row,col)
                elif br[row][col]==2:
                    if (row+col) <= 5 and (row<5) and row!=0:
                        element = Tile(2, 2, 0, row, col)
                    elif (row+col) < 5 and (row<5) and row==0:
                        element = Tile(2, 2, 0, row, col)
                    elif (row>10) and (row+col)>=25 and row!=15:
                        element = Tile(1, 2, 0, row, col)
                    elif (row>10) and (row+col)>25 and row==15:
                        element = Tile(1, 2, 0, row, col)
                    else:
                        element = Tile(0,2,0,row,col)
                else:
                    if (row + col) <= 5 and (row < 5) and row!=0:
                        element = Tile(2, 0, 0, row, col)
                    elif (row + col) < 5 and (row < 5) and row==0:
                        element = Tile(2, 0, 0, row, col)
                    elif (row>10) and (row+col)>=25 and row!=15:
                        element = Tile(1,0,0,row,col)
                    elif (row>10) and (row+col)>25 and row==15:
                        element = Tile(1, 0, 0, row, col)
                    else:
                        element = Tile(0,0,0,row,col)
                board[row][col] = element







        self.r_goals = [t for row in board
                        for t in row if t.tile == Tile.T_RED]

        self.g_goals = [t for row in board
                        for t in row if t.tile == Tile.T_GREEN]

        self.b_size = b_size
        self.t_limit = t_limit
        self.c_player = c_player

        self.board = board
        if val[0]=='W':
         self.current_player = Tile.P_GREEN
        else:
         self.current_player = Tile.P_RED
        if self.current_player == Tile.P_RED:
            self.c_player = Tile.P_RED
        else:
            self.c_player = Tile.P_GREEN
        if val[0]=='B':
         self.current_player = Tile.P_RED
        else:
         self.current_player = Tile.P_GREEN
        if self.current_player == Tile.P_RED:
            self.c_player = Tile.P_RED
        else:
            self.c_player = Tile.P_GREEN


        self.selected_tile = None
        self.valid_moves = []
        self.computing = False
        self.total_plies = 0

        self.ply_depth = 2
        self.ab_enabled = True



        if self.c_player == self.current_player:
            self.execute_computer_move()



    def minimax(self, depth, player_to_max, max_time, a=float("-inf"),
                b=float("inf"), maxing=True, prunes=0, boards=0):


        if depth == 0  or time.time() > max_time:
            return self.utility_distance(player_to_max), None, prunes, boards


        best_move = None
        if maxing:
            best_val = float("-inf")

            moves = self.get_next_moves(player_to_max)
        else:
            best_val = float("inf")
            moves = self.get_next_moves((Tile.P_RED
                    if player_to_max == Tile.P_GREEN else Tile.P_GREEN))


        for move in moves:
            for to in move["to"]:


                if time.time() > max_time:
                    return best_val, best_move, prunes, boards


                piece = move["from"].piece
                move["from"].piece = Tile.P_NONE
                to.piece = piece
                boards += 1

                # Recursively call self
                val, _, new_prunes, new_boards = self.minimax(depth - 1,
                    player_to_max, max_time, a, b, not maxing, prunes, boards)
                prunes = new_prunes
                boards = new_boards

                # Move the piece back
                to.piece = Tile.P_NONE
                move["from"].piece = piece

                if maxing and val > best_val:
                    best_val = val
                    best_move = (move["from"].loc, to.loc)
                    a = max(a, val)

                if not maxing and val < best_val:
                    best_val = val
                    best_move = (move["from"].loc, to.loc)
                    b = min(b, val)

                if self.ab_enabled and b <= a:
                    return best_val, best_move, prunes + 1, boards

        return best_val, best_move, prunes, boards

    def execute_computer_move(self):


        current_turn = (self.total_plies // 2) + 1

        sys.stdout.flush()


        self.computing = True

        max_time = time.time() + self.t_limit


        start = time.time()

        _, move, prunes, boards = self.minimax(self.ply_depth,
            self.c_player, max_time)
        end = time.time()


        curr_tile = self.board[move[0][0]][move[0][1]]
        to_tile = self.board[move[1][0]][move[1][1]]
        path = self.get_moves_at_tilee(curr_tile, to_tile,  self.c_player)

        move_from = self.board[move[0][0]][move[0][1]]
        move_to = self.board[move[1][0]][move[1][1]]
        from_tile = move_from
        to_tile = move_to
        c = to_tile.loc[0]
        d = to_tile.loc[1]
        e = from_tile.loc[0]
        f = from_tile.loc[1]
        a = abs(c - e)
        b = abs(d - f)



        self.move_piece(move_from, move_to)


        dup_move_from = self.board[move[0][0]][move[0][1]]
        dup_move_to = self.board[move[1][0]][move[1][1]]
        result = []
        if a >= 2 or b >= 2:
            while True:
                for element in path:
                    if (element[0] == dup_move_to):

                        result.insert(0, (element[0].loc[1], element[0].loc[0]))

                        result.insert(0,(element[1].loc[1], element[1].loc[0]))
                        res = element[1]
                        if res == dup_move_from:
                            break
                        else:
                            dup_move_to = element[1]
                            break

                if res == dup_move_from:
                    break
                else:
                    continue
            z = open("/Users/asharanikota/PycharmProjects/homework/output.txt", "w+")
            ct=0
            for element in result:
                if ct%2==0:
                    line = ["J "]
                    for lines in line:
                        z.write(lines)
                    z.write("{0},{1} ".format(element[0], element[1]))
                else:
                    z.write("{0},{1}".format(element[0], element[1]))
                    z.write('\n')
                ct=ct+1




        self.computing = False
        print()

    def get_next_moves(self, player):


        moves = []  # All possible moves
        flag=0
        if val[0]=='W'  and st[0]=='S':

            for i in range(11, 16):
                if i == 11:
                    for j in range(14, 16):
                        curr_tile = self.board[i][j]
                        if curr_tile.piece == player:
                            flag = 1
                            break
                elif i == 12:
                    for j in range(13, 14):
                        curr_tile = self.board[i][j]
                        if curr_tile.piece == player:
                            flag = 1
                            break
                elif i == 13:
                    for j in range(12, 13):
                        curr_tile = self.board[i][j]
                        if curr_tile.piece == player:
                            flag = 1
                            break
                elif i == 14:
                    for j in range(11, 12):
                        curr_tile = self.board[i][j]
                        if curr_tile.piece == player:
                            flag = 1
                            break
                elif i == 15:
                    for j in range(11, 12):
                        curr_tile = self.board[i][j]
                        if curr_tile.piece == player:
                            flag = 1
                            break
                if flag == 1:
                    break
        if val[0] == 'B' and st[0] == 'S':

            for i in range(4, -1, -1):
                if i == 0:
                    for j in range(4, 3, -1):
                        curr_tile = self.board[i][j]
                        if curr_tile.piece == player:
                            flag = 1
                            break
                elif i == 1:
                    for j in range(4, 3, -1):
                        curr_tile = self.board[i][j]
                        if curr_tile.piece == player:
                            flag = 1
                            break
                elif i == 2:
                    for j in range(3, 2, -1):
                        curr_tile = self.board[i][j]
                        if curr_tile.piece == player:
                            flag = 1
                            break
                elif i == 3:
                    for j in range(2, 1, -1):
                        curr_tile = self.board[i][j]
                        if curr_tile.piece == player:
                            flag = 1
                            break
                elif i == 4:
                    for j in range(1, -1, -1):
                        curr_tile = self.board[i][j]
                        if curr_tile.piece == player:
                            flag = 1
                            break
                if flag == 1:
                    break
        if val[0] == 'W' and st[0] == 'S' and flag==0:

            for i in range(11, 16):
                if i == 11:
                    for j in range(14, 16):
                        curr_tile = self.board[i][j]
                        if curr_tile.piece == player:
                            flag = 1
                            break
                elif i == 12:
                    for j in range(13, 16):
                        curr_tile = self.board[i][j]
                        if curr_tile.piece == player:
                            flag = 1
                            break
                elif i == 13:
                    for j in range(12, 16):
                        curr_tile = self.board[i][j]
                        if curr_tile.piece == player:
                            flag = 1
                            break
                elif i == 14:
                    for j in range(11, 16):
                        curr_tile = self.board[i][j]
                        if curr_tile.piece == player:
                            flag = 1
                            break
                elif i == 15:
                    for j in range(11, 16):
                        curr_tile = self.board[i][j]
                        if curr_tile.piece == player:
                            flag = 1
                            break
                if flag == 1:
                    break
        if val[0] == 'B' and st[0]=='S' and flag==0:

            for i in range(4, -1, -1):
                if i == 0:
                    for j in range(4, -1, -1):
                        curr_tile = self.board[i][j]
                        if curr_tile.piece == player:
                            flag = 1
                            break
                elif i == 1:
                    for j in range(4, -1, -1):
                        curr_tile = self.board[i][j]
                        if curr_tile.piece == player:
                            flag = 1
                            break
                elif i == 2:
                    for j in range(3, -1, -1):
                        curr_tile = self.board[i][j]
                        if curr_tile.piece == player:
                            flag = 1
                            break
                elif i == 3:
                    for j in range(2, -1, -1):
                        curr_tile = self.board[i][j]
                        if curr_tile.piece == player:
                            flag = 1
                            break
                elif i == 4:
                    for j in range(1, -1, -1):
                        curr_tile = self.board[i][j]
                        if curr_tile.piece == player:
                            print("trouble")
                            flag = 1
                            break
                if flag == 1:
                    break
        if val[0]=='W'  and st[0]=='G' and self.board[14][12].piece==player:

            for i in range(11, 16):
                if i == 11:
                    for j in range(14, 16):
                        curr_tile = self.board[i][j]
                        if curr_tile.piece == player:
                            flag = 1
                            break
                elif i == 12:
                    for j in range(13, 14):
                        curr_tile = self.board[i][j]
                        if curr_tile.piece == player:
                            flag = 1
                            break
                elif i == 13:
                    for j in range(12, 13):
                        curr_tile = self.board[i][j]
                        if curr_tile.piece == player:
                            flag = 1
                            break
                elif i == 14:
                    for j in range(11, 12):
                        curr_tile = self.board[i][j]
                        if curr_tile.piece == player:
                            flag = 1
                            break
                elif i == 15:
                    for j in range(11, 12):
                        curr_tile = self.board[i][j]
                        if curr_tile.piece == player:
                            flag = 1
                            break
                if flag == 1:
                    break
        if val[0] == 'W' and st[0]=='G' and (self.board[11][14].piece==player or self.board[11][15].piece==player or self.board[12][13].piece==player or self.board[12][14].piece==player or self.board[12][15].piece==player or self.board[13][12].piece==player or self.board[13][13].piece==player or self.board[13][14].piece==player or self.board[13][15].piece==player or self.board[14][11].piece==player or self.board[14][12].piece==player or self.board[14][13].piece==player or self.board[14][14].piece==player or  self.board[14][15].piece==player or self.board[15][11].piece==player or self.board[15][12].piece==player or self.board[15][13].piece==player or self.board[15][14].piece==player or self.board[15][15].piece==player) and self.board[14][12].piece!=player:

            for i in range(11, 16):
                if i == 11:
                    for j in range(14, 16):
                        curr_tile = self.board[i][j]
                        if curr_tile.piece == player:
                            flag = 1
                            break
                elif i == 12:
                    for j in range(13, 16):
                        curr_tile = self.board[i][j]
                        if curr_tile.piece == player:
                            flag = 1
                            break
                elif i == 13:
                    for j in range(12, 16):
                        curr_tile = self.board[i][j]
                        if curr_tile.piece == player:
                            flag = 1
                            break
                elif i == 14:
                    for j in range(11, 16):
                        curr_tile = self.board[i][j]
                        if curr_tile.piece == player:
                            flag = 1
                            break
                elif i == 15:
                    for j in range(11, 16):
                        curr_tile = self.board[i][j]
                        if curr_tile.piece == player:
                            flag = 1
                            break
                if flag == 1:
                    break
        if val[0] == 'B' and st[0] == 'G' and self.board[1][3].piece == player:

            for i in range(4, -1, -1):
                if i == 0:
                    for j in range(4, 3, -1):
                        curr_tile = self.board[i][j]
                        if curr_tile.piece == player:
                            flag = 1
                            break
                elif i == 1:
                    for j in range(4, 3, -1):
                        curr_tile = self.board[i][j]
                        if curr_tile.piece == player:
                            flag = 1
                            break
                elif i == 2:
                    for j in range(3, 2, -1):
                        curr_tile = self.board[i][j]
                        if curr_tile.piece == player:
                            flag = 1
                            break
                elif i == 3:
                    for j in range(2, 1, -1):
                        curr_tile = self.board[i][j]
                        if curr_tile.piece == player:
                            flag = 1
                            break
                elif i == 4:
                    for j in range(1, -1, -1):
                        curr_tile = self.board[i][j]
                        if curr_tile.piece == player:
                            flag = 1
                            break
                if flag == 1:
                    break
        if val[0] == 'B' and st[0] == 'G' and (
                self.board[4][0].piece == player or self.board[2][2].piece == player or self.board[1][
            1].piece == player or self.board[0][0].piece == player) and self.board[1][3].piece != player:

            for i in range(4, -1, -1):
                if i == 0:
                    for j in range(4, -1, -1):
                        curr_tile = self.board[i][j]
                        if curr_tile.piece == player:
                            flag = 1
                            break
                elif i == 1:
                    for j in range(4, -1, -1):
                        curr_tile = self.board[i][j]
                        if curr_tile.piece == player:
                            flag = 1
                            break
                elif i == 2:
                    for j in range(3, -1, -1):
                        curr_tile = self.board[i][j]
                        if curr_tile.piece == player:
                            flag = 1
                            break
                elif i == 3:
                    for j in range(2, -1, -1):
                        curr_tile = self.board[i][j]
                        if curr_tile.piece == player:
                            flag = 1
                            break
                elif i == 4:
                    for j in range(1, -1, -1):
                        curr_tile = self.board[i][j]
                        if curr_tile.piece == player:
                            flag = 1
                            break
                if flag == 1:
                    break

        # if val[0] == 'B' and  st[0]=='G' and self.board[2][1].piece==player:
        #
        #     for i in range(4, -1, -1):
        #         if i == 0:
        #             for j in range(4, 3, -1):
        #                 curr_tile = self.board[i][j]
        #                 if curr_tile.piece == player:
        #                     flag = 1
        #                     break
        #         elif i == 1:
        #             for j in range(4, 3, -1):
        #                 curr_tile = self.board[i][j]
        #                 if curr_tile.piece == player:
        #                     flag = 1
        #                     break
        #         elif i == 2:
        #             for j in range(3, 2, -1):
        #                 curr_tile = self.board[i][j]
        #                 if curr_tile.piece == player:
        #                     flag = 1
        #                     break
        #         elif i == 3:
        #             for j in range(2, 1, -1):
        #                 curr_tile = self.board[i][j]
        #                 if curr_tile.piece == player:
        #                     flag = 1
        #                     break
        #         elif i == 4:
        #             for j in range(1, -1, -1):
        #                 curr_tile = self.board[i][j]
        #                 if curr_tile.piece == player:
        #
        #                     flag = 1
        #                     break
        #         if flag == 1:
        #             break
        # if val[0] == 'B' and  st[0]=='G'  and (self.board[4][1].piece==player or self.board[4][0].piece==player or self.board[3][2].piece==player or self.board[3][1].piece==player or self.board[3][0].piece==player or self.board[2][3].piece==player or self.board[2][2].piece==player or self.board[2][1].piece==player or self.board[2][0].piece==player or self.board[1][4].piece==player or self.board[1][3].piece==player or self.board[1][2].piece==player or self.board[1][1].piece==player or  self.board[1][0].piece==player or self.board[0][4].piece==player or self.board[0][3].piece==player or self.board[0][2].piece==player or self.board[0][1].piece==player or self.board[0][0].piece==player) and self.board[2][1].piece!=player:
        #
        #     for i in range(4, -1 ,-1):
        #         if i == 0:
        #             for j in range(4, -1, -1):
        #                 curr_tile = self.board[i][j]
        #                 if curr_tile.piece == player:
        #                     flag = 1
        #                     break
        #         elif i == 1:
        #             for j in range(4, -1, -1):
        #                 curr_tile = self.board[i][j]
        #                 if curr_tile.piece == player:
        #                     flag = 1
        #                     break
        #         elif i == 2:
        #             for j in range(3, -1, -1):
        #                 curr_tile = self.board[i][j]
        #                 if curr_tile.piece == player:
        #                     flag = 1
        #                     break
        #         elif i == 3:
        #             for j in range(2, -1, -1):
        #                 curr_tile = self.board[i][j]
        #                 if curr_tile.piece == player:
        #                     flag = 1
        #                     break
        #         elif i == 4:
        #             for j in range(1, -1, -1):
        #                 curr_tile = self.board[i][j]
        #                 if curr_tile.piece == player:
        #
        #                     flag = 1
        #                     break
        #         if flag == 1:
        #             break
        if flag==1:
            move = {
                "from": curr_tile,
                "to": self.get_moves_at_tile(curr_tile, player)
            }
            moves.append(move)
        if flag == 0:
            for col in range(self.b_size):
                for row in range(self.b_size):

                    curr_tile = self.board[row][col]

                        # Skip board elements that are not the current player
                    if curr_tile.piece != player:
                        continue
                    move = {
                            "from": curr_tile,
                            "to": self.get_moves_at_tile(curr_tile, player)
                        }
                    moves.append(move)

        return moves


    def get_moves_at_tile(self, tile,   player, moves=None, adj=True):
        if moves is None:
            moves = []

        row = tile.loc[0]
        col = tile.loc[1]


        valid_tiles = [Tile.T_NONE, Tile.T_GREEN, Tile.T_RED]
        if tile.tile != player:
            valid_tiles.remove(player)
        if tile.tile != Tile.T_NONE and tile.tile != player:
            valid_tiles.remove(Tile.T_NONE)


        for col_delta in range(-1, 2):
            for row_delta in range(-1, 2):



                new_row = row + row_delta
                new_col = col + col_delta


                if ((new_row == row and new_col == col) or
                    new_row < 0 or new_col < 0 or
                    new_row >= self.b_size or new_col >= self.b_size):
                    continue


                new_tile = self.board[new_row][new_col]
                if new_tile.tile not in valid_tiles:
                    continue

                if new_tile.piece == Tile.P_NONE:
                    if adj:
                        moves.append(new_tile)
                    continue


                new_row = new_row + row_delta
                new_col = new_col + col_delta


                if (new_row < 0 or new_col < 0 or
                    new_row >= self.b_size or new_col >= self.b_size):
                    continue


                new_tile = self.board[new_row][new_col]
                if new_tile in moves or (new_tile.tile not in valid_tiles):
                    continue

                if new_tile.piece == Tile.P_NONE:
                    moves.insert(0, new_tile)
                    self.get_moves_at_tile(new_tile, player, moves, False)



        return moves

    def get_moves_at_tilee(self, tile, to_tile, player, moves=None, adj=True, pre=[]):
        if moves is None:
            moves = []

        row = tile.loc[0]
        col = tile.loc[1]


        valid_tiles = [Tile.T_NONE, Tile.T_GREEN, Tile.T_RED]
        if tile.tile != player:
            valid_tiles.remove(player)
        if tile.tile != Tile.T_NONE and tile.tile != player:
            valid_tiles.remove(Tile.T_NONE)


        for col_delta in range(-1, 2):
            for row_delta in range(-1, 2):



                new_row = row + row_delta
                new_col = col + col_delta


                if ((new_row == row and new_col == col) or
                    new_row < 0 or new_col < 0 or
                    new_row >= self.b_size or new_col >= self.b_size):
                    continue


                new_tile = self.board[new_row][new_col]
                if new_tile.tile not in valid_tiles:
                    continue

                if new_tile.piece == Tile.P_NONE:
                    if adj:
                       moves.append(new_tile)

                    continue


                new_row = new_row + row_delta
                new_col = new_col + col_delta


                if (new_row < 0 or new_col < 0 or
                    new_row >= self.b_size or new_col >= self.b_size):
                    continue


                new_tile = self.board[new_row][new_col]
                if new_tile in moves or (new_tile.tile not in valid_tiles):
                    continue

                if new_tile.piece == Tile.P_NONE:
                    moves.insert(0,new_tile)
                    pre.insert(0,(new_tile,tile))
                    self.get_moves_at_tilee(new_tile,to_tile, player, moves, False,pre)

        return pre

    def move_piece(self, from_tile, to_tile):


        to_tile.piece = from_tile.piece
        from_tile.piece = Tile.P_NONE


        to_tile.outline = Tile.O_MOVED
        from_tile.outline = Tile.O_MOVED

        self.total_plies += 1
        c = to_tile.loc[0]
        d = to_tile.loc[1]
        e = from_tile.loc[0]
        f = from_tile.loc[1]
        a = abs(c-e)
        b = abs(d-f)
        if a<=1 and b<=1:
            z = open("/Users/asharanikota/PycharmProjects/homework/output.txt", "w+")
            line = ["E "]
            for lines in line:
                z.write(lines)
            z.write("{0},{1} ".format(from_tile.loc[1],from_tile.loc[0]))
            z.write("{0},{1}".format(to_tile.loc[1],to_tile.loc[0]))






    def utility_distance(self, player):

        def point_distance(p0, p1):
            return math.sqrt((p1[0] - p0[0])**2 + (p1[1] - p0[1])**2)

        value = 0

        for col in range(self.b_size):
            for row in range(self.b_size):

                tile = self.board[row][col]

                if tile.piece == Tile.P_GREEN:
                    distances = [point_distance(tile.loc, g.loc) for g in
                                 self.r_goals if g.piece != Tile.P_GREEN]
                    value -= max(distances) if len(distances) else -50

                elif tile.piece == Tile.P_RED:
                    distances = [point_distance(tile.loc, g.loc) for g in
                                 self.g_goals if g.piece != Tile.P_RED]
                    value += max(distances) if len(distances) else -50

        if player == Tile.P_RED:
            value *= -1

        return value


if __name__ == "__main__":

    halma = Halma()