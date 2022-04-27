#Learning Material

#list of transport mode
motorcycles= ["honda","suzuki","yamaha"]
print(motorcycles)

#modifying exixting list
motorcycles[0]="ducati"
print(motorcycles)

#adding item to the list

#appending item to end of list using append() method
motorcycles.append("honda")
print(motorcycles)

#inserting item to a list to specific location using insert() method
motorcycles.insert(0,"bmw")
print(motorcycles)

#removing element from the list using del
#value will delete permanently. you can no longer use anywhere in the list
print (motorcycles)
del motorcycles[0]

print(motorcycles)

#remove an item using pop() method
#The pop() method removes the last item in a list, but it lets you work with that item after removing it.

print(motorcycles)
popped_motorcycles=motorcycles.pop()
print(motorcycles)
print(popped_motorcycles)

print(motorcycles)

new_motorcycles = ["honda","suzuki","yamaha"]
last_owned= new_motorcycles.pop()
print("The last motorcycles was " + last_owned.title()+ ".")

# poping item from any position in a list

first_owned = new_motorcycles.pop(0)
print("The fist motorcycles was " + first_owned.title()+ ".")


#remove the item by value from a list using remove() method
best_motorcycle = ["honda","suzuki","yamaha"]
print(best_motorcycle)

best_motorcycle.remove("honda")
print(best_motorcycle)


# try it by youself chapter3

# 3-4 guest list

#guest list for inviiatiom
guest =["sahil","monarch","deepak","gaurav"]

#invitation message to guest
invitation = "Hi " + guest[0].title() + " please come to the fucntion."
print(invitation)

invitation = "Hi " + guest[1].title() + " please come to the fucntion."
print(invitation)

invitation = "Hi " + guest[2].title() + " please come to the fucntion."
print(invitation)

invitation = "Hi " + guest[3].title() + " please come to the fucntion."
print(invitation)


#3-5 change guest list

invitation = "\nHi\nSorry! "  + guest[1].title() + " will not be able to join the fuction."
print(invitation)

# lets invite tejaswi instead
del guest[1]
guest.insert(1,"tejaswi")

#lets print the invitation list again


invitation = "Hi " + guest[0].title() + " please come to the fucntion."
print(invitation)

invitation = "Hi " + guest[1].title() + " please come to the fucntion."
print(invitation)

invitation = "Hi " + guest[2].title() + " please come to the fucntion."
print(invitation)

invitation = "Hi " + guest[3].title() + " please come to the fucntion."
print(invitation)

#3-6 change guest list
#lets invite more guest as we have more sopace.

print("\nWe got a bigger table!")

guest.insert(0,"sourav")
guest.insert(1,"tousif")
guest.append("deepak")

#let print the final invitaion list.

invitation = "Hi " + guest[0].title() + " please come to the fucntion."
print(invitation)

invitation = "Hi " + guest[1].title() + " please come to the fucntion."
print(invitation)

invitation = "Hi " + guest[2].title() + " please come to the fucntion."
print(invitation)

invitation = "Hi " + guest[3].title() + " please come to the fucntion."
print(invitation)

invitation = "Hi " + guest[4].title() + " please come to the fucntion."
print(invitation)

invitation = "Hi " + guest[5].title() + " please come to the fucntion."
print(invitation)

invitation = "Hi " + guest[6].title() + " please come to the fucntion."
print(invitation)


#3-7 shrinking the guest list
#new dinner table wont be arriving at time and you have space only for two 	

print("\nwe got some problem.Dinner table wont arrive at time.we can invite only two people !")
invitation = guest.pop(0)
print("Sorry " + invitation.title() + " there is no room at at the table")

invitation = guest.pop(0)
print("Sorry " + invitation.title() + " there is no room at at the table")

invitation = guest.pop(0)
print("Sorry " + invitation.title() + " there is no room at at the table")

invitation = guest.pop(0)
print("Sorry " + invitation.title() + " there is no room at at the table")

invitation = guest.pop(0)
print("Sorry " + invitation.title() + " there is no room at at the table")

print(guest)

#sent invitation to remaining guest

invitation= guest[0].title()
print(invitation + " dont forget to come to dinner.")

invitation= guest[1].title()
print(invitation + " dont forget to come to dinner.")

#make list empty
del guest[0]
del guest[0]

#print empty list
print(guest)









