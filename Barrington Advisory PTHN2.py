'''

Barrington Advisory Solutions
BIS Development Team Project

'''
print("Barrington Advisory Solutions, LLC")

company_name = input("Customer/Company Name ")
print(company_name)

company_size = int(input("Company Size "))
print(company_size,"Number of Employees ")

service_prices = {
    'Mergers and Acquisitions':3000,
    'Business Valuations':2000,
    'Financial Analysis & Operational Ideas':5000,
    'Strategic Planning Services':3500,
    'Specialized Strategic Consultion Services':4000,
    'Litigation Support':6000,
    '':0,
}

serv1 = input('Service 1 Needed ')
#calculate and display total cost based on the user entries
if((serv1=='Mergers and Acquisitions') 
or (serv1=='Business Valuations') 
or (serv1=='Financial Analysis & Operational Ideas') 
or (serv1=='Strategic Planning Services') 
or (serv1=='Specialized Strategic Consultion Services') 
or (serv1=='Litigation Support')):
    costPerService1= service_prices[serv1]


serv2 = input('Service 2 Needed ')
#calculate and display total cost based on the user entries
if((serv2=='Mergers and Acquisitions') 
or (serv2=='Business Valuations') 
or (serv2=='Financial Analysis & Operational Ideas') 
or (serv2=='Strategic Planning Services') 
or (serv2=='Specialized Strategic Consultion Services') 
or (serv2=='Litigation Support')
or (serv2=='')):
    costPerService2 = service_prices[serv2]


serv3 = input('Service 3 Needed ')
#calculate and display total cost based on the user entries
if((serv3=='Mergers and Acquisitions') 
or (serv3=='Business Valuations') 
or (serv3=='Financial Analysis & Operational Ideas') 
or (serv3=='Strategic Planning Services') 
or (serv3=='Specialized Strategic Consultion Services') 
or (serv3=='Litigation Support')
or (serv3=='')):
    costPerService3 = service_prices[serv3]


Time_required = int(input("Time Required "))

cost1 = costPerService1 * Time_required * company_size
cost2 = costPerService2 * Time_required * company_size
cost3 = costPerService3 * Time_required * company_size

totalcost = cost1 + cost2 + cost3

print('Price Quote','$',totalcost)
