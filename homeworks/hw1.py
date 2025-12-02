
import emoji
class ChessFigure:

    def __init__(self, name, nick, value=" "):
        self.name = name
        self.nick = nick
        self.value = value
        self.black = True

    def first(self):
        return f"1. {self.name} e4 {self.name} e5"
    def second(self):
        return f"2. {self.name} c4 {self.name} c5"
    def third(self):
        self.black = "knight"
        return f"3. {self.name} f3 {self.black} c6"
    def fourth(self):
        return f"4. {self.name} f7 CHECKMATE Game over"


pawn = ChessFigure("Pawn", "P", 1)
knight = ChessFigure("Knight", "N", 3)
bishop = ChessFigure("Bishop", "B", 3)
rook = ChessFigure("Rook", "R", 5)
quen = ChessFigure("Quen", "Q", 9)
king = ChessFigure("King", "K")

print(pawn.first())
print(bishop.second())
print(quen.third())
print(quen.fourth(), emoji.emojize(':trophy:'))