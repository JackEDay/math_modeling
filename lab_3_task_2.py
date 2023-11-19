import numpy
from lab_3_task_1 import g
from lab_3_task_1 import plank as p
from lab_3_task_1 import eler as e
from lab_3_task_1 import boc

b = 30
h = 100
a = 60
t = 200
o = 300
cosa = numpy.cos(a)
tgb = numpy.sin(b)/numpy.cos(b)
tga = numpy.sin(a)/numpy.cos(a)

fir = g * h * tgb**2
sec = 2 * cosa**2 * (1 - tgb * tga)

ans = (fir / sec) ** 0.5
print(ans)

fstMult = (2/(3.14 ** 0.5)) * (p/ (t * boc) ** 1.5)
secMult = e ** (-o / boc * t) * o ** 100

print(fstMult * secMult)