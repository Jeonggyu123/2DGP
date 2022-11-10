from pico2d import *

# Game object class here

class Grass:
    def __init__(self):
        self.x, self.y = 0, 90
        self.frame = 0
        self.image = load_image('grass.png')

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += 5
    def draw(self):
        self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)
    pass



grass = Grass() # Grass 라는 클래스로부터, grass 객체를 생성한다



def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

# initialization code

# game main loop code

# finalization code