ticks = 0
obstacles: List[game.LedSprite] = []
dinosaur: List[game.LedSprite] = []

frame = 100

def move(moves : List[int], frames : List[int], up : bool):
    n = len(frames)
    for i in range(n):
        t = frames[i]
        dy = moves[i]
        if up:
            for piece in dinosaur:
                piece.change(LedSpriteProperty.Y, -dy)
        else:
            dinosaur[0].change(LedSpriteProperty.Y, -dy)
        basic.pause(frame*t)

def jump():
    frames = [1,13,1,0]
    moves   = [1,1,-1,-1]
    move(moves,frames,True)
input.on_button_pressed(Button.A, jump)


def duck():
    frames = [15,0]
    moves   = [-1,1]
    move(moves,frames,False)
input.on_button_pressed(Button.B, duck)


obstacles = []
dinosaur = [game.create_sprite(0, 3), game.create_sprite(0, 4)]
dinosaur[0].set(LedSpriteProperty.BLINK, 300)
dinosaur[1].set(LedSpriteProperty.BLINK, 300)

modulo = 3

passed = False

def on_forever():
    global ticks, modulo, frame,passed
    while len(obstacles) > 0 and obstacles[0].get(LedSpriteProperty.X) == 0:
        obstacles.remove_at(0).delete()
        passed = True
    if passed:
        passed = not passed
        game.set_score(game.score()+1)
    for obstacle in obstacles:
        obstacle.change(LedSpriteProperty.X, -1)

    if ticks % modulo == 0:
        ticks = 0
        modulo = 3 + randint(-1,1)
        obstacletype = randint(0, 1)
        for i in range(2):
            obstacles.append(game.create_sprite(4, 2+i+obstacletype))
    for obstacle3 in obstacles:
        for piece in dinosaur:
            if obstacle3.get(LedSpriteProperty.X) == piece.get(LedSpriteProperty.X) and obstacle3.get(LedSpriteProperty.Y) == piece.get(LedSpriteProperty.Y):
                game.game_over()
    ticks += 1
    basic.pause(5*frame)
    if (game.score() + 1) % 10 == 0:
        frame = (frame * 8) // 10
basic.forever(on_forever)