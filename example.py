import randColor
import tkinter as tk
import random

class buttonPosition:
    def __init__(self, x, y):
        self.x = x
        self.y = y

pos = buttonPosition(0.3, 0.3)

def fun(canvas, button):
    changeBg(canvas)
    moveButton(button)

def changeBg(canvas):
    canvas.configure(bg=randColor.randColor())

def moveButton(button):
    """resets button current pos and the places it random"""

    button.place(relx=(0-pos.x), rely=(0-pos.y))

    # update Obj
    pos.x = random.randint(0, 88) / 100
    pos.y = random.randint(0, 95) / 100

    # place button on new location
    button.place(relx=pos.x, rely=pos.y)

def main():
    """
    creates a simple root with canvas and a button
    when button is pressed the color of the background changes
    the button also moves to a random position
    :return:
    """

    root = tk.Tk()

    canvas = tk.Canvas(root, height=500, width=500)
    canvas.pack()

    button = tk.Button(canvas ,text="Click me!", command=lambda :fun(canvas, button))
    button.place(relx=pos.x, rely=pos.y)

    root.mainloop()


if __name__ == '__main__':
    main()