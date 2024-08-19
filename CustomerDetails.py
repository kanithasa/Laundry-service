class Customer:
    def __init__(self, serialno):
        self.__cusname=''
        self.email=''
        self.__cusaddress=''
        self.__cusnumber=0
        self.package=''
        self.__cusid=""
        self.cusno=serialno #accessing through list index
        
    def getDetail(self):
        return (self.__cusid, self.__cusname,self.email,self.__cusnumber,self.__cusaddress, self.package)

    def setItem(self,name,email,number,address,package=None):
        self.__cusname=name
        self.__cusaddress=address
        self.__cusnumber=number
        self.email=email
        
        if package==None:
            package=CustomerPackage()
            package.showpackages()
            print("Choose any one of the following packages")
            print("----------------------------------------")
            self.package=input("Select any one of the five packages shown above:")
        else:
            self.package=package

    def getEmail(self):
        return self.email
    
    def getPackage(self):
        return self.package

    def updateName(self, newname):
        self.__cusname=newname

    def updateNumber(self, newnum):
        self.__cusnumber=newnum
        
    def updateEmail(self, email):
        self.email=email

    def updateAdd(self, newadd):
        self.__cusaddress=newadd

    def updatePackage(self, newpackage):
        self.__package=newpackage
    
    def generateID(self, branch=0, year=str(22)):
        k=self.cusno
        m="{0:04}".format(k)
        self.__cusid=int(str(branch)+str(year)+str(m))
        return self.__cusid
    
class CustomerPackage():
    def __init__(self):
        pass
    
    def showpackages(self):
        print("Occasional Package\n---------------\nNumber of orders:1\nCloth Details: 3\nEstimated Delivery date: 3 days\nPickup Options:Weekly\nPackage Price: Rs.300\nIf suppose the number of clothes exceed than that of the cloth limit of the package, then the overall price would be the sum of the price of package and the prices of the clothes added additionally\n\n")
        print("Monthly Package\n---------------\nNumber of orders:4\nCloth Details: 5\nEstimated Delivery date: 3 days\nPickup Options:Weekly\nPackage Price: Rs.500\nNOTE:\n-----\nIf suppose the number of clothes exceed than that of the cloth limit of the package, then the overall price would be the sum of the price of package and the prices of the clothes added additionally. However,if payment is done on a weekly basis, it would mean that only at the last week of payment,the amount to be paid will be increased\n\n")
        print("Quarterly Package\n---------------\nNumber of orders:10\nCloth Details: 9\nEstimated Delivery date: 2 days\nPickup Options:Weekly\nPackage Price: Rs900\nNOTE:\n-----\nIf suppose the number of clothes exceed than that of the cloth limit of the package, then the overall price would be the sum of the price of package and the prices of the clothes added additionally. However,if payment is done on a weekly basis, it would mean that only at the last week of payment,the amount to be paid will be increased\n\n")
        print("Annual Package\n---------------\nNumber of orders:10\nCloth Details: 13\nEstimated Delivery date: 2 days\nPickup Options:Weekly\nPackage Price: Rs.1200\nNOTE:\n-----\nIf suppose the number of clothes exceed than that of the cloth limit of the package, then the overall price would be the sum of the price of package and the prices of the clothes added additionally. However,if payment is done on a weekly basis, it would mean that only at the last week of payment,the amount to be paid will be increased\n\n")
        print("Industrial Package\n-----------------\nNumber of orders:10\nCloth Details: 18\nEstimated Delivery date: 2 days\nPickup Options:Weekly\nPackage Price: Rs.2800\nNOTE:\n-----\nIf suppose the number of clothes exceed than that of the cloth limit of the package, then the overall price would be the sum of the price of package and the prices of the clothes added additionally. However,if payment is done on a weekly basis, it would mean that only at the last week of payment,the amount to be paid will be increased\n\n")
        #We can include cloth details in this function itself!
    
def createcustomer(yr,name,email,number,address,package=None,serialno=None):
    global arr, idlst
    yrno=(yr%10)-2 #since the year starts from 2022
    if arr[yrno][0]==None:
        serialno=len(arr[yrno])
    else:
        serialno=len(arr[yrno])+1
    m=Customer(serialno)
    m.setItem(name,email,number,address, package)
    cusId=m.generateID(year=yr)
    if arr[yrno][0]==None:
        arr[yrno][0]=(m)
        idlst[yrno][0]=cusId
    else:
        arr[yrno].append(m)
        idlst[yrno].append(cusId)
    
#Arr stores my customer detail object's reference
arr=[[None], [None], [None]]
idlst=[[None], [None], [None]]
createcustomer(22,"abc",'123@gmail.com',  123456789, "104 area", "Annual")
createcustomer(22,"xyz",'456@gmail.com',  123456789, "107 area", "Monthly")
createcustomer(23,"jkl", '789@gmail.com', 123456789, "103 area", "Industrial")
print(idlst)
print(arr[0][0].getDetail(), arr[0][1].getDetail(), arr[1][0].getDetail())

