#Tic-Tac-Toe
"""
class:player rules facilities
    player:player1 player2
    rules:order_rule judge_rule
    facilities:checkerboard
"""
class Player:
    def name(self):
        playername=input("name:")
        return playername
player1=Player()
print(player1.name())
player2=Player()
print(player2.name())
player1.order="first"
player2.order="second"
class Facilities:
    def xxx(self):
        print(self)
checkerboard=Facilities()
checkerboard.xxx()