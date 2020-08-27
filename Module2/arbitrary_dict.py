def menu(item, quan, **restaurant): # ** creates a dictionary with as many key - val pair as user wants
    restaurant['Item'] = item
    restaurant['Quantity'] = quan
    return restaurant


restaurant = menu('soup', '1', Location = 'Seattle', Zipcode = '98109')
print(restaurant)