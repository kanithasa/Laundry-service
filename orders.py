#priority queue for order placement
class node:
    def __init__(self, data=None, pos=None):
            self.data=data
            self.next=pos
class flag:
    def __init__(self, high=None, low=None):
        self.left=high
        self.right=low
        
class orderQ:
    def __init__(self):
        self.point1=flag()
        self.point2=flag()
        self.head=node(pos=self.point1)
        self.end=node(pos=self.point2)
        self.point1.left=self.head
        self.point1.right=self.point2
        self.point2.left=self.point1
        self.point2.right=self.end
        self.highSize=self.lowSize=self.midSize=0
        
    def placeOrder(self, data, priority="low"):
        if (priority=="low"):
            temp=self.point2.right
            self.point2.right=node(data,self.point2)
            temp.next=self.point2.right
            self.lowSize+=1
            
        elif (priority=="high"):
            temp=self.point1.left
            self.point1.left=node(data, self.point1)
            temp.next=self.point1.left
            self.highSize+=1
            
        elif (priority=="mid"):
            temp=self.point2.left
            self.point2.left=node(data, self.point2)
            if (self.midSize==0):
                self.point1.right=self.point2.left
            else:
                temp.next=self.point2.left
            self.midSize+=1
        
        else:
            raise Exception("invalid value passed for 'priority' parameter!")
            
    def closeOrder(self, priority="low"):
        closedOrder=None
        if (priority=="low"):
            if (self.lowSize==0):
                raise Exception("Low priority order list is Empty!")
            else:
                closedOrder=self.end.next.data
                self.end.next=self.end.next.next
                if (self.end.next==self.point2):
                    self.point2.right=self.end
                self.lowSize-=1
                
        elif (priority=="high"):
            if (self.highSize==0):
                raise Exception("Hight priority order list is Emptpy!")
            else:
                closedOrder=self.head.next.data
                self.head.next=self.head.next.next
                if (self.head.next==self.point1):
                    self.point1.left=self.head
                self.highSize-=1
                
        elif (priority=="mid"):
            if (self.midSize==0):
                raise Exception("Mid priority order list is Emptpy!")
            else:
                closedOrder=self.point1.right.data
                self.point1.right=self.point1.right.next
                if (self.point1.right==self.point2):
                    self.point2.left=self.point1
                self.midSize-=1
                
        else:
            raise Exception("Invalide value passed for 'priority' parameter!")
            
        return closedOrder
            
    def show(self, priority="low"):
        if (priority=="low"):
            cnt=self.end
            while (cnt.next!=self.point2):
                print(cnt.next.data, end=" ")
                cnt=cnt.next
            print("Size=", self.lowSize)
            
        elif (priority=="high"):
            cnt=self.head
            while (cnt.next!=self.point1):
                print(cnt.next.data, end=" ")
                cnt=cnt.next
            print("Size=", self.highSize)
            
        elif (priority=="mid"):
            cnt=self.point1.right
            while (cnt.next!=self.point2):
                print(cnt.data, end=" ")
                cnt=cnt.next
            print(cnt.data, end=" ")
            print("Size=", self.midSize)
            
demo=orderQ()
demo.placeOrder(1, "low")
demo.placeOrder(2, "low")
demo.placeOrder(3, "low")
demo.show("low")
print()
demo.placeOrder(5, "mid")
demo.placeOrder(6, "mid")
demo.placeOrder(7, "mid")
demo.show("mid")
print()
demo.placeOrder(10, "high")
demo.placeOrder(12, "high")
demo.placeOrder(6, "high")
demo.show("high")
print()
print(f"{demo.closeOrder('low')} low Order closed!")
demo.show("low")
print()
print(f"{demo.closeOrder('mid')} mid Order closed!")
demo.show("mid")
print()
print(f"{demo.closeOrder('high')} high Order closed!")
demo.show("high")
print()






























