import unittest
from app import biz


class TestEnergy(unittest.TestCase):
    def test_get_energy(self):
        sn = '0110358190820021'
        dt = '2020-08-24'

        energy_save = biz.energy.equipment_energy_save(sn, dt)
        print(dict(energy_save))

        self.assertEqual(1, 1)
        pass
