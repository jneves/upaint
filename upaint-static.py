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

def pos(acc_value):
    acc_stages = [-500, -250, 250, 500]

    pos = 0
    for limit in acc_stages:
        if acc_value > limit:
            pos += 1

    return pos

screen = Screen()
pointer = Pointer()

while True:
    sleep(25)
    pointer.y = pos(accelerometer.get_x())
    pointer.x = pos(accelerometer.get_y())
    if button_a.was_pressed():
        screen.toggle(pointer.x, pointer.y)
    if button_b.was_pressed():
        screen.publish()
    screen.display(pointer)
    sleep(25)
