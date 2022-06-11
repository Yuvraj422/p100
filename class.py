class Car():
    def __init__(self,model,color,company,speedlimit):
        self.color=color
        self.company=company
        self.speedlimit=speedlimit
        self.model=model

    def start(self):
        print('started')

    def stop(self):
        print('stopped')

    def acceleration(self):
        print('accelerated')

    def change_gear(self,geartype):
        print('gear changed')
        
        
    audi=Car('a6','black','Audi','150')
    audi.color
         


#audi.start()
#audi.stop()
