#taken from https://makecode.microbit.org/projects/crashy-bird
ticks = 0
emptyObstacleY = 0
obstacles: List[game.LedSprite] = []
index = 0
bird: game.LedSprite = None

def on_button_pressed_a():
    bird.change(LedSpriteProperty.Y, -1)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    bird.change(LedSpriteProperty.Y, 1)
input.on_button_pressed(Button.B, on_button_pressed_b)

index = 0
obstacles = []
bird = game.create_sprite(0, 2)
bird.set(LedSpriteProperty.BLINK, 300)

def on_forever():
    global emptyObstacleY, ticks
    while len(obstacles) > 0 and obstacles[0].get(LedSpriteProperty.X) == 0:
        obstacles.remove_at(0).delete()
    for obstacle2 in obstacles:
        obstacle2.change(LedSpriteProperty.X, -1)
    if ticks % 3 == 0:
        emptyObstacleY = randint(0, 4)
        for index2 in range(5):
            if index2 != emptyObstacleY:
                obstacles.append(game.create_sprite(4, index2))
    for obstacle3 in obstacles:
        if obstacle3.get(LedSpriteProperty.X) == bird.get(LedSpriteProperty.X) and obstacle3.get(LedSpriteProperty.Y) == bird.get(LedSpriteProperty.Y):
            game.game_over()
    ticks += 1
    basic.pause(1000)
basic.forever(on_forever)