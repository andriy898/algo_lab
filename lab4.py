class Benzopyla:
    def __init__(self, nazva, potuzhnist_vat, kilkist_obertiv):
        self.nazva = nazva
        self.potuzhnist_vat = potuzhnist_vat
        self.kilkist_obertiv = kilkist_obertiv
    
    def info(self):
        return f"Бензопила {self.nazva}: Потужність - {self.potuzhnist_vat} Вт, Оберти - {self.kilkist_obertiv} об/хв"
    
    shtil = Benzopyla ("Shtil MS 180 " ,1500 , 9000 )
    print = (shtil.info())
