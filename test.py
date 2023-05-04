import tkinter as tk

win = tk.Tk()
win.configure(width=400, height=400)
win.wm_title("Hello world!")
win.wait_window()

s = 'Hello'
r = "World"
ss = 10.33
ss = {
    "test": "text",
    "test2": "insert text"
}
# Hello
"""
Hello world
"""
foo = True or False

class Vector2:
    def __init__(self, x: int, y: int) -> None:
        print("Hello world!")
        self.x = x
        self.y = y

myvect = Vector2(10, 15)
print(f"Vector: x={myvect.x}\ty={myvect.y}")

ok = [1,4,7,5,2]