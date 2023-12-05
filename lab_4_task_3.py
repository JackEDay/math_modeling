from const_module import g
import numpy as np

def full_energy_calc(gravity_const, vel, h, mass):
    pot_energ = mass * h * gravity_const
    kin_energ = (mass * vel ** 2) / 2
    full_energy = pot_energ + kin_energ
    
    return full_energy

m = 5
h = 10
v = 20

print(full_energy_calc(g, v, h, m))

