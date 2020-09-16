
# For reading or writting the file ,first we have open the file
# open(File name,Access mode)

# Access Modes:-
# 	1."r ":- for reading.
# 	2."w ":- for writing.
# 	3."a ":- for appending.
# 	4."r+":- for both reading and writing


############################################################## READING #####################################################################


# open the file in read mode
f1 = open("file.txt",'r')


# It will read the whole text 
# use "read" method
print(f1.read())


# It will read characterwie 
# use "read(number_of_characters)" method
# print starting 10 character
# print(f.read(10))


# close the file
f1.close()


############################################################# WRITTING #####################################################################


# for writing in the file,use write method 
# write(Enter your text)

# open the same file in write mode
# it also create the file ,if not exists
f2 = open("file.txt",'w')


# Use Write method for writtng in file
# write(Enter text here)
# It will overwite the existing text also
f2.write("How are you!\n")
f2.write("What is your name!")


# close the file
f2.close()


############################################################# APPENDING ####################################################################


# here appending will help us to append the text
# above we have use "w" access mode for writting in file, it will overwrite the text
# but "a" access mode will add in existing text
# it also create the file ,if not exists
f3 = open("file.txt",'a')


# Use write method for writtng in file
# write(Enter text here)
# It will not overwite the existing text also
f3.write("Good")


# close the file
f3.close()