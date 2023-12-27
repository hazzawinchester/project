import math as maths

def evaluate(board):
    pass

def terminal(board):
    # return true/false if the game is over
    pass

def possible_moves(board):
    #returns all possible moves
    pass

def get_state(board,move):
    #returns the state of the board after a move
    pass

def capture(move):
    #uses the notation of the move to return true if it was a capture to extend the search
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
    
def get_best_move(board,depth):
    best_move = None
    alpha = float('-inf')
    beta = float('inf')

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

    return best_move

