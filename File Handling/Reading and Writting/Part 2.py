# By default 'r' access mode will be there
# Here we not need for closing the file
# it will automatically close the file whenever the task is completed

# it does it effect anything whether we close the file or not
# But whnen we use in higher-level project it may cause
with open("file.txt") as f1:   
    data = f1.read() 
    print(data)


# Same for writting
with open("file.txt",'w') as f2:   
	f2.write("Hello World!") 


############################################################## SPLIT #######################################################################


with open("file.txt", "r") as file: 

	# "readlines" will split the line ,whenever new line start
    data = file.readlines() 
    print(data)

    # iterate each line
    for line in data: 

    	# "split" will split line ,whenever space come
        word = line.split() 
        print(word)


######################################## COPY TEXT AND PASTE INTO ANOTHER FILE #############################################################


# open the file in read mode

with open('file.txt','r') as r:
	data = r.read()

# open the file in write mode

with open('file1.txt','w') as w:
	w.write(data)