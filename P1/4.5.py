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


def smoothstep(t):
    """Гладкая интерполяционная функция"""
    return t * t * (3 - 2 * t)

def lerp(a, b, t):
    """Линейная интерполяция"""
    return a + (b - a) * t


def val_noise( x, y ) :
    """Интерполяционный шум (Value Noise)"""
    x0 = math.floor( x )
    y0 = math.floor( y )
    x1 = x0 + 1
    y1 = y0 + 1

    # Получаем значения шума в четырех ближайших целых координатах
    v00 = noise( x0, y0 )
    v10 = noise( x1, y0 )
    v01 = noise( x0, y1 )
    v11 = noise( x1, y1 )

    # Интерполяция
    sx = smoothstep( x - x0 )
    sy = smoothstep( y - y0 )

    i1 = lerp( v00, v10, sx )
    i2 = lerp( v01, v11, sx )

    return lerp( i1, i2, sy )

def func(x, y):
    noise_value = val_noise(x * 5, y * 5)
    return (noise_value, noise_value, noise_value)

root = tk.Tk()
label = tk.Label(root)
img = tk.PhotoImage(data=pyshader(func, 256, 256)).zoom(2,2)
label.pack()
label.config(image=img)
root.mainloop()
