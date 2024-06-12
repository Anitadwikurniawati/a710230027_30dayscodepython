class IPhone:
    def __init__(self, model, kapasitas, warna):
        self.model= model
        self.kapasitas = kapasitas
        self.warna = warna

    def deskripsi(self):
        return f"iPhone {self.model} dengan kapasitas {self.kapasitas}GB dan warna {self.warna}"

    def nyalakan(self):
        return f"iPhone {self.model} sedang dinyalakan!"

    def matikan(self):
        return f"iPhone {self.model} dimatikan."
        
iphone1 = IPhone("12 Pro Max", 128, "Pacific Blue")
print(iphone1.deskripsi())  
print(iphone1.nyalakan())  
print(iphone1.matikan())    

iphone2 = IPhone("13", 256, "Midnight")
print(iphone2.deskripsi())  
print(iphone2.nyalakan())   
print(iphone2.matikan())   