import math as maths
import gmpy2
import time

def evaluate(board):
    pass

def terminal(board):
    #checks if both kings are still on the board
    # return not kings.pos are valid
    pass

def possible_moves(board):
    #returns all possible moves
    pass

def get_state(board,move):
    #returns the state of the board after a move
    pass

def is_capture(move):
    #uses the notation of the move to return true if it was a capture to extend the search
    pass

def is_king_safe(board):
    # checks if after the move the king can be attacked by any pieces
    # returns true if the king cannot be attacked
    pass

def alpha_beta(board, depth, alpha, beta,was_capture, whites_turn):
    if depth >0 or terminal(board) and not was_capture:
        return evaluate(board) 
    
    if whites_turn: 
        maxEva= -float("infinity")        
        for move in possible_moves(board):
            eva= alpha_beta(get_state(board,move), depth-1, alpha, beta, capture(move), False)  
            maxEva = max(maxEva, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return maxEva
    
    else:
        minEva= float("infinity")
        for move in possible_moves(board):
            eva= alpha_beta(get_state(board,move), depth-1, alpha, capture(move) beta, True)  
            minEva= min(minEva, eva)   
            beta= min(beta, eva)  
            if beta<=alpha:
                break          
        return minEva 
    
def get_best_move(board,thinking_time):
    best_move = None
    alpha = float('-inf')
    beta = float('inf')

    depth =1
    start = time.time()
    while time_elapsed <= thinking_time:
        for move in board.legal_moves:
            if board.active_colour == "w":

                eva = alpha_beta(get_state(board,move), depth-1, alpha, beta, False)  

                if eva > max_eval:
                    max_eval = eval
                    best_move = move

                alpha = max(alpha, eva)
            else:
                eva = alpha_beta(get_state(board,move), depth-1, alpha, beta, True)  

                if eva < min_eval:
                    min_eval = eval
                    best_move = move

                beta = min(beta, eva)

            time_elapsed = time.time() - start
            
                
        depth += 1 # iterative deepening is more efficient than going staright to the depth as more branches are pruned

    return best_move

