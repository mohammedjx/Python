def printing (income, tax_braket, filing_status):
    tax_deducted = tax_braket * income
    income_taxed = income - tax_deducted
    if filing_status == 1:
        print("-----------------------\nYou selected: Filing Single")
    elif filing_status == 2:
        print("-----------------------\nYou selected: Married Filing Jointly")
    print("Your income is: $", income)
    print("Your deducted taxes: $", tax_deducted)
    print("Your tax braket: ", tax_braket)
    print("Your income after taxes: $", income_taxed)
    
    
#Function for calculation
def tax (filing_status, income):
    if filing_status == 2:
       
        if int(income)>= 19751 and int(income) <= 80250:
            tax_braket = 12/100
            printing (income, tax_braket, filing_status)
           
        elif int(income)>= 80251 and int(income) <= 171050:
            tax_braket = 22/100
            printing (income, tax_braket, filing_status)
                   
        elif int(income)>= 1 and int(income) <= 19750:
            tax_braket = 10/100
            printing (income, tax_braket, filing_status)
                  
        elif int(income)>= 171051 and int(income) <=  326600:
            tax_braket = 24/100
            printing (income, tax_braket, filing_status)
           
        elif int(income)>= 326601 and int(income) <=  414700:
            tax_braket = 32/100
            printing (income, tax_braket, filing_status)
           
        elif int(income)>= 414701 and int(income) <=  622050:
            tax_braket = 35/100
            printing (income, tax_braket, filing_status)
           
        elif int(income)>= 622050:
            tax_braket = 37/100
            printing (income, tax_braket, filing_status)
            
            
            
    if filing_status == 1:
        
        if int(income) <= 9875:
            tax_braket = 10/100
            printing (income, tax_braket, filing_status)
            
        elif int(income) >= 9876 and int(income) <= 40125:
            tax_braket = 12/100
            printing (income, tax_braket, filing_status)
            
        elif int(income) >= 40126 and int(income) <= 85525:
            tax_braket = 22/100
            printing (income, tax_braket, filing_status)
            
        elif int(income) >= 85526 and int(income) <= 163300:
            tax_braket = 24/100
            printing (income, tax_braket, filing_status)
            
        elif int(income) >= 163301 and int(income) <= 207350:
            tax_braket = 32/100
            printing (income, tax_braket, filing_status)
            
        elif int(income) >= 207350 and int(income) <= 518400:
            tax_braket = 35/100
            printing (income, tax_braket, filing_status)
            
        elif int(income) >= 518401:
            tax_braket = 37/100
            printing (income, tax_braket, filing_status)
    else:
        print("Out of Filing Status selection range\nTerminating...")
        pass
            
         
repeat = True            
print("\\\ Welcome to the Tax Calculator (2020/2021) //\n\nPlease select from the following...")       
while repeat == True:
    tax (int(input("Filing status: \n1 - Single.\n2 - Married, filing jointly. \n(Select 1/2):")), int(input("Enter your income: $")))
    repeat = input("Check other numbers? (Y/N) ")
    if repeat.lower() == 'y':
        repeat = True
    elif repeat.lower() == 'n':
        print("Thank you!")
        repeat = False
    else:
        print("Wrong selection\nTerminating")
        repeat = False