import array
total_charge = 0
i = 0
charge = [5,6,7,8]
for i in range(4):
    total_charge = total_charge + charge[i]    
    
tip = total_charge*0.18
sales_tax = total_charge*0.07
total_charge = total_charge + tip + sales_tax
print ('Total charge is $',total_charge)
    
