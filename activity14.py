age = int(input('Enter Age ---> '))
is_employed = bool(input('Are you currently employed? (True or False) ---> '))
credit_score = int(input('Input credit score ---> '))
annual_income = int(input('Input annual income ---> '))
has_collateral = bool(eval(input('Do you have any collateral? ( True or False) ---> ')))

base_rate = 0.0 

if age >= 21 and is_employed == True :
    print('APPLICANT PASSED')
    if credit_score >= 750 : #tier1
        print('You have a high credit score')
        if annual_income >= 100000:
            base_rate = 4.5 
            print('You have high salary and high credit score, you got a loyalty discount!, your total interest rate is',base_rate,"%'")
        else:
            base_rate = 5.0
            print('You have a low salary but high credit score, your total interest rate is',base_rate,"%")
    elif credit_score > 600 and credit_score < 750 : #tier2
        print('You have a fair credit score')
        if has_collateral == True:
            base_rate = 7.0
            print('accepted at', base_rate, '%')
        elif annual_income <40000:
            base_rate = 9.5
            print('accepted at', base_rate, '%')
        else:
            base_rate = 8.0
    else: #tier3
        print('Rejected: Credit score is too low')

else: 
    print('REJECTED: Failed baseline criteria')