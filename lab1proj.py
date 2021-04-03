# This is the first project of the python lab 
# First question
mylist = [] # List in which integers are going to be stored in
value = int(input("Please user enter the length(max num of integers) of the list:")) # User input for every integer which will later be added to the list
# int is used to convert the type of the input(which is by default string) to integer

for i in range(0, value): # For loop used for adding each element to the list
    element = int(input("The element added to the list is:")) # For the same reason as before int is used here as well
    mylist.append(element)

def removeDuplicates(tlist): # Function used for removing duplicate integers located in the list
    temporarylist = [] # Array(list) which is going to be used as a means to store the elements which are not found for a second time in the list we take as an argument
    
    print("The list before changes", tlist)

    for element in tlist: # If an element which is found in tlist is not found in temporary list then it will be added to temporarylist
        if element not in temporarylist: 
            temporarylist.append(element)
        else: # Otherwise the element will not be added
            print("The following element already exists in the list:",element)
    
    return(temporarylist)

mynewlist = removeDuplicates(mylist) # We take the list and pass it as an argument to our function removeDuplicates and the result is stored in mynewlist

print("The list after changes", mynewlist)

# Second question
def sortList(newlist): # Function which utilizes the bubblesort function in order to sort the elements of our now non-duplicate list in ascending order

    length = len(newlist) # len function which is used to take the maximum length of an list(array)
    temp = 0 # variable which will be used to temporarily so as to store a value

    for i in range(length-1): 
        for j in range(0,length-i-1):
            if newlist[j+1] < newlist[j]:
                temp = newlist[j]
                newlist[j] = newlist[j+1]
                newlist[j+1] = temp

    return(newlist)

mynewlist2 = sortList(mynewlist) # We take the list and pass it as an argument to our function sortList and the result is stored in mynewlist

print("The changed list sorted in ascending order",mynewlist2)