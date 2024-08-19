from laundryData import clothData

class generateSlip:
    def __init__(self, orderDetails,pkg):
        self.clothDetails=orderDetails[1]
        self.package=pkg
        #self.email=Customer(sno).getEmail()
        
    def calculate(self):
        sum=0
        
        #Monthly
        if (self.package=="Monthly"):
            qty=5
            for i in (self.clothDetails[1]):
                x=clothData(i)
                
                #Cloth Constraints
                if (i=="Casuals"):
                    qty=2
                elif(i=="Formals"):
                    qty=2
                elif (i=="Ethnic Wear"):
                    qty=1
                    
                #Washing and Clothes Cost    
                for j in self.clothDeltails[1][i]:
                    
                    #Washing cost
                    if (j[0]=="Normal Wash"):
                        sum+=2
                    elif (j[0]=="Bleach"):
                        sum+=4
                    elif (j[0]=="Starch Wash"):
                        sum+=6
                    elif (j[0]=="Dry Cleaning"):
                        sum+=8
                            
                    #Cloth Cost
                    if (len(self.clothDetails[1][i])>qty):
                        sum+=x.getItem(j[1])*(j[2]-qty)
                        qty=0
                        
        #Occasional                
        elif (self.package=="Occasional"):
            qty=3
            for i in (self.clothDetails[1]):
                x=clothData(i)
                
                #Cloth Constraints
                if (i=="Casuals"):
                    qty=2
                elif(i=="Formals"):
                    qty=1
                    
                #Washing and Clothes Cost    
                for j in self.clothDeltails[1][i]:
                    
                    #Washing cost
                    if (j[0]=="Normal Wash"):
                        sum+=2
                    elif (j[0]=="Bleach"):
                        sum+=5
                    elif (j[0]=="Starch Wash"):
                        sum+=6
                    elif (j[0]=="Dry Cleaning"):
                        sum+=9
                            
                    #Cloth Cost
                    if (len(self.clothDetails[1][i])>qty):
                        sum+=x.getItem(j[1])*(j[2]-qty)
                        qty=0
                        
        #Quaterly                        
        elif (self.package=="Quaterly"):
            qty=9
            for i in (self.clothDetails[1]):
                x=clothData(i)
                
                #Cloth Constraints
                if (i=="Casuals"):
                    qty=3
                elif (i=="Formals"):
                    qty=2
                elif (i=="Ethnic Wear"):
                    qty=1
                elif (i=="Denims"):
                    qty=2
                elif (i=="House Accessories"):
                    qty=1
                    
                #Washing and Clothes Cost    
                for j in self.clothDeltails[1][i]:
                    
                    #Washing cost
                    if (j[0]=="Normal Wash"):
                        sum+=1.5
                    elif (j[0]=="Bleach"):
                        sum+=4
                    elif (j[0]=="Starch Wash"):
                        sum+=5
                    elif (j[0]=="Dry Cleaning"):
                        sum+=7
                            
                    #Cloth Cost
                    if (len(self.clothDetails[1][i])>qty):
                        sum+=x.getItem(j[1])*(j[2]-qty)
                        qty=0
                        
        #Annual                        
        elif (self.package=="Annual"):
            qty=13
            for i in (self.clothDetails[1]):
                x=clothData(i)
                
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
                for j in self.clothDeltails[1][i]:
                    
                    #Washing cost
                    if (j[0]=="Normal Wash"):
                        sum+=1
                    elif (j[0]=="Bleach"):
                        sum+=3
                    elif (j[0]=="Starch Wash"):
                        sum+=4.5
                    elif (j[0]=="Dry Cleaning"):
                        sum+=6.5
                            
                    #Cloth Cost
                    if (len(self.clothDetails[1][i])>qty):
                        sum+=x.getItem(j[1])*(j[2]-qty)
                        qty=0
                        
        #Industrial                        
        elif (self.package=="Industrial"):
            qty=18
            for i in (self.clothDetails[1]):
                x=clothData(i)
                
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
                for j in self.clothDeltails[1][i]:
                    
                    #Washing cost
                    if (j[0]=="Normal Wash"):
                        sum+=1
                    elif (j[0]=="Bleach"):
                        sum+=2.5
                    elif (j[0]=="Starch Wash"):
                        sum+=3.5
                    elif (j[0]=="Dry Cleaning"):
                        sum+=6
                            
                    #Cloth Cost
                    if (len(self.clothDetails[1][i])>qty):
                        sum+=x.getItem(j[1])*(j[2]-qty)
                        qty=0            
                    
        #Pickup cost
        if (self.clothDetails[2]=="Pickup"):
            sum+=30
            
        #Delivery cost
        if (self.clothDetails[3]=="Door Delivery"):
            sum+=40
            
        #Delivery date cost
        if (self.clothDetails[4]=="24 Hrs"):
            sum+=70
        elif (self.clothDetails[4]=="2 Days"):
            sum+=45
        elif (self.clothDetails[4]=="3 Days"):
            sum+=15
        
        return sum
        
              
            
        
    
