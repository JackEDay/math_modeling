from const_module import g
import numpy as np

def full_energy_calc(gravity_const):
    m = int(input("Масса:   "))
    h = int(input("Высота:  "))
    v = int(input("Скорость:  "))
    pot_energ = m * h * gravity_const
    kin_energ = (m * v ** 2) / 2
    full_energy = pot_energ + kin_energ
    
    return full_energy

print(full_energy_calc(g))

