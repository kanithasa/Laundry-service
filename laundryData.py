import ctypes

class clothData:
    def __init__(self,cloth=None):
        self.clothType={}
        self.cloth=cloth
        
    def getItem(self, clothItem=None):
        if (clothItem==None):
            return self.clothType
        else:
            return self.clothType[self.cloth][1][clothItem]

    def setItem(self, clothType, priceRange, clothItem):
        self.clothType[clothType]=[priceRange, clothItem]
        self.cloth=clothType

    def addItem(self,clothItem, price):
        self.clothType[self.cloth][1][clothItem]=price

    def clothMenu(self):
        return ["Casuals", "Formals", "Ethnic Wear", "Denims", "Footwear & Bags", "House Accessories", "Night Wear"]
        
    def clothtypeMenu(self, cloth):
        lst={"Casuals":["T-shirts:3.0","Shirts|Tops:4.0", "Pants:4.0", "Skirts|Shorts:3.0", "Kurtas:4.0", "Kerchiefs:2.0", "Masks:2.0", "Sarees & Blouses:6.0", "Dresses:5.0", "Jumpsuits:5.0"], 
              "Formals": ["Suits:10.0", "Coats:7.0", "Shirts|Blouses:6.0", "Tie & PocketSquare:3.0", "Sarees:7.0", "Salwar Sets:8.0", "Kurtas:6.0", "Dresses:6.0", "Skirts:5.0"],
              "Ethnic Wear": ["Lehengas:18.0", "Sarees & Blouses:16.0", "Sherwani:15.0", "Gowns:12.0", "Suits:11.0", "Safari Suits:10.0", "Dhotis:8.0"],
              "Denims" : ["Jeans|Pants:7.0", "Jackets:5.0", "Skirts|Shorts:4.0", "Shirts|Tops:4.0", "Jumpsuits:7.0", "Dresses:6.0"],
              "Footwear & Bags" : ["Formal Shoes:15.0", "Socks:3.0", "Casual Footwear:9.0", "School & Hand Bags:13.0", "Travel & Leather Bags:18.0", "Canvas:12.0", "Boots:14.0", "Raincoats:12.0"],
               "House Accessories" : ["Curtains:12.0", "Bedsheets & bedspreads:15.0", "Pillow & Cushion Covers:4.0", "Comforters:18.0", "Quilts:20.0", "Table & Door Mats:5.0", "Towels:4.0", "Vehicle Covers:7.0"],
              "Night Wear" : ["Shorts|Skirts:4.0", "Nighties:5.0", "T-shirts:4.0", "Tracks & Pants:5.0", "Lungi:4.0"]}
        return lst[cloth]
    
    def modeOfWashMenu(self):
        return ['Normal Wash', 'Bleach', "Starch Wash", "Dry Cleaning"]
        
    def dateOfDeliveryMenu(self):
        return ['24 Hrs', '2 Days', '3 Days']
        
    def modeOfPickupMenu(self):
        return ["Pickup", "Self dropping"]
        
    def modeOfDeliveryMenu(self):
        return ["Self Collection", "Door Delivery"]
 
#Adding Clothes
 
def clothSet(index, clothtype, priceRange, clothItem):
    global clothList
    clothList[index]=clothData()
    clothList[index].setItem(clothtype, priceRange, clothItem)

clothtype=["Casuals", "Formals", "Ethnic Wear", "Denims", "Footwear & Bags", "House Accessories", "Night Wear"]
priceRange=["2.0-6.0","3.0-10.0","8.0-18.0","4.0-7.0", "3.0-18.0", "4.0-20.0", "4.0-5.0"]
clothItem=[{"T-shirts":3.0,"Shirts|Tops":4.0, "Pants":4.0, "Skirts|Shorts":3.0, "Kurtas":4.0, "Kerchiefs":2.0, "Masks":2.0, "Sarees & Blouses":6.0, "Dresses":5.0, "Jumpsuits":5.0}, 
{"Suits":10.0, "Coats":7.0, "Shirts|Blouses":6.0, "Tie & PocketSquare":3.0, "Sarees":7.0, "Salwar Sets":8.0, "Kurtas":6.0, "Dresses":6.0, "Skirts":5.0},
{"Lehengas":18.0, "Sarees & Blouses":16.0, "Sherwani":15.0, "Gowns":12.0, "Suits":11.0, "Safari Suits":10.0, "Dhotis":8.0},
{"Jeans|Pants":7.0, "Jackets":5.0, "Skirts|Shorts":4.0, "Shirts|Tops":4.0, "Jumpsuits":7.0, "Dresses":6.0},
{"Formal Shoes":15.0, "Socks":3.0, "Casual Footwear":9.0, "School & Hand Bags":13.0, "Travel & Leather Bags":18.0, "Canvas":12.0, "Boots":14.0, "Raincoats":12.0},
{"Curtains":12.0, "Bedsheets & bedspreads":15.0, "Pillow & Cushion Covers":4.0, "Comforters":18.0, "Quilts":20.0, "Table & Door Mats":5.0, "Towels":4.0, "Vehicle Covers":7.0},
{"Shorts|Skirts":4.0, "Nighties":5.0, "T-shirts":4.0, "Tracks & Pants":5.0, "Lungi":4.0}]

clothList=(ctypes.py_object*len(clothtype))()
for i in range(len(clothtype)):
    clothSet(i, clothtype[i], priceRange[i], clothItem[i])
#Menu to traverse
indexOrder={"Casuals":0, "Formals":1, "Ethnic Wear":2, "Denims":3, "Footwear & Bags":4, "House Accessories":5, "Night Wear":6}

class order:
    def __init__(self):
        self.qty=0
        self.cloth={}
        self.modeOfPickup=None
        self.modeOfDelivery=None
        self.dateOfDelivery=None
        
    def makeorder(self, cloth, clothtype, qty, modeOfWash):
        clothtype=[modeOfWash,clothtype, qty]
        if cloth not in self.cloth:
            self.cloth[cloth]=[clothtype]
        else:
            self.cloth[cloth].append(clothtype)
        self.qty+=qty
        
    def orderDetails(self):
        return (self.qty, self.cloth, self.modeOfPickup, self.modeOfDelivery, self.dateOfDelivery)
    
    def setOrderDetails(self, modeofpickup, modeofdelivery, dateofdelivery):
        self.modeOfPickup=modeofpickup
        self.modeOfDelivery=modeofdelivery
        self.dateOfDelivery=dateofdelivery
    
#Getting order input from user    
class orderMenu:
    def __init__(self):
        self.orderclass=order()
        self.clothdata=clothData()

    def inputOrder(self):
        ch='y'
        while ch=='y':
            cloth=input(self.clothdata.clothMenu())
            clothtype=input(self.clothdata.clothtypeMenu(cloth))
            qty=int(input("Enter quantity:"))
            modeofwash=input(self.clothdata.modeOfWashMenu())
            self.orderclass.makeorder(cloth, clothtype,qty, modeofwash)
            ch=input("Add? y or n")
        modeOfPickup=input(self.clothdata.modeOfPickupMenu())
        modeOfDelivery=input(self.clothdata.modeOfDeliveryMenu())
        dateOfDelivery=input(self.clothdata.dateOfDeliveryMenu())
        self.orderclass.setOrderDetails(modeOfPickup, modeOfDelivery, dateOfDelivery)
        
    def getOrder(self):
        return self.orderclass.orderDetails()
    
