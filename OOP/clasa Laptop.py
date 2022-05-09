clear = lambda: os.system("cls")
class Lapek:
    def __init__(self, cpu, ram=0, gpu="xsraj", price="kosztujący wchuj"):  
        self.setCpu(cpu)
        self.setRam(ram)
        self.gpu = gpu
        self.price = price
    def setCpu(self, cpu):
        if cpu.lower() == "amd" or cpu.lower()=="intel" or cpu.lower()=="arm":
            self.cpu = cpu
        else:
            self.cpu = "nieznany"
    def setRam(self, ram):        
        if type(ram)== str:
            self.ram = "zła wartość ram"
        else:
            self.ram = ram

    def printData(self):
        print(self.cpu, self.ram, self.gpu, self.price)
        
lap1 = Lapek("amd", "66666", "nvidia", "mało")
lap1.printData()
