import unittest
from app import PCBuilder

class TestPCBuilder(unittest.TestCase):

    def test_default_pc(self):
        builder = PCBuilder()
        result = builder.build()
        self.assertEqual(result, "PC with Intel i3, Integrated, 8GB")

    def test_gaming_pc(self):
        builder = PCBuilder()
        result = builder.set_cpu("Ryzen 5").set_gpu("RTX 4060").set_ram("16GB").build()
        self.assertEqual(result, "PC with Ryzen 5, RTX 4060, 16GB")

    def test_ram_upgrade_only(self):
        builder = PCBuilder()
        result = builder.set_ram("32GB").build()
        self.assertEqual(result, "PC with Intel i3, Integrated, 32GB")

if __name__ == '__main__':
    unittest.main()