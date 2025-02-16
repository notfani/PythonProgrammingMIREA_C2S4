import math
import tkinter as tk

def pyshader(func, w, h):
    scr = bytearray((0, 0, 0) * w * h)
    for y in range(h):
        for x in range(w):
            p = (w * y + x) * 3
            scr[p:p + 3] = [max(min(int(c * 255), 255), 0)
                            for c in func(x / w, y / h)]
    return bytes('P6\n%d %d\n255\n' % (w, h), 'ascii') + scr

def noise(x, y):
     n = math.sin(x * 19.191919 + y * 78.7878787) * 12345.678912
     return n - math.floor(n)


def func(x, y):
    n = noise(x, y)
    return (n, n, n)


root = tk.Tk()
label = tk.Label(root)
img = tk.PhotoImage(data=pyshader(func, 256, 256)).zoom(2, 2)
label.pack()
label.config(image=img)
root.mainloop()
