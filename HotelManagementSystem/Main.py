class hotelfarecal:

    def __init__(self,total='',roombill=0,gamebill=0,foodbill=0,laundrybill=0,a=1800,name='',address='',cindate='',coutdate='',rno=101):

        print ("*****WELCOME TO YELLOWBELLL HOTEL*****\n")

        self.total=total

        self.foodbill=foodbill

        self.laundrybill=laundrybill

        self.gamebill=gamebill

        self.roombill=roombill
        self.a=a
        self.name=name
        self.address=address
        self.cindate=cindate
        self.coutdate=coutdate
        self.rno=rno
        
    def inputdata(self):
        self.name=input("\nEnter your name:")
        self.address=input("\nEnter your address:")
        self.cindate=input("\nEnter your check in date:")
        self.coutdate=input("\nEnter your checkout date:")
        print("\nYour room no.:",self.rno,"\n")
        
    def roomrent(self):#sel1353

        print ("\nWe have the following rooms for you:\n")
        
        print ("1. Small ₱3,000")

        print ("2. Medium ₱5,000")

        print ("3. Large ₱9,000")

        print ("4. Suite ₱15,000")

        room=int(input("\nEnter Your Choice Please: "))

        night=int(input("\nFor How Many Nights Did You Stay: "))

        if room == 1:

            self.roombill=3000*night

        elif room == 2:

            self.roombill=5000*night

        elif room == 3:
            
            self.roombill=9000*night

        elif room == 4:

            self.roombill=15000*night

        else:

            print ("\nPlease choose a room")

        print ("\nYour room rent is = ₱",self.roombill,"\n")

    def restaurentbill(self):

        print("***RESTAURANT MENU***")
        
        print("1. Breakfast ₱200/head")
        
        print("2. Lunch ₱250/head")
        
        print("3. Dinner ₱180/head")
        
        print("4. Snacks ₱50/head")
        
        print("5. Quit")

        while (1):

            food=int(input("\nEnter your choice:"))

            if food == 1:
                head=int(input("\nEnter the quantity:"))
                self.foodbill=self.foodbill+200*head

            elif food == 2:
                 head=int(input("\nEnter the quantity:"))
                 self.foodbill=self.foodbill+250*head

            elif food == 3:
                 head=int(input("\nEnter the quantity:"))
                 self.foodbill=self.foodbill+180*head

            elif food == 4:
                 head=int(input("\nEnter the quantity:"))
                 self.foodbill=self.foodbill+50*head

            elif food == 5:
                break;

            else:
                print("\nInvalid option")

        print ("Total food Cost is ₱",self.foodbill,"\n")

    def	laundrybill(self):
        print ("****LAUNDRY MENU*****")

        print ("1.Shorts ₱20")
        
        print ("2.Pants ₱35")
        
        print ("3.Shirt ₱30")
        
        print ("4.Jeans ₱40")
        
        print ("5.Polo ₱35")
        
        print ("6.Exit")

        while (1):

            clothes=int(input("\nEnter your choice:"))

            if clothes == 1:
                f=int(input("\nEnter the quantity: "))
                self.laundrybill=self.laundrybill+20*f

            elif clothes == 2:
                f=int(input("\nEnter the quantity:"))
                self.laundrybill=self.laundrybill+35*f

            elif clothes == 3:
                f=int(input("\nEnter the quantity:"))
                self.laundrybill=self.laundrybill+30*f

            elif clothes == 4:
                f=int(input("\nEnter the quantity:"))
                self.laundrybill=self.laundrybill+40*f

            elif clothes == 5:
                f=int(input("\nEnter the quantity:"))
                self.t=self.t+35*f
                
            elif clothes == 6:
                break;
            
            else:
                print ("\nInvalid option")


        print ("\nTotal Laundary Cost is ₱",self.laundrybill,"\n")

    def gamebill(self):
        print ("****GAME MENU*****")

        print ("1.Table tennis -  ₱20/hr")
        
        print  ("2.Bowling - ₱50/hr")
        
        print ("3.Basketball - 35/hr")
        
        print ("4.Video games - 60/hr")
        
        print ("5.Pool - 50/hr")
              
        print ("6.Exit")

        while (1):
            
            game=int(input("\nEnter your choice:"))

            if game == 1:
                hours=int(input("\nNo. of hours:"))
                self.gamebill=self.gamebill+20*hours

            elif game == 2:
                hours=int(input("\nNo. of hours:"))
                self.gamebill=self.gamebill+50*hours

            elif game == 3:
                hours=int(input("\nNo. of hours:"))
                self.gamebill=self.gamebill+35*hours

            elif game == 4:
                hours=int(input("\nNo. of hours:"))
                self.gamebill=self.gamebill+60*hours

            elif game == 5:
                hours=int(input("\nNo. of hours:"))
                self.gamebill=self.gamebill+50*hours
                
            elif (game==6):
                break;

            else:
                print ("\nInvalid option")

        print ("\nTotal Game Bill is ₱",self.gamebill,"\n")

    def display(self):
        print ("\n*****HOTEL BILL*****\n")
        print ("Customer details:")
        print ("Customer name:",self.name)
        print ("Customer address:",self.address)
        print ("Check in date:",self.cindate)
        print ("Check out date",self.coutdate)
        print ("Room no.",self.rno)
        print ("Your Room rent is:",self.roombill)
        print ("Your Food bill is:",self.foodbill)
        print ("Your laundary bill is:",self.laundrybill)
        print ("Your Game bill is:",self.gamebill)

        self.total=self.roombill+self.foodbill+self.laundrybill+self.gamebill

        print ("Your sub total bill is: ₱",self.total)
        print ("Additional Service Charges is ₱",self.a)
        print ("Your grandtotal bill is: ₱",self.total+self.a,"\n")
        self.rno+=1

def main():

    a=hotelfarecal()


    while 1:
        print("1.Enter Customer Data")

        print("2.Calculate rommrent")

        print("3.Calculate restaurant bill")

        print("4.Calculate laundry bill")

        print("5.Calculate gamebill")

        print("6.Show total cost")

        print("7.EXIT")

        b=int(input("\nEnter your choice:"))

        if b == 1:
            a.inputdata()

        elif b == 2:
            a.roomrent()

        elif b == 3:
            a.restaurentbill()

        elif b == 4:
            a.laundrybill()

        elif b == 5:
            a.gamebill()

        elif b == 6:
            a.display()

        elif b == 7:
            quit()
            
main()
