from microbit import *

warp = True

class snake():
    def __init__(self):
        self.body = [[2,2]]
        self.dir = 0
        self.length = 1
        self.show()

    def move(self):
        x, y = self.body[0]
        if self.dir == 0:
            x += 1
        elif self.dir == 1:
            y += 1
        elif self.dir == 2:
            x -= 1
        elif self.dir == 3:
            y -= 1
        if warp:
            x %= 5
            y %= 5
        if ([x,y] in self.body[1:-1]) or ( (not warp) and (not(0 <= x <= 4) or not(0 <= y <= 4))):
            return True
        else:
            self.hide()
            self.body.insert(0,[x,y])
            if len(self.body) > self.length:
                self.body.pop()
            self.show()
            return False

    def change_dir(self, counter_clockwise):
        if counter_clockwise:
            self.dir = (self.dir + 3) % 4
        else:
            self.dir = (self.dir + 1) % 4
    
    def hide(self):
        for x,y in self.body:
            display.set_pixel(x,y,0)
    def show(self):
        x, y = self.body[0]
        display.set_pixel(x,y,9)
        for x,y in self.body[1:]:
            display.set_pixel(x,y,3)
    def head(self):
        return self.body[0]
    def lengthen(self):
        self.length += 1


from random import choice

class mela():
    def __init__(self,snake):
        self.x,self.y = self.genera_mela(snake)
        self.show()

    def genera_mela(self,snake):
        used = [True]*25
        for x,y in snake.body:
           used[5*x+y] = False
        possible = choice([i for i,x in enumerate(used) if used[i]])
        return possible // 5, possible % 5

    def show(self):
        display.set_pixel(self.x,self.y,6)

    def pos(self):
        return [self.x,self.y]

player = snake()
apple = mela(player)
play = True
while True:
    while play:
        if button_a.was_pressed():
            player.change_dir(True)
        if button_b.was_pressed():
            player.change_dir(False)
        sleep(300)
        lost = player.move()
        if lost:
            display.scroll(player.length)
            play = False
            display.clear()
            break
        if player.head() == apple.pos():
            apple = mela(player)
            player.lengthen()
    if button_a.was_pressed():
        player = snake()
        apple = mela(player)
        play = True
    if button_b.was_pressed():
        warp = not warp