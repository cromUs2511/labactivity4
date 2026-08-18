class PCBuilder:
    def __init__(self):
        self.cpu = "Intel i3"
        self.gpu = "Integrated"
        self.ram = "8GB"

    def set_cpu(self, cpu):
        self.cpu = cpu
        return self

    def set_gpu(self, gpu):
        self.gpu = gpu
        return self

    def set_ram(self, ram):
        self.ram = ram
        return self

    def build(self):
        return f"PC with {self.cpu}, {self.gpu}, {self.ram}"