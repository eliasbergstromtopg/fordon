import fordon

class personbil:
    
#constructor
def __init__(self, fabrikat, color, bagagevolym):
    self.flakvolym = bagagevolym
    self.fabrikat = fabrikat
    self.color = color 


    #metoder
    def set_flakvolym(slef, bagagevolym):
        slef.flakvolym = bagagevolym

    def get_flakvolym(slef):
        return self.bagagevolym
    
    
    def print_fordon(slef):
        print(self.fabrikat +"färg: "+ self.color +" flakvolym= " + self(self.bagagevolym))
