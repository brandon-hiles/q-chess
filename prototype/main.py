from openings.silican import Silican

silican = Silican()
board = silican.accelerated_dragon()
print(len(list(board.legal_moves))) # 42 moves 