#inputs
age =int(input('Enter Age ---> '))
month_rev = float(input('Input Monthly Revenue ---> '))
credit_score = int(input('Input Credit Score ---> '))
years = float(input('Input years in business ---> '))
has_defaults = bool(eval(input('Do you have any defaults? (True or False) ---> ')))
collateral_name = input('Input Collateral ---> ')
collateral_val = float(input('Enter Collateral Value ---> '))

max_loan = 0
base_fee = 0 

if age >= 21 and years >= 2.0 and has_defaults == False:
    print('Baseline Passed')
    if credit_score >= 720: #tier1
        print('high credit score')
        max_loan = 3 * month_rev
        if month_rev >= 50000:
            print('rev is above 50k')
            base_fee = max_loan * 0.015
            print('base fee is set to', base_fee)
        else:
            print('rev is below 50k')
            base_fee = max_loan * 0.025
            print('base fee is set to', base_fee)

        #collateral
        if collateral_val >= max_loan:
            print ('collateral', collateral_name, 'with a value of', collateral_val, 'is accepted')
        else:
            print('rejected: insufficient collateral value for', collateral_name)

        #surcharge
        surge_fee = max_loan * base_fee
        if max_loan %5000 != 0:
            print('Additional Charge is Added')
            surge_fee += 250
            print('Updated base fee is', base_fee)

    elif credit_score <= 620 and credit_score <720 : #tier2
        print('credit score is between 620 to 720')
        max_loan = 1.5 * month_rev
        if years >= 5.0:
            print('business is around more than 5years')
            base_fee = max_loan * 0.02
            print('base fee is set to', base_fee)
        else: 
            print('business is less than 5years')
            base_fee = max_loan * 0.035
            print('base fee is set to', base_fee)

         #collateral
        if collateral_val >= max_loan:
            print ('collateral', collateral_name, 'with a value of', collateral_val, 'is accepted')
        else:
            print('rejected: insufficient collateral value for', collateral_name)
        
        #surcharge
        surge_fee = max_loan * base_fee
        if max_loan %5000 != 0:
            print('Additional Charge is Added')
            surge_fee += 250
            print('Updated base fee is', base_fee)

    elif credit_score <620: #tier3 
        print('low credit score')
    else:
        print('rejected')
else:
    print('Baseline Rejected')