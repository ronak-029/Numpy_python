import numpy as np

price = np.array([200,650,500,300])
discount = 10
final_price = price - ((price*discount)/100)
print(final_price)