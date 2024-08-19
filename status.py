import time,threading

class Status(object):
    def __init__(self):
        pass
    def one(self):
        #connecting to tkinter
        print("Your  order has been placed!")
    
    def two(self):
        print("Your order has been picked up!")
        
    def three(self):
        print( "Your clothes are transferred to respective service points for washing")
        
    def four(self):
        print("Your clothes are being washed!")
        
    def five(self):
        print("Your clothes are being ironed with care!")
        
    def six(self):
        print("Your clothes are being accumulated")
        
    def seven(self):
        print("Clothes are ready!")
        
    def eight(self):
        print("Your clothes are delivered and ready to be used!")

    def _24Hour(self):
        threading.Timer(2,self.one).start()
        time.sleep(4)
        threading.Timer(1,self.two).start()
        time.sleep(4)
        threading.Timer(2,self.three).start()
        time.sleep(4)
        threading.Timer(2,self.four).start()
        time.sleep(4)
        threading.Timer(2,self.five).start()
        time.sleep(4)
        threading.Timer(2,self.six).start()
        time.sleep(4)
        threading.Timer(2,self.seven).start()
        time.sleep(4)
        threading.Timer(2,self.eight).start()
    
    def _2days(self):
        threading.Timer(2,self.one).start()
        time.sleep(4)
        threading.Timer(1,self.two).start()
        time.sleep(4)
        threading.Timer(2,self.three).start()
        time.sleep(4)
        threading.Timer(2,self.four).start()
        time.sleep(4)
        threading.Timer(2,self.five).start()
        time.sleep(4)
        threading.Timer(2,self.six).start()
        time.sleep(4)
        threading.Timer(2,self.seven).start()
        time.sleep(4)
        threading.Timer(2,self.eight).start()
    
    def _3days(self):
        threading.Timer(2,self.one).start()
        time.sleep(4)
        threading.Timer(1,self.two).start()
        time.sleep(4)
        threading.Timer(2,self.three).start()
        time.sleep(4)
        threading.Timer(2,self.four).start()
        time.sleep(4)
        threading.Timer(2,self.five).start()
        time.sleep(4)
        threading.Timer(2,self.six).start()
        time.sleep(4)
        threading.Timer(2,self.seven).start()
        time.sleep(4)
        threading.Timer(2,self.eight).start()
    
m=Status()
m._24Hour()
