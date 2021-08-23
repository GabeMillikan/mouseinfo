import mouse
import mss, numpy

print("mouse position (x, y) | color on screen at position (r, g, b)")
with mss.mss() as sct:
    while True:
        (x, y) = mouse.get_position()
        [r,g,b] = list(numpy.array(sct.grab({"left": x, "top": y, "width": 1, "height": 1}))[0][0])[:3]
        print(f"({x:5}, {y:5}) | ({r:3}, {g:3}, {b:3})", end="\r")