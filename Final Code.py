'''

Barrington Advisory Solutions
BIS Development Team Project

'''

service = {
    'Mergers and Acquisitions':3000,
    'Business Valuations':2000,
    'Financial Analysis & Operational Ideas':5000,
    'Strategic Planning Services':3500,
    'Specialized Strategic Consultion Services':4000,
    'Litigation Support':6000,
    '': 0
    }

class QuotaCalc:
    
    ## A class that asks for data about a client and then calculates
    ## both the time required for the service and the total estimate cost

    def __init__(self, cust_name = 'none', co_size = 0, option1=None, option2=None, option3=None):      ##This initializes the class with all of the variables that we will use

        self.cust_name = cust_name
        self.co_size = co_size
        self.option1 = option1
        self.option2 = option2
        self.option3 = option3
        self.timeRequired = 0
        if co_size == 0:
            self.timeRequired = 0
        elif co_size <= 20:
            self.timeRequired = 1
        elif co_size <= 40:
            self.timeRequired = 2
        elif co_size <= 60:
            self.timeRequired = 3
        elif co_size <= 80:
            self.timeRequired = 4
        elif co_size <= 100:
            self.timeRequired = 5
        elif co_size <= 150:
            self.timeRequired = 6
        else:
            self.timeRequired = 8
    def getTime(self):
        return self.timeRequired

    def calcCost(self):
        cost = self.timeRequired * service[self.option1]
        if self.option2:
            cost += self.timeRequired * service[self.option2]
        if self.option3:
            cost += self.timeRequired * service[self.option3]

        return cost
#monthly_service_cost = ##option1 + opiton2 + option3        <- this needs to be fixed to their actual variable names
#total_cost = months * monthly_service_cost          ##this calculates the total cost for all of the services 
    

if __name__ == "__main__":
    print('Quota Calculator\n')
    name = input("Customer/Company Name: ")
    size = int(input("Size of Company: ")) 
    while size <1 or size >200: #need to check that is between 1-200
        print("\nError! Company size must be between 1-200! Please enter a valid input...")
        size = int(input("Size of Company: "))
    
    option1 = input("Service 1: ") #required
    while option1 not in service:
        print("\nError! Please enter a valid service...")
        option1 = input("Service 1: ") #required

    option2 = input("Service 2: ") #optional
    while option2 not in service:
        print("\nError! Please enter a valid service...")
        option2 = input("Service 2: ") #required

    option3 = input("Service 3: ") #optional
    while option3 not in service:
        print("\nError! Please enter a valid service...")
        option3 = input("Service 3: ") #required
    print("\nPrinting the results...\n")
    # print(name)
    # print(size)
    # print(option1)
    # print(option2)
    # print(option3)

    calc = QuotaCalc(name, size, option1, option2, option3)
    timeRequired = calc.getTime()
    print("Time rquired: ", str(timeRequired) + " month(s)")

    totalCost = calc.calcCost()
    totalCost = format(totalCost, '.2f')
    print("Price quote: $", totalCost)



''' Make groups for the number of employees eg 0 - 20 is small & takes one month.
Then take that one month and multiply it by the number of months
maybe break it into like 5 groups to make it smoother
'''