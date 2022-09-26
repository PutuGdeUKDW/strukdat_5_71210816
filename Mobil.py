class Mobil:
    _merk = None
    _tipe = None
    _kapasitasBBM = None
    _jenisBahanBakar = None

    def __init__(self, merk, tipe):
        self._merk = merk
        self._tipe = tipe
    
    #GETTER
    def getmerk (self):
        return self._merk
    
    def gettipe (self):
        return self._tipe

    def getkapasitasBBM (self):
        return self._kapasitasBBM
    
    def getjenisBB (self):
        return self._jenisBahanBakar
    
    #SETTER

    def setmerk (self,merk):
        self._merk = merk
    
    def settipe (self,tipe):
        self._tipe = tipe

    def setKapasitasBBM (self,kapasitasBBM):
        self._kapasitasBBM = kapasitasBBM
    
    def setJenisBahanBakar (self,jenisBahanBakar):
        self._jenisBahanBakar = jenisBahanBakar
    
    def printInfo(self):
        print("==============INFO==============")
        print("Merk\t\t:",self.getmerk())
        print("Tipe\t\t:",self.gettipe())
        print("Bahan Bakar\t:",self.getjenisBB())
        print("Kapasitas BBM\t:",self.getkapasitasBBM())

    def isiBBM(self,x):
        
        if self.getkapasitasBBM() != None:
            print('Mengisi ', self.getkapasitasBBM(),' Liter')
            print('Total Harga : Rp'+str(self.getkapasitasBBM() * x))
        else:
            print("ERROR! Kapasitas BBM atau Jenis Bahan Bakar belum di inputkan")


if __name__ == "__main__":
    mobil1 = Mobil("Toyota", "Avanza")  
    mobil1.printInfo()

    mobil2 = Mobil("Nissan", "Grand Livina")
    mobil2.setJenisBahanBakar("Bensin")
    mobil2.setKapasitasBBM(20)
    mobil2.printInfo()

    mobil1.isiBBM(14500)
    mobil2.isiBBM(14500)
