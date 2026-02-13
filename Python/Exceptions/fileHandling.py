
# ! Old Way Of Making the files
# file = open("index.js" , "w")

# try :
#     file.write(f"Hello Chotuuuu")
# finally :
#     file.close()

#@ Mordern Way to Make File
    
with open("filemade.py" , 'w') as file :
    file.write("print('helllo World')")