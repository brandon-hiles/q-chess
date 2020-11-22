import chess

class Silican(object):

    def __init__(self):
        self.board = chess.Board()

    def open_silican(self):
        self.board.push_san("e4")
        self.board.push_san("c5")
        self.board.push_san("Nf3")
        return self.board

    def closed_silican(self):
        self.board.push_san("e4")
        self.board.push_san("c5")
        self.board.push_san("Nc3")
        return self.board

    def accelerated_dragon(self):
        self.open_silican()
        self.board.push_san("Nc6")
        self.board.push_san("d4")
        self.board.push_san("c5xd4")
        self.board.push_san("Nxd4")
        self.board.push_san("g6")
        return self.board