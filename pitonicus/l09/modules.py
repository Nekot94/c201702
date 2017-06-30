import random
from math import sin, sqrt
# from cmath import *
from cmath import sqrt as csqrt
import qeq
import wave
import pyglet

best_men = ["Рукижат","Магомед"]
print(random.choice(best_men))
print(sin(3))
print(sqrt(4))
print(csqrt(-1))
# wave.open("aaaaa.wav", mode=None)

song = pyglet.media.load('aaaaa.ogg')
song.play()
pyglet.app.run()
a, b, c = input("Введите коэффиценты a, b, c ").split(" ")
a, b, c = int(a), int(b), int(c)
print(qeq.solve(a, b, c))