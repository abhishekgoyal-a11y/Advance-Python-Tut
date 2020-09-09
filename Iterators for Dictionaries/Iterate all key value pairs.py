statesAndCapitals = { 
					'Gujarat' : 'Gandhinagar', 
					'Maharashtra' : 'Mumbai', 
					'Rajasthan' : 'Jaipur', 
					'Bihar' : 'Patna'
					} 
					
print('List Of given states and their capitals:\n') 

# Iterating over values 
for state, capital in statesAndCapitals.items(): 
	print(state, ":", capital) 


# Output:-

List Of given states and their capitals:

Bihar : Patna
Gujarat : Gandhinagar
Rajasthan : Jaipur
Maharashtra : Mumbai

# it will print all keys and values

print(statesAndCapitals.items())

# Output:- 

dict_items([('Gujarat', 'Gandhinagar'), ('Maharashtra', 'Mumbai'), ('Rajasthan', 'Jaipur'), ('Bihar', 'Patna')])