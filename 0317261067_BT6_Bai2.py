def credit_score(income, credit_history_years, has_bad_debt=False):
    if has_bad_debt == True:
        return "Reject"

    elif income < 10000000 or credit_history_years < 1:
        return "High Risk"

    elif income >= 20000000 and credit_history_years >= 3:
        return "VIP"

    else:
        return "Standard"


# Test case 1
print(credit_score(25000000, 4, False))

# Test case 2
print(credit_score(8000000, 2, False))

# Test case 3
print(credit_score(25000000, 4, True))

# Test case 4
print(credit_score(15000000, 2, False))
