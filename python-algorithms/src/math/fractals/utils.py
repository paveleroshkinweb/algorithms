from tkinter import *


def create_root(*, title, bg='#fafafa', width=800, height=800):
    root = Tk()
    root['bg'] = bg
    root.title(title)
    root.geometry(f'{width}x{height}')
    canvas = Canvas(root, width=width, height=height)
    canvas.pack()
    return root, canvas