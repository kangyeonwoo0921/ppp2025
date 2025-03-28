mart = {"우유": 2800, "계란": 300, "빵": 1200, "물": 1700}

cart = ["우유", "계란", "빵", "빵", "빵"]

total_cost = 0
for item in cart:
    total_cost = total_cost + mart[item]
    #total_cost += mart[item]
     
print("가격은 {:,}입니다.".format(total_cost)) 