from microbit import Image, button_a, button_b, display, sleep, accelerometer


class Screen():
    def __init__(self):
        self.array = [[0 for x in range(5)] for x in range(5)]
        self.blink = 0

    def image(self):
        s = ''
        for x in range(5):
            for y in range(5):
                s += str(self.array[x][y])
            s += ':'
        return Image(s)

    def update(self, x, y, intensity=9):
        self.array[x][y] = intensity

    def toggle(self, x, y):
        self.array[x][y] = 9 - self.array[x][y]
        
    def display(self, pointer):
        if self.blink:
            screen.toggle(pointer.x, pointer.y)
        display.show(self.image())
        if self.blink:
            screen.toggle(pointer.x, pointer.y)
            self.blink = 0
        else:
            self.blink = 1

    def publish(self):
        print(self.image())
        

class Pointer():
    def __init__(self):
        self.reset()
    
    def reset(self):
        self.x = 2
        self.y = 2
        
    def move_up(self):
        if not self.x == 0:
            self.x -= 1

    def move_down(self):
        if not self.x == 4:
            self.x += 1

    def move_left(self):
        if not self.y == 0:
            self.y -= 1

    def move_right(self):
        if not self.y == 4:
            self.y += 1
            

screen = Screen()
pointer = Pointer()

while True:
    sleep(25)
    if accelerometer.get_x() < -200:
        pointer.move_left()
    if accelerometer.get_x() > 200:
        pointer.move_right()
    if accelerometer.get_y() < -200:
        pointer.move_up()
    if accelerometer.get_y() > 200:
        pointer.move_down()
    if button_a.was_pressed():
        screen.toggle(pointer.x, pointer.y)
    if button_b.was_pressed():
        screen.publish()
    screen.display(pointer)
    sleep(25)
