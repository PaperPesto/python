class led:
    """Un esempio di classe per gestire i led gpio del Raspberry Pi 3"""
    def __init__(self, pin = 26):
        self.pin = pin
    
    def printInfo(self):
        print("Led class, pin n.", self.pin)

leddino = led(26)
leddino.printInfo()
