class Player:
    name = 'Player'

    def __init__(self): #self는 파라미터이기 때문에 다른걸로 바꿔도 됨 ex)(my)
        self.x = 100

    def where(self):
        print(self.x)

player = Player()
player.where()

print(Player.name)
print(player.name)

# Player.where() self 필요함
Player.where(player) #이렇게