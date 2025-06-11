def calculatediscount(price, discount):
   if discount > 100:
       raise ValueError('Discount cannot exceed 100%')
   return price * (100 - discount) / 100

# Test cases
print(calculatediscount(100, 105)) # Should raise an exception

