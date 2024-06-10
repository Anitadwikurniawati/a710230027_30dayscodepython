class AlatMusik:
    def play_suara(self):
        raise NotImplementedError("Subclass harus mengimplementasikan metode abstrak ini")

class Gitar(AlatMusik):
    def play_suara(self):
        return "Gitar play: Twing twing!"

class Piano(AlatMusik):
    def play_suara(self):
        return "Piano play: Ting ting ting!"

class Drum(AlatMusik):
    def play_suara(self):
        return "Drum play: Dum dum dum!"

def play_alat_musik(alat_musik):
    print(alat_musik.play_suara())

gitar = Gitar()
piano = Piano()
drum = Drum()

play_alat_musik(gitar)   
play_alat_musik(piano)  
play_alat_musik(drum)   