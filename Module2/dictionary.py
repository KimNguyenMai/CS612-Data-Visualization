dict = {'Name': 'abc', 'Age': 7}
print ("Name: ", dict['Name'], "\n", "Age: ", dict['Age'])

dict['Age'] = 20
print("Updated Age: ", dict['Age'])

dict['Phone_no'] = 123456789
print("After adding the new pair: ", dict)

del dict['Phone_no']
print("After deleting phone_no: ", dict)