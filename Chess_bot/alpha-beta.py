import math as maths
import gmpy2
import Chess_bot.Transposition_table as Transposition_table
import time

class Alpha_Beta:
    def __init__(self):
        self.transposition = Transposition_table.Transpoisition()
        
        
    def evaluate(self, board):
        # checks if board has already been visited
        # if not applies {eval function}
        # then saves board and its eval to transposition
        pass

    def terminal(self, board):
        return (board.white_king & board.black_can_take) or (board.black_king & board.white_can_take)
        

    def possible_moves(self, board):
        #returns all possible moves
        pass

    def get_state(self, board,move):
        #returns the state of the board after a move
        pass

    def is_capture(self, move):
        #uses the notation of the move to return true if it was a capture to extend the search
        pass

    def is_king_safe(self,board):
        # checks if after the move the king can be attacked by any pieces
        # returns true if the king cannot be attacked
        pass
    
    def search_all_captures(self,alpha, beta):
        pass
    
    def alpha_beta(self,board, depth, alpha, beta,was_capture, whites_turn):
        if depth >0 or self.terminal(board) and not was_capture:
            return self.evaluate(board) 
        
        if whites_turn: 
            maxEva= -float("infinity")        
            for move in self.possible_moves(board):
                eva= self.alpha_beta(self.get_state(board,move), depth-1, alpha, beta, self.is_capture(move), False)  
                maxEva = max(maxEva, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
            return maxEva
        
        else:
            minEva= float("infinity")
            for move in self.possible_moves(board):
                eva= self.alpha_beta(self.get_state(board,move), depth-1, alpha, beta, self.is_capture(move) , True)  
                minEva= min(minEva, eva)   
                beta= min(beta, eva)  
                if beta<=alpha:
                    break          
            return minEva 
        
    def get_best_move(self, board,thinking_time):
        # uses the best move from the previous search to start the next search depth
        # depth increases with each iteration until time has been exceeded
        
        best_move = None
        alpha = float('-inf')
        beta = float('inf')

        depth =1
        start = time.time()
        while time_elapsed <= thinking_time:
            for move in board.legal_moves:
                if board.active_colour == "w":

                    eva = self.alpha_beta(self.get_state(board,move), depth-1, alpha, beta, False)  

                    if eva > max_eval:
                        max_eval = eval
                        best_move = move

                    alpha = max(alpha, eva)
                else:
                    eva = self.alpha_beta(self.get_state(board,move), depth-1, alpha, beta, True)  

                    if eva < min_eval:
                        min_eval = eval
                        best_move = move

                    beta = min(beta, eva)

                time_elapsed = time.time() - start
                
                    
            depth += 1 # iterative deepening is more efficient than going staright to the depth as more branches are pruned

        return best_move

