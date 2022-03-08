from utils import create_root


def draw_tree(canvas, depth, size, x, y):
    if depth == 0:
        return
    x0 = x - size // 2
    y0 = y - size // 2
    x1 = x + size // 2
    y1 = y + size // 2
    canvas.create_line(x0, y0, x0, y1)
    canvas.create_line(x1, y0, x1, y1)
    canvas.create_line(x0, y, x1, y)
    draw_tree(canvas, depth - 1, size // 2, x0, y0)
    draw_tree(canvas, depth - 1, size // 2, x0, y1)
    draw_tree(canvas, depth - 1, size // 2, x1, y0)
    draw_tree(canvas, depth - 1, size // 2, x1, y1)


if __name__ == '__main__':
    depth = int(input().strip())
    root, canvas = create_root(title="Htree")
    draw_tree(canvas, depth, 200, 400, 400)
    root.mainloop()