class generateSlip:
    def __init__(self, orderDetails,pkg):
        self.clothDetails=orderDetails
        self.package=pkg
        self.priority=None
        #self.email=Customer(sno).getEmail()
        
    def calculate(self):
        sum=0
        
        #Monthly
        if (self.package=="Monthly"):
            qty=5
            for i in (self.clothDetails[1]):
                x=clothList[indexOrder[i]]
                
                #Cloth Constraints
                if (i=="Casuals"):
                    qty=2
                elif(i=="Formals"):
                    qty=2
                elif (i=="Ethnic Wear"):
                    qty=1
                else:
                    qty=0
                    
                #Washing and Clothes Cost    
                for j in self.clothDetails[1][i]:
                    
                    #Washing cost
                    if (j[0]=="Bleach"):
                        sum+=4
                    elif (j[0]=="Starch Wash"):
                        sum+=6
                    elif (j[0]=="Dry Cleaning"):
                        sum+=8
                            
                    #Cloth Cost
                    if (j[2]>qty):
                        sum+=x.getItem(j[1])*(j[2]-qty)
                        qty=0
                    else:
                        qty-=j[2]
                        
        #Occasional                
        elif (self.package=="Occasional"):
            qty=3
            for i in (self.clothDetails[1]):
                x=clothList[indexOrder[i]]
                
                #Cloth Constraints
                if (i=="Casuals"):
                    qty=2
                elif(i=="Formals"):
                    qty=1
                    
                #Washing and Clothes Cost    
                for j in self.clothDetails[1][i]:
                    
                    #Washing cost
                    if (j[0]=="Bleach"):
                        sum+=5
                    elif (j[0]=="Starch Wash"):
                        sum+=6
                    elif (j[0]=="Dry Cleaning"):
                        sum+=9
                            
                    #Cloth Cost
                    if (len(self.clothDetails[1][i])>qty):
                        sum+=x.getItem(j[1])*(j[2]-qty)
                        qty=0
                    else:
                        qty-=j[2]
                        
        #Quaterly                        
        elif (self.package=="Quaterly"):
            qty=9
            for i in (self.clothDetails[1]):
                x=clothList[indexOrder[i]]
                
                #Cloth Constraints
                if (i=="Formals"):
                    qty=2
                elif (i=="Ethnic Wear"):
                    qty=1
                elif (i=="Denims"):
                    qty=2
                elif (i=="House Accessories"):
                    qty=1
                    
                #Washing and Clothes Cost    
                for j in self.clothDetails[1][i]:
                    
                    #Washing cost
                    if (j[0]=="Bleach"):
                        sum+=4
                    elif (j[0]=="Starch Wash"):
                        sum+=5
                    elif (j[0]=="Dry Cleaning"):
                        sum+=7
                            
                    #Cloth Cost
                    if (len(self.clothDetails[1][i])>qty):
                        sum+=x.getItem(j[1])*(j[2]-qty)
                        qty=0
                    else:
                        qty-=j[2]
                        
        #Annual                        
        elif (self.package=="Annual"):
            qty=13
            for i in (self.clothDetails[1]):
                x=clothList[indexOrder[i]]
                
                #Cloth Constraints
                if (i=="Casuals"):
                    qty=4
                elif (i=="Formals"):
                    qty=2
                elif (i=="Ethnic Wear"):
                    qty=2
                elif (i=="Denims"):
                    qty=3
                elif (i=="House Accessories"):
                    qty=2
                    
                #Washing and Clothes Cost    
                for j in self.clothDetails[1][i]:
                    
                    #Washing cost
                    if (j[0]=="Bleach"):
                        sum+=3
                    elif (j[0]=="Starch Wash"):
                        sum+=4.5
                    elif (j[0]=="Dry Cleaning"):
                        sum+=6.5
                            
                    #Cloth Cost
                    if (len(self.clothDetails[1][i])>qty):
                        sum+=x.getItem(j[1])*(j[2]-qty)
                        qty=0
                    else:
                        qty-=j[2]
                        
        #Industrial                        
        elif (self.package=="Industrial"):
            qty=18
            for i in (self.clothDetails[1]):
                x=clothList[indexOrder[i]]
                
                #Cloth Constraints
                if (i=="Casuals"):
                    qty=4
                elif (i=="Formals"):
                    qty=2
                elif (i=="Ethnic Wear"):
                    qty=2
                elif (i=="Denims"):
                    qty=1
                elif (i=="House Accessories"):
                    qty=4
                    
                #Washing and Clothes Cost    
                for j in self.clothDetails[1][i]:
                    
                    #Washing cost
                    if (j[0]=="Bleach"):
                        sum+=2.5
                    elif (j[0]=="Starch Wash"):
                        sum+=3.5
                    elif (j[0]=="Dry Cleaning"):
                        sum+=6
                            
                    #Cloth Cost
                    if (len(self.clothDetails[1][i])>qty):
                        sum+=x.getItem(j[1])*(j[2]-qty)
                        qty=0     
                    else:
                        qty-=j[2]
                    
        #Pickup cost
        if (self.clothDetails[2]=="Pickup"):
            sum+=30
            
        #Delivery cost
        if (self.clothDetails[3]=="Door Delivery"):
            sum+=40
            
        #Delivery date cost
        if (self.clothDetails[4]=="24 Hrs"):
            self.priority='high'
            sum+=70
        elif (self.clothDetails[4]=="2 Days"):
            self.priority='mid'
            sum+=45
        elif (self.clothDetails[4]=="3 Days"):
            self.priority='low'
            sum+=15
        
        return sum

#Order priority

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
    
data=orderMenu()
data.inputOrder()
print(data.getOrder())
x=generateSlip(data.getOrder(), "Monthly")
slip=x.calculate()
orderPlacement=orderQ()
priority=x.priority
cusId=220001
orderPlacement.placeOrder(cusId, priority)
orderPlacement.show(priority)
print("Total Cost=",slip)
    

    
    
    
    