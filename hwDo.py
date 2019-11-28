# Python Standard Library imports
import sys
import time
import math

# Custom module imports
from board import Board
from tile import Tile
from MainTiles import MainTiles
class Halma():


    def __init__(self, b_size=16, t_limit=60, c_player=Tile.P_RED):
        br = []
        f = open("/Users/asharanikota/PycharmProjects/homework/input.txt", "r")
        global st
        st = f.readline()
        print(st)
        global val
        global k
        k = 0
        val = f.readline()
        val = val.strip()
        print(val)
        t_limit = float(f.readline())
        t_limit = 60
        for i in range(16):
            br.append(f.readline().split())
        for i in range(16):
            word = br[i][0]
            br[i] = [word[i:i + 1] for i in range(0, len(word), 1)]
        print(br)
        mb = [['B', 'B', 'B', 'B', 'B', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], ['B', 'B', 'B', 'B', 'B', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], ['B', 'B', 'B', 'B', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], ['B', 'B', 'B', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], ['B', 'B', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'W', 'W'], ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'W', 'W', 'W'], ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'W', 'W', 'W', 'W'], ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'W', 'W', 'W', 'W', 'W'], ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'W', 'W', 'W', 'W', 'W']]

        for i in range(len(br)):
            for j in range(len(br[i])):
                if (br[i][j] == 'B'):
                    br[i][j] = 2
                elif (br[i][j] == 'W'):
                    br[i][j] = 1
                else:
                    br[i][j] = 0

        a = 'BLACK'
        b = 'WHITE'

        # Create initial board
        board = [[None] * b_size for _ in range(b_size)]

        # for row in range(b_size):
        #     for col in range(b_size):
        #         if mb[row][col]==1:
        #             element = Tile(1, 0, 0, row, col)
        #         elif mb[row][col]==2:
        #             element = Tile(2, 0, 0, row, col)
        #         else:
        #             element = Tile(0, 0, 0, row, col)
        #         board[row][col] = element


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
        # for row in range(b_size):
        #     for col in range(b_size):
        #         if (row>10) and (row+col)>=25:
        #             if board[row][col].tile.tile==0:
        #                 board[row][col].tile.tile = Tile.P_GREEN
        #         elif (row+col) <= 5 and (row<5):
        #             if board[row][col].piece == 0:
        #                 board[row][col].tile = Tile.P_RED






        self.r_goals = [t for row in board
                        for t in row if t.tile == Tile.T_RED]
        print(self.r_goals)
        self.g_goals = [t for row in board
                        for t in row if t.tile == Tile.T_GREEN]
        print(self.g_goals)

        # Save member variables
        self.b_size = b_size
        self.t_limit = t_limit
        self.c_player = c_player
        self.board_view = Board(board)
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

        # self.r_goals = [t for row in board
        #                 for t in row if t.tile == Tile.T_RED]
        # print(self.r_goals)
        # self.g_goals = [t for row in board
        #                 for t in row if t.tile == Tile.T_GREEN]
        # print(self.g_goals)
        self.board_view.set_status_color("#E50000" if
            self.current_player == Tile.P_RED else "#007F00")

        if self.c_player == self.current_player:
            self.execute_computer_move()

        self.board_view.add_click_handler(self.tile_clicked)
        self.board_view.draw_tiles(board=self.board)  # Refresh the board

        # Print initial program info
        print("Halma Solver Basic Information")
        print("==============================")
        print("AI opponent enabled:", "no" if self.c_player is None else "yes")
        print("A-B pruning enabled:", "yes" if self.ab_enabled else "no")
        print("Turn time limit:", self.t_limit)
        print("Max ply depth:", self.ply_depth)
        print()

        self.board_view.mainloop()  # Begin tkinter main loop

    def tile_clicked(self, row, col):

        if self.computing:  # Block clicks while computing
            return

        new_tile = self.board[row][col]

        # If we are selecting a friendly piece
        if new_tile.piece == self.current_player:

            self.outline_tiles(None)  # Reset outlines

            # Outline the new and valid move tiles
            new_tile.outline = Tile.O_MOVED
            self.valid_moves = self.get_moves_at_tile(new_tile,
                self.current_player)
            self.outline_tiles(self.valid_moves)

            # Update status and save the new tile
            self.board_view.set_status("Tile `" + str(new_tile) + "` selected")
            self.selected_tile = new_tile

            self.board_view.draw_tiles(board=self.board)  # Refresh the board

        # If we already had a piece selected and we are moving a piece
        elif self.selected_tile and new_tile in self.valid_moves:

            self.outline_tiles(None)  # Reset outlines
            self.move_piece(self.selected_tile, new_tile)  # Move the piece

            # Update status and reset tracking variables
            self.selected_tile = None
            self.valid_moves = []
            self.current_player = (Tile.P_RED
                if self.current_player == Tile.P_GREEN else Tile.P_GREEN)

            self.board_view.draw_tiles(board=self.board)  # Refresh the board

            # If there is a winner to the game
            winner = self.find_winner()
            if winner:
                self.board_view.set_status("The " + ("green"
                    if winner == Tile.P_GREEN else "red") + " player has won!")
                self.current_player = None

            elif self.c_player is not None:
                self.execute_computer_move()

        else:
            self.board_view.set_status("Invalid move attempted")

    def minimax(self, depth, player_to_max, max_time, a=float("-inf"),
                b=float("inf"), maxing=True, prunes=0, boards=0):
        flag = 1

        # Bottomed out base case
        if depth == 0 or self.find_winner() or time.time() > max_time:
            return self.utility_distance(player_to_max), None, prunes, boards

        # Setup initial variables and find moves
        best_move = None
        if maxing:
            best_val = float("-inf")

            moves = self.get_next_moves(player_to_max)
        else:
            best_val = float("inf")
            moves = self.get_next_moves((Tile.P_RED
                    if player_to_max == Tile.P_GREEN else Tile.P_GREEN))

        # For each move
        for move in moves:
            for to in move["to"]:

                # Bail out when we're out of time
                if time.time() > max_time:
                    return best_val, best_move, prunes, boards

                # Move piece to the move outlined
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

        # Print out search information
        current_turn = (self.total_plies // 2) + 1
        print("Turn", current_turn, "Computation")
        print("=================" + ("=" * len(str(current_turn))))
        print("Executing search ...", end=" ")
        sys.stdout.flush()

        # self.board_view.set_status("Computing next move...")
        self.computing = True
        self.board_view.update()
        max_time = time.time() + self.t_limit

        # Execute minimax search
        start = time.time()

        _, move, prunes, boards = self.minimax(self.ply_depth,
            self.c_player, max_time)
        end = time.time()

        # Print search result stats
        print("complete")
        print("Time to compute:", round(end - start, 4))
        print("Total boards generated:", boards)
        print("Total prune events:", prunes)

        # Move the resulting piece
        self.outline_tiles(None)  # Reset outlines
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
        print(move_from)
        print(move_to)
        print(path)


        self.move_piece(move_from, move_to)

        self.board_view.draw_tiles(board=self.board)  # Refresh the board

        dup_move_from = self.board[move[0][0]][move[0][1]]
        dup_move_to = self.board[move[1][0]][move[1][1]]
        result = []
        if a >= 2 or b >= 2:
            while True:
                for element in path:
                    if (element[0] == dup_move_to):
                        # print("{0},{1} ".format(element[0].loc[1], element[0].loc[0]))
                        result.insert(0, (element[0].loc[1], element[0].loc[0]))
                        # print("{0},{1}".format(element[1].loc[1], element[1].loc[0]))
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


        print(result)



        winner = self.find_winner()
        if winner:
            self.board_view.set_status("The " + ("green"
                if winner == Tile.P_GREEN else "red") + " player has won!")
            self.board_view.set_status_color("#212121")
            self.current_player = None
            self.current_player = None

            print()
            print("Final Stats")
            print("===========")
            print("Final winner:", "green"
                if winner == Tile.P_GREEN else "red")
            print("Total # of plies:", self.total_plies)

        else:  # Toggle the current player
            self.current_player = (Tile.P_RED
                if self.current_player == Tile.P_GREEN else Tile.P_GREEN)

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


        if val[0]=='W' and st[0]=='G' and  (self.board[11][14].piece==player or self.board[11][15].piece==player or self.board[12][13].piece==player or self.board[12][14].piece==player or self.board[12][15].piece==player or self.board[13][12].piece==player or self.board[13][13].piece==player or self.board[13][14].piece==player or self.board[13][15].piece==player or self.board[14][11].piece==player or self.board[14][12].piece==player or self.board[14][13].piece==player or self.board[14][14].piece==player or  self.board[14][15].piece==player or self.board[15][11].piece==player or self.board[15][12].piece==player or self.board[15][13].piece==player or self.board[15][14].piece==player or self.board[15][15].piece==player):

            if self.board[12][15].piece==player:
                curr_tile = self.board[12][15]
                flag = 1
            elif self.board[13][14].piece==player:
                curr_tile = self.board[13][14]
                flag = 1
            elif self.board[14][13].piece==player:
                curr_tile = self.board[14][13]
                flag=1
            elif self.board[15][12].piece==player:
                curr_tile = self.board[15][12]
                flag=1
            elif self.board[14][15].piece==player:
                curr_tile = self.board[14][15]
                flag=1
            elif self.board[15][14].piece==player:
                curr_tile = self.board[15][14]
                flag=1
            elif self.board[11][14].piece==player:
                curr_tile = self.board[11][14]
                flag=1
            elif self.board[12][13].piece==player:
                curr_tile = self.board[12][13]
                flag=1
            elif self.board[13][12].piece==player:
                curr_tile = self.board[13][12]
                flag=1
            elif self.board[14][11].piece==player:
                curr_tile = self.board[14][11]
                flag=1
            elif self.board[15][11].piece==player:
                curr_tile = self.board[15][11]
                flag=1
            elif self.board[13][15].piece==player:
                curr_tile = self.board[13][15]
                flag=1
            elif self.board[14][14].piece==player:
                curr_tile = self.board[14][14]
                flag=1
            elif self.board[15][13].piece==player:
                curr_tile = self.board[15][13]
                flag=1
            elif self.board[11][15].piece==player:
                curr_tile = self.board[11][15]
                flag=1
            elif self.board[12][14].piece==player:
                curr_tile = self.board[12][14]
                flag=1
            elif self.board[13][13].piece==player:
                curr_tile = self.board[13][13]
                flag=1
            elif self.board[14][12].piece==player:
                curr_tile = self.board[14][12]
                flag=1

            elif self.board[15][15].piece==player:
                curr_tile = self.board[15][15]
                flag=1


        if val[0] == 'B' and st[0] == 'G' and (self.board[4][1].piece==player or self.board[4][0].piece==player or self.board[3][2].piece==player or self.board[3][1].piece==player or self.board[3][0].piece==player or self.board[2][3].piece==player or self.board[2][2].piece==player or self.board[2][1].piece==player or self.board[2][0].piece==player or self.board[1][4].piece==player or self.board[1][3].piece==player or self.board[1][2].piece==player or self.board[1][1].piece==player or  self.board[1][0].piece==player or self.board[0][4].piece==player or self.board[0][3].piece==player or self.board[0][2].piece==player or self.board[0][1].piece==player or self.board[0][0].piece==player):

            if self.board[3][0].piece==player:
                curr_tile = self.board[3][0]
                flag = 1
            elif self.board[2][1].piece==player:
                curr_tile = self.board[2][1]
                flag = 1
            elif self.board[1][2].piece==player:
                curr_tile = self.board[1][2]
                flag=1
            elif self.board[0][3].piece==player:
                curr_tile = self.board[0][3]
                flag=1
            elif self.board[1][0].piece==player:
                curr_tile = self.board[1][0]
                flag=1
            elif self.board[0][1].piece==player:
                curr_tile = self.board[0][1]
                flag=1
            elif self.board[4][1].piece==player:
                curr_tile = self.board[4][1]
                flag=1
            elif self.board[3][2].piece==player:
                curr_tile = self.board[3][2]
                flag=1
            elif self.board[2][3].piece==player:
                curr_tile = self.board[2][3]
                flag=1
            elif self.board[1][4].piece==player:
                curr_tile = self.board[1][4]
                flag=1
            elif self.board[0][4].piece==player:
                curr_tile = self.board[0][4]
                flag=1
            elif self.board[2][0].piece==player:
                curr_tile = self.board[2][0]
                flag=1
            elif self.board[1][1].piece==player:
                curr_tile = self.board[1][1]
                flag=1
            elif self.board[0][2].piece==player:
                curr_tile = self.board[0][2]
                flag=1
            elif self.board[4][0].piece==player:
                curr_tile = self.board[4][0]
                flag=1
            elif self.board[3][1].piece==player:
                curr_tile = self.board[3][1]
                flag=1
            elif self.board[2][2].piece==player:
                curr_tile = self.board[2][2]
                flag=1
            elif self.board[1][3].piece==player:
                curr_tile = self.board[1][3]
                flag=1

            elif self.board[0][0].piece==player:
                curr_tile = self.board[0][0]
                flag=1


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

        # List of valid tile types to move to
        valid_tiles = [Tile.T_NONE, Tile.T_GREEN, Tile.T_RED]
        if tile.tile != player:
            valid_tiles.remove(player)  # Moving back into your own goal
        if tile.tile != Tile.T_NONE and tile.tile != player:
            valid_tiles.remove(Tile.T_NONE)  # Moving out of the enemy's goal

        # Find and save immediately adjacent moves
        for col_delta in range(-1, 2):
            for row_delta in range(-1, 2):

                # Check adjacent tiles

                new_row = row + row_delta
                new_col = col + col_delta

                # Skip checking degenerate values
                if ((new_row == row and new_col == col) or
                    new_row < 0 or new_col < 0 or
                    new_row >= self.b_size or new_col >= self.b_size):
                    continue

                # Handle moves out of/in to goals
                new_tile = self.board[new_row][new_col]
                if new_tile.tile not in valid_tiles:
                    continue

                if new_tile.piece == Tile.P_NONE:
                    if adj:  # Don't consider adjacent on subsequent calls
                        moves.append(new_tile)
                    continue

                # Check jump tiles
                new_row = new_row + row_delta
                new_col = new_col + col_delta

                # Skip checking degenerate values
                if (new_row < 0 or new_col < 0 or
                    new_row >= self.b_size or new_col >= self.b_size):
                    continue

                # Handle returning moves and moves out of/in to goals
                new_tile = self.board[new_row][new_col]
                if new_tile in moves or (new_tile.tile not in valid_tiles):
                    continue

                if new_tile.piece == Tile.P_NONE:
                    moves.insert(0, new_tile)  # Prioritize jumps
                    self.get_moves_at_tile(new_tile, player, moves, False)



        return moves

    def get_moves_at_tilee(self, tile, to_tile, player, moves=None, adj=True, pre=[]):
        if moves is None:
            moves = []

        row = tile.loc[0]
        col = tile.loc[1]

        # List of valid tile types to move to
        valid_tiles = [Tile.T_NONE, Tile.T_GREEN, Tile.T_RED]
        if tile.tile != player:
            valid_tiles.remove(player)  # Moving back into your own goal
        if tile.tile != Tile.T_NONE and tile.tile != player:
            valid_tiles.remove(Tile.T_NONE)  # Moving out of the enemy's goal

        # Find and save immediately adjacent moves
        for col_delta in range(-1, 2):
            for row_delta in range(-1, 2):

                # Check adjacent tiles

                new_row = row + row_delta
                new_col = col + col_delta

                # Skip checking degenerate values
                if ((new_row == row and new_col == col) or
                    new_row < 0 or new_col < 0 or
                    new_row >= self.b_size or new_col >= self.b_size):
                    continue

                # Handle moves out of/in to goals
                new_tile = self.board[new_row][new_col]
                if new_tile.tile not in valid_tiles:
                    continue

                if new_tile.piece == Tile.P_NONE:
                    if adj:
                       moves.append(new_tile)
                       #pre.insert(0,(new_tile,tile))
                    continue

                # Check jump tiles
                new_row = new_row + row_delta
                new_col = new_col + col_delta

                # Skip checking degenerate values
                if (new_row < 0 or new_col < 0 or
                    new_row >= self.b_size or new_col >= self.b_size):
                    continue

                # Handle returning moves and moves out of/in to goals
                new_tile = self.board[new_row][new_col]
                if new_tile in moves or (new_tile.tile not in valid_tiles):
                    continue

                if new_tile.piece == Tile.P_NONE:
                    moves.insert(0,new_tile)
                    pre.insert(0,(new_tile,tile))
                    self.get_moves_at_tilee(new_tile,to_tile, player, moves, False,pre)

        return pre

    def move_piece(self, from_tile, to_tile):

        # Handle trying to move a non-existant piece and moving into a piece
        if from_tile.piece == Tile.P_NONE or to_tile.piece != Tile.P_NONE:
            self.board_view.set_status("Invalid move")
            return

        # Move piece
        to_tile.piece = from_tile.piece
        from_tile.piece = Tile.P_NONE

        # Update outline
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




        self.board_view.set_status_color("#007F00" if
            self.current_player == Tile.P_RED else "#E50000")
        self.board_view.set_status("Piece moved from `" + str(from_tile) +
            "` to `" + str(to_tile) + "`, " + ("green's" if
            self.current_player == Tile.P_RED else "red's") + " turn...")

    def find_winner(self):

        if all(g.piece == Tile.P_GREEN for g in self.r_goals):
            return Tile.P_GREEN
        elif all(g.piece == Tile.P_RED for g in self.g_goals):
            return Tile.P_RED
        else:
            return None

    def outline_tiles(self, tiles=[], outline_type=Tile.O_SELECT):

        if tiles is None:
            tiles = [j for i in self.board for j in i]
            outline_type = Tile.O_NONE

        for tile in tiles:
            tile.outline = outline_type

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