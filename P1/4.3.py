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

def func(x, y):
    cx, cy = 0.5, 0.5
    ex, ey = 0.6, 0.25
    radius = 0.4
    eye_radius = 0.05
    angle_start = 35
    angle_end = 325
    dist = math.sqrt((x - cx) ** 2 + (y - cy) ** 2)
    if dist < radius:
        eye = math.sqrt((x - ex) ** 2 + (y - ey) ** 2)
        angle = math.degrees(math.atan2(y - cy, x - cx))
        if angle < 0:
            angle += 360
        if angle >= angle_start and angle <= angle_end and eye > eye_radius:
            return (1, 1, 0)
        else:
            return (0, 0, 0)
    else:
        return (0, 0, 0)


root = tk.Tk()
label = tk.Label(root)
img = tk.PhotoImage(data=pyshader(func, 256, 256)).zoom(2, 2)
label.pack()
label.config(image=img)
root.mainloop()
