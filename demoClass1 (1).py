class Customer:
    def __init__(self):
        self.__cusname=''
        self.__cusaddress=''
        self.__cusnumber=0
        self.package=''
        self.__serialnumber=""
        
    def getDetail(self):
        return (self.__cusname,self.__cusaddress,self.__cusnumber,self.__package)

    def setItem(self,name,address,number):
        self.__cusname=name
        self.__cusaddress=address
        self.__cusnumber=number
    
    def getlen(self):
        if customer_arr==[]:
            return 0
        else:
            x=0
            for i in customer_arr:
                x+=1
            return x
    
    def choose_a_package(self):
        print("Choose any one of the following packages")
        print("----------------------------------------")
        print("Occasional Order\nMonthly Order\nQuarterly Order\nIndustrial Order\nYearly Order\n")
        self.package=input("Select any one of the five packages shown above:")

    def getname(self):
        return self.__cusname
    
    def getaddress(self):
        return self.__cusaddress

    def getnumber(self):
        return self.__cusnumber

    def updateName(self, newname):
        self.__cusname=newname

    def updateNumber(self, newnum):
        self.__cusnumber=newnum

    def updateAdd(self, newadd):
        self.__cusaddress=newadd

    def updatePackage(self, newpackage):
        self.__package=newpackage
    
    def getserialnumber(self):
        m=self.__serialnum()
        return m

    def __serialnum(self):
        x=0
        for i in customer_arr:
            x+=1
        return x+1

class CustomerID(Customer):
    def __init__(self,customer,branch=0,year=str(22)):
        self.branch=branch
        self.year=year
        self.id=""
    def generateID(self):
        k=self.getserialnumber()
        m="{0:04}".format(k)
        self.id=str(self.branch)+str(self.year)+str(m)
        
def createcustomer(name,address,number):
    m=Customer()
    m.setItem(name,address,number)
    mid=CustomerID(m)
    mid.generateID()
    customer_arr.append(m)
    customer_id.append(mid.id)


class CustomerMenu:
    pass

class CustomerPackage(Customer):
    def __init__(self,customer=None):
        if customer:
            self.package=customer.choose_a_package()
    def showpackages(self):
        print("Occasional Package\n---------------\nNumber of orders:1\nCloth Details: x\nEstimated Delivery date for Occasional Package: Not more than 48 hours\nPickup Options:Weekly\nPackage Price: Rs.300\nDiscount:12%\nIf suppose the number of clothes exceed than that of the cloth limit of the package, then the overall price would be the sum of the price of package and the prices of the clothes added additionally\n\n")
        print("Monthly Package\n---------------\nNumber of orders:4\nCloth Details: x\nEstimated Delivery date for Monthly Package: 3-4 days\nPickup Options:Weekly\nPackage Price: Rs.800\nDiscount:15%\nNOTE:\n-----\nIf suppose the number of clothes exceed than that of the cloth limit of the package, then the overall price would be the sum of the price of package and the prices of the clothes added additionally. However,if payment is done on a weekly basis, it would mean that only at the last week of payment,the amount to be paid will be increased\n\n")
        print("Quarterly Package\n---------------\nNumber of orders:10\nCloth Details: x\nEstimated Delivery date for Quarterly Package: 1 week\nPickup Options:Weekly\nPackage Price: Rs.1200\nDiscount:25%\nNOTE:\n-----\nIf suppose the number of clothes exceed than that of the cloth limit of the package, then the overall price would be the sum of the price of package and the prices of the clothes added additionally. However,if payment is done on a weekly basis, it would mean that only at the last week of payment,the amount to be paid will be increased\n\n")
        print("Annual Package\n---------------\nNumber of orders:10\nCloth Details: x\nEstimated Delivery date for Annual Package: 1-2 months\nPickup Options:Weekly\nPackage Price: Rs.1200\nDiscount:23%\nNOTE:\n-----\nIf suppose the number of clothes exceed than that of the cloth limit of the package, then the overall price would be the sum of the price of package and the prices of the clothes added additionally. However,if payment is done on a weekly basis, it would mean that only at the last week of payment,the amount to be paid will be increased\n\n")
        print("Industrial Package\n-----------------\nNumber of orders:10\nCloth Details: x\nEstimated Delivery date for Industrial Package: \nPickup Options:Weekly\nPackage Price: Rs.1200\nDiscount:14%\nNOTE:\n-----\nIf suppose the number of clothes exceed than that of the cloth limit of the package, then the overall price would be the sum of the price of package and the prices of the clothes added additionally. However,if payment is done on a weekly basis, it would mean that only at the last week of payment,the amount to be paid will be increased\n\n")
    
    def clothdetails(self,package):
        if package=="Occasional":
            #return the cloth details of Occasional Package
            pass
        elif package=="Monthly":
            #return the cloth details of Monthly Package
            pass
        elif package=="Annual":
            #return the cloth details of Annual Package
            pass
        elif package=="Quarterly":
            #return the cloth details of Quarterly Package
            pass
        elif package=="Industrial":
            #return the cloth details of Industrial Package
            pass





customer_arr=[]
customer_id=[]
createcustomer("enkenb","no 12 jign nagwbn street",1234567890,)
# createcustomer("enb","no 512 jign nagwbn street",123456267890)
# createcustomer("en5b","no 512 jign na1251gwbn street",12345626716890)

m={}
for i in range(len(customer_arr)):
    m[customer_id[i]]=customer_arr[i]
CustomerPackage().showpackages()