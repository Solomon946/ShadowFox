friends = ["Aditya", "Rohan", "Sneha", "Anusmita", "Sudipa"] #Making a list of friends names 

friends_length = [] #Creating an empty list to store names and their lengths eg.,(Aditya,6)

for name in friends: #Iterating through each name in friends list
    friends_length.append((name, len(name))) #Appending a tuple of name and its length to friends_length list

print(friends_length) #Printing the final list which holds name and their lenghts as tuples 
