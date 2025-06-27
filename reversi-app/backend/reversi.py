class ReversiGame:
    def __init__(self):
        self.board = [[0 for _ in range(8)] for _ in range(8)]
        self.board[3][3] = self.board[4][4] = 2  # White
        self.board[3][4] = self.board[4][3] = 1  # Black
        self.current_player = 1  # Black starts
        self.game_over = False
        self.winner = None
    
    def get_valid_moves(self, player):
        valid_moves = []
        for row in range(8):
            for col in range(8):
                if self.is_valid_move(row, col, player):
                    valid_moves.append((row, col))
        return valid_moves
    
    def is_valid_move(self, row, col, player):
        if self.board[row][col] != 0:
            return False
        
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        
        for dr, dc in directions:
            if self._check_direction(row, col, dr, dc, player):
                return True
        return False
    
    def _check_direction(self, row, col, dr, dc, player):
        opponent = 3 - player
        r, c = row + dr, col + dc
        
        if not (0 <= r < 8 and 0 <= c < 8) or self.board[r][c] != opponent:
            return False
        
        r += dr
        c += dc
        while 0 <= r < 8 and 0 <= c < 8:
            if self.board[r][c] == 0:
                return False
            if self.board[r][c] == player:
                return True
            r += dr
            c += dc
        return False
    
    def make_move(self, row, col, player):
        if not self.is_valid_move(row, col, player):
            return False
        
        self.board[row][col] = player
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        
        for dr, dc in directions:
            if self._check_direction(row, col, dr, dc, player):
                self._flip_pieces(row, col, dr, dc, player)
        
        self.current_player = 3 - self.current_player
        self._check_game_over()
        return True
    
    def _flip_pieces(self, row, col, dr, dc, player):
        r, c = row + dr, col + dc
        while self.board[r][c] != player:
            self.board[r][c] = player
            r += dr
            c += dc
    
    def _check_game_over(self):
        player1_moves = self.get_valid_moves(1)
        player2_moves = self.get_valid_moves(2)
        
        if not player1_moves and not player2_moves:
            self.game_over = True
            self._determine_winner()
        elif not self.get_valid_moves(self.current_player):
            self.current_player = 3 - self.current_player
            if not self.get_valid_moves(self.current_player):
                self.game_over = True
                self._determine_winner()
    
    def _determine_winner(self):
        black_count = sum(row.count(1) for row in self.board)
        white_count = sum(row.count(2) for row in self.board)
        
        if black_count > white_count:
            self.winner = 1
        elif white_count > black_count:
            self.winner = 2
        else:
            self.winner = 0  # Tie
    
    def get_score(self):
        black_count = sum(row.count(1) for row in self.board)
        white_count = sum(row.count(2) for row in self.board)
        return {'black': black_count, 'white': white_count}
    
    def get_state(self):
        return {
            'board': self.board,
            'current_player': self.current_player,
            'valid_moves': self.get_valid_moves(self.current_player),
            'score': self.get_score(),
            'game_over': self.game_over,
            'winner': self.winner
        }