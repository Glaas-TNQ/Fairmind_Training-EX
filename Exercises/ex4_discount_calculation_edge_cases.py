# Exercise 4: Discount Calculation and Edge Case Analysis
# -------------------------------------------------------
# A basic function to apply percentage-based discounts. Your task as a tester
# is to explore boundary conditions, input validation, and potential failure
# modes, such as negative prices or over-100% discounts.

def calculatediscount(price, discount):
   if discount > 100:
       raise ValueError('Discount cannot exceed 100%')
   return price * (100 - discount) / 100

# Test cases
print(calculatediscount(100, 105)) # Should raise an exception

