import sys
import time
import math

from tile import Tile


class Halma():

    def __init__(self, plank_size=16, t_limit=60, c_player=Tile.P_RED):
        br = []
        f = open("input.txt", "r")
        global st
        st = f.readline()
        # print(st)
        global val
        val = f.readline()
        val = val.strip()

        t_limit = float(f.readline())
        t_limit = 60
        for i in range(16):
            br.append(f.readline().split())
        for i in range(16):
            word = br[i][0]
            br[i] = [word[i:i + 1] for i in range(0, len(word), 1)]

        mb = [['B', 'B', 'B', 'B', 'B', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
              ['B', 'B', 'B', 'B', 'B', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
              ['B', 'B', 'B', 'B', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
              ['B', 'B', 'B', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
              ['B', 'B', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
              ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
              ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
              ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
              ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
              ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
              ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
              ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'W', 'W'],
              ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'W', 'W', 'W'],
              ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'W', 'W', 'W', 'W'],
              ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'W', 'W', 'W', 'W', 'W'],
              ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'W', 'W', 'W', 'W', 'W']]

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

        plank = [[None] * plank_size for _ in range(plank_size)]



        for r in range(plank_size):
            for c in range(plank_size):
                if br[r][c] == 1:
                    if (r > 10) and (r + c) >= 25 and r != 15:
                        ele = Tile(1, 1, 0, r, c)
                    elif (r > 10) and (r + c) > 25 and r == 15:
                        ele = Tile(1, 1, 0, r, c)
                    elif (r + c) <= 5 and (r < 5) and r != 0:
                        ele = Tile(2, 1, 0, r, c)
                    elif (r + c) < 5 and (r < 5) and r == 0:
                        ele = Tile(2, 1, 0, r, c)
                    else:
                        ele = Tile(0, 1, 0, r, c)
                elif br[r][c] == 2:
                    if (r + c) <= 5 and (r < 5) and r != 0:
                        ele = Tile(2, 2, 0, r, c)
                    elif (r + c) < 5 and (r < 5) and r == 0:
                        ele = Tile(2, 2, 0, r, c)
                    elif (r > 10) and (r + c) >= 25 and r != 15:
                        ele = Tile(1, 2, 0, r, c)
                    elif (r > 10) and (r + c) > 25 and r == 15:
                        ele = Tile(1, 2, 0, r, c)
                    else:
                        ele = Tile(0, 2, 0, r, c)
                else:
                    if (r + c) <= 5 and (r < 5) and r != 0:
                        ele = Tile(2, 0, 0, r, c)
                    elif (r + c) < 5 and (r < 5) and r == 0:
                        ele = Tile(2, 0, 0, r, c)
                    elif (r > 10) and (r + c) >= 25 and r != 15:
                        ele = Tile(1, 0, 0, r, c)
                    elif (r > 10) and (r + c) > 25 and r == 15:
                        ele = Tile(1, 0, 0, r, c)
                    else:
                        ele = Tile(0, 0, 0, r, c)
                plank[r][c] = ele

        self.r_goals = [t for r in plank
                        for t in r if t.tile == Tile.T_RED]

        self.g_goals = [t for r in plank
                        for t in r if t.tile == Tile.T_GREEN]

        self.plank_size = plank_size
        self.t_limit = t_limit
        self.c_player = c_player

        self.plank = plank
        if val[0] == 'W':
            self.current_player = Tile.P_GREEN
        else:
            self.current_player = Tile.P_RED
        if self.current_player == Tile.P_RED:
            self.c_player = Tile.P_RED
        else:
            self.c_player = Tile.P_GREEN
        if val[0] == 'B':
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
                b=float("inf"), maxing=True, prunes=0, planks=0):

        if depth == 0 or time.time() > max_time:
            return self.utility_distance(player_to_max), None, prunes, planks

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
                    return best_val, best_move, prunes, planks

                piece = move["from"].piece
                move["from"].piece = Tile.P_NONE
                to.piece = piece
                planks += 1

                val, _, new_prunes, new_planks = self.minimax(depth - 1,
                                                              player_to_max, max_time, a, b, not maxing, prunes, planks)
                prunes = new_prunes
                planks = new_planks

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
                    return best_val, best_move, prunes + 1, planks

        return best_val, best_move, prunes, planks

    def execute_computer_move(self):

        current_turn = (self.total_plies // 2) + 1

        sys.stdout.flush()

        self.computing = True

        max_time = time.time() + self.t_limit

        start = time.time()

        _, move, prunes, planks = self.minimax(self.ply_depth,
                                               self.c_player, max_time)
        end = time.time()

        ct = self.plank[move[0][0]][move[0][1]]
        to_tile = self.plank[move[1][0]][move[1][1]]
        path = self.get_moves_at_tilee(ct, to_tile, self.c_player)

        move_from = self.plank[move[0][0]][move[0][1]]
        move_to = self.plank[move[1][0]][move[1][1]]
        from_tile = move_from
        to_tile = move_to
        c = to_tile.loc[0]
        d = to_tile.loc[1]
        e = from_tile.loc[0]
        f = from_tile.loc[1]
        a = abs(c - e)
        b = abs(d - f)

        self.move_piece(move_from, move_to)

        dup_move_from = self.plank[move[0][0]][move[0][1]]
        dup_move_to = self.plank[move[1][0]][move[1][1]]
        result = []
        if a >= 2 or b >= 2:
            while True:
                for ele in path:
                    if (ele[0] == dup_move_to):

                        result.insert(0, (ele[0].loc[1], ele[0].loc[0]))

                        result.insert(0, (ele[1].loc[1], ele[1].loc[0]))
                        res = ele[1]
                        if res == dup_move_from:
                            break
                        else:
                            dup_move_to = ele[1]
                            break

                if res == dup_move_from:
                    break
                else:
                    continue
            z = open("output.txt", "w+")
            ct = 0
            for ele in result:
                if ct % 2 == 0:
                    line = ["J "]
                    for lines in line:
                        z.write(lines)
                    z.write("{0},{1} ".format(ele[0], ele[1]))
                else:
                    z.write("{0},{1}".format(ele[0], ele[1]))
                    z.write('\n')
                ct = ct + 1

        self.computing = False
        print()

    def get_next_moves(self, player):


        moves = []
        flag=0
        if val[0]=='W'  and st[0]=='S':

            for i in range(11, 16):
                if i == 11:
                    for j in range(14, 16):
                        ct = self.plank[i][j]
                        if ct.piece == player:
                            flag = 1
                            break
                elif i == 12:
                    for j in range(13, 14):
                        ct = self.plank[i][j]
                        if ct.piece == player:
                            flag = 1
                            break
                elif i == 13:
                    for j in range(12, 13):
                        ct = self.plank[i][j]
                        if ct.piece == player:
                            flag = 1
                            break
                elif i == 14:
                    for j in range(11, 12):
                        ct = self.plank[i][j]
                        if ct.piece == player:
                            flag = 1
                            break
                elif i == 15:
                    for j in range(11, 12):
                        ct = self.plank[i][j]
                        if ct.piece == player:
                            flag = 1
                            break
                if flag == 1:
                    break
        if val[0] == 'B' and st[0] == 'S':

            for i in range(4, -1, -1):
                if i == 0:
                    for j in range(4, 3, -1):
                        ct = self.plank[i][j]
                        if ct.piece == player:
                            flag = 1
                            break
                elif i == 1:
                    for j in range(4, 3, -1):
                        ct = self.plank[i][j]
                        if ct.piece == player:
                            flag = 1
                            break
                elif i == 2:
                    for j in range(3, 2, -1):
                        ct = self.plank[i][j]
                        if ct.piece == player:
                            flag = 1
                            break
                elif i == 3:
                    for j in range(2, 1, -1):
                        ct = self.plank[i][j]
                        if ct.piece == player:
                            flag = 1
                            break
                elif i == 4:
                    for j in range(1, -1, -1):
                        ct = self.plank[i][j]
                        if ct.piece == player:
                            flag = 1
                            break
                if flag == 1:
                    break
        if val[0] == 'W' and st[0] == 'S' and flag==0:

            for i in range(11, 16):
                if i == 11:
                    for j in range(14, 16):
                        ct = self.plank[i][j]
                        if ct.piece == player:
                            flag = 1
                            break
                elif i == 12:
                    for j in range(13, 16):
                        ct = self.plank[i][j]
                        if ct.piece == player:
                            flag = 1
                            break
                elif i == 13:
                    for j in range(12, 16):
                        ct = self.plank[i][j]
                        if ct.piece == player:
                            flag = 1
                            break
                elif i == 14:
                    for j in range(11, 16):
                        ct = self.plank[i][j]
                        if ct.piece == player:
                            flag = 1
                            break
                elif i == 15:
                    for j in range(11, 16):
                        ct = self.plank[i][j]
                        if ct.piece == player:
                            flag = 1
                            break
                if flag == 1:
                    break
        if val[0] == 'B' and st[0]=='S' and flag==0:

            for i in range(4, -1, -1):
                if i == 0:
                    for j in range(4, -1, -1):
                        ct = self.plank[i][j]
                        if ct.piece == player:
                            flag = 1
                            break
                elif i == 1:
                    for j in range(4, -1, -1):
                        ct = self.plank[i][j]
                        if ct.piece == player:
                            flag = 1
                            break
                elif i == 2:
                    for j in range(3, -1, -1):
                        ct = self.plank[i][j]
                        if ct.piece == player:
                            flag = 1
                            break
                elif i == 3:
                    for j in range(2, -1, -1):
                        ct = self.plank[i][j]
                        if ct.piece == player:
                            flag = 1
                            break
                elif i == 4:
                    for j in range(1, -1, -1):
                        ct = self.plank[i][j]
                        if ct.piece == player:
                            print("trouble")
                            flag = 1
                            break
                if flag == 1:
                    break


        if val[0]=='W' and st[0]=='G' and  (self.plank[11][14].piece==player or self.plank[11][15].piece==player or self.plank[12][13].piece==player or self.plank[12][14].piece==player or self.plank[12][15].piece==player or self.plank[13][12].piece==player or self.plank[13][13].piece==player or self.plank[13][14].piece==player or self.plank[13][15].piece==player or self.plank[14][11].piece==player or self.plank[14][12].piece==player or self.plank[14][13].piece==player or self.plank[14][14].piece==player or  self.plank[14][15].piece==player or self.plank[15][11].piece==player or self.plank[15][12].piece==player or self.plank[15][13].piece==player or self.plank[15][14].piece==player or self.plank[15][15].piece==player):

            if self.plank[12][15].piece==player:
                ct = self.plank[12][15]
                flag = 1
            elif self.plank[13][14].piece==player:
                ct = self.plank[13][14]
                flag = 1
            elif self.plank[14][13].piece==player:
                ct = self.plank[14][13]
                flag=1
            elif self.plank[15][12].piece==player:
                ct = self.plank[15][12]
                flag=1
            elif self.plank[14][15].piece==player:
                ct = self.plank[14][15]
                flag=1
            elif self.plank[15][14].piece==player:
                ct = self.plank[15][14]
                flag=1
            elif self.plank[11][14].piece==player:
                ct = self.plank[11][14]
                flag=1
            elif self.plank[12][13].piece==player:
                ct = self.plank[12][13]
                flag=1
            elif self.plank[13][12].piece==player:
                ct = self.plank[13][12]
                flag=1
            elif self.plank[14][11].piece==player:
                ct = self.plank[14][11]
                flag=1
            elif self.plank[15][11].piece==player:
                ct = self.plank[15][11]
                flag=1
            elif self.plank[13][15].piece==player:
                ct = self.plank[13][15]
                flag=1
            elif self.plank[14][14].piece==player:
                ct = self.plank[14][14]
                flag=1
            elif self.plank[15][13].piece==player:
                ct = self.plank[15][13]
                flag=1
            elif self.plank[11][15].piece==player:
                ct = self.plank[11][15]
                flag=1
            elif self.plank[12][14].piece==player:
                ct = self.plank[12][14]
                flag=1
            elif self.plank[13][13].piece==player:
                ct = self.plank[13][13]
                flag=1
            elif self.plank[14][12].piece==player:
                ct = self.plank[14][12]
                flag=1

            elif self.plank[15][15].piece==player:
                ct = self.plank[15][15]
                flag=1


        if val[0] == 'B' and st[0] == 'G' and (self.plank[4][1].piece==player or self.plank[4][0].piece==player or self.plank[3][2].piece==player or self.plank[3][1].piece==player or self.plank[3][0].piece==player or self.plank[2][3].piece==player or self.plank[2][2].piece==player or self.plank[2][1].piece==player or self.plank[2][0].piece==player or self.plank[1][4].piece==player or self.plank[1][3].piece==player or self.plank[1][2].piece==player or self.plank[1][1].piece==player or  self.plank[1][0].piece==player or self.plank[0][4].piece==player or self.plank[0][3].piece==player or self.plank[0][2].piece==player or self.plank[0][1].piece==player or self.plank[0][0].piece==player):

            if self.plank[3][0].piece==player:
                ct = self.plank[3][0]
                flag = 1
            elif self.plank[2][1].piece==player:
                ct = self.plank[2][1]
                flag = 1
            elif self.plank[1][2].piece==player:
                ct = self.plank[1][2]
                flag=1
            elif self.plank[0][3].piece==player:
                ct = self.plank[0][3]
                flag=1
            elif self.plank[1][0].piece==player:
                ct = self.plank[1][0]
                flag=1
            elif self.plank[0][1].piece==player:
                ct = self.plank[0][1]
                flag=1
            elif self.plank[4][1].piece==player:
                ct = self.plank[4][1]
                flag=1
            elif self.plank[3][2].piece==player:
                ct = self.plank[3][2]
                flag=1
            elif self.plank[2][3].piece==player:
                ct = self.plank[2][3]
                flag=1
            elif self.plank[1][4].piece==player:
                ct = self.plank[1][4]
                flag=1
            elif self.plank[0][4].piece==player:
                ct = self.plank[0][4]
                flag=1
            elif self.plank[2][0].piece==player:
                ct = self.plank[2][0]
                flag=1
            elif self.plank[1][1].piece==player:
                ct = self.plank[1][1]
                flag=1
            elif self.plank[0][2].piece==player:
                ct = self.plank[0][2]
                flag=1
            elif self.plank[4][0].piece==player:
                ct = self.plank[4][0]
                flag=1
            elif self.plank[3][1].piece==player:
                ct = self.plank[3][1]
                flag=1
            elif self.plank[2][2].piece==player:
                ct = self.plank[2][2]
                flag=1
            elif self.plank[1][3].piece==player:
                ct = self.plank[1][3]
                flag=1

            elif self.plank[0][0].piece==player:
                ct = self.plank[0][0]
                flag=1


        if flag==1:
            move = {
                "from": ct,
                "to": self.get_moves_at_tile(ct, player)
            }
            moves.append(move)
        if flag == 0:
            for c in range(self.plank_size):
                for r in range(self.plank_size):

                    ct = self.plank[r][c]


                    if ct.piece != player:
                        continue
                    move = {
                            "from": ct,
                            "to": self.get_moves_at_tile(ct, player)
                        }
                    moves.append(move)

        return moves

    def get_moves_at_tile(self, tile, player, moves=None, adj=True):
        if moves is None:
            moves = []

        r = tile.loc[0]
        c = tile.loc[1]

        vt = [Tile.T_NONE, Tile.T_GREEN, Tile.T_RED]
        if tile.tile != player:
            vt.remove(player)
        if tile.tile != Tile.T_NONE and tile.tile != player:
            vt.remove(Tile.T_NONE)

        for cd in range(-1, 2):
            for rd in range(-1, 2):

                nr = r + rd
                nc = c + cd

                if ((nr == r and nc == c) or
                        nr < 0 or nc < 0 or
                        nr >= self.plank_size or nc >= self.plank_size):
                    continue

                nt = self.plank[nr][nc]
                if nt.tile not in vt:
                    continue

                if nt.piece == Tile.P_NONE:
                    if adj:
                        moves.append(nt)
                    continue

                nr = nr + rd
                nc = nc + cd

                if (nr < 0 or nc < 0 or
                        nr >= self.plank_size or nc >= self.plank_size):
                    continue

                nt = self.plank[nr][nc]
                if nt in moves or (nt.tile not in vt):
                    continue

                if nt.piece == Tile.P_NONE:
                    moves.insert(0, nt)
                    self.get_moves_at_tile(nt, player, moves, False)

        return moves

    def get_moves_at_tilee(self, tile, to_tile, player, moves=None, adj=True, pre=[]):
        if moves is None:
            moves = []

        r = tile.loc[0]
        c = tile.loc[1]

        vt = [Tile.T_NONE, Tile.T_GREEN, Tile.T_RED]
        if tile.tile != player:
            vt.remove(player)
        if tile.tile != Tile.T_NONE and tile.tile != player:
            vt.remove(Tile.T_NONE)

        for cd in range(-1, 2):
            for rd in range(-1, 2):

                nr = r + rd
                nc = c + cd

                if ((nr == r and nc == c) or
                        nr < 0 or nc < 0 or
                        nr >= self.plank_size or nc >= self.plank_size):
                    continue

                nt = self.plank[nr][nc]
                if nt.tile not in vt:
                    continue

                if nt.piece == Tile.P_NONE:
                    if adj:
                        moves.append(nt)

                    continue

                nr = nr + rd
                nc = nc + cd

                if (nr < 0 or nc < 0 or
                        nr >= self.plank_size or nc >= self.plank_size):
                    continue

                nt = self.plank[nr][nc]
                if nt in moves or (nt.tile not in vt):
                    continue

                if nt.piece == Tile.P_NONE:
                    moves.insert(0, nt)
                    pre.insert(0, (nt, tile))
                    self.get_moves_at_tilee(nt, to_tile, player, moves, False, pre)

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
        a = abs(c - e)
        b = abs(d - f)
        if a <= 1 and b <= 1:
            z = open("output.txt", "w+")
            line = ["E "]
            for lines in line:
                z.write(lines)
            z.write("{0},{1} ".format(from_tile.loc[1], from_tile.loc[0]))
            z.write("{0},{1}".format(to_tile.loc[1], to_tile.loc[0]))

    def utility_distance(self, player):

        def point_distance(p0, p1):
            return math.sqrt((p1[0] - p0[0]) ** 2 + (p1[1] - p0[1]) ** 2)

        value = 0

        for c in range(self.plank_size):
            for r in range(self.plank_size):

                tile = self.plank[r][c]

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