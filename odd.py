#writing program to seperste odd and even line
file=open("akash.txt","r")

r=file.read()  #reading the file
file.close() #closing the main file 

lines=[]
lines=r.split() #spliting the file into words
newlist=[]
newlist=r.splitlines("\n") #spliting the file into lines




print("Total number of characters in file:",len(r))
oddlines=[] #creted empty list for odd lines 
oddlines=newlist[::2] #slicing for odd lines 
evenlines=[] #created empty list for even lines
evenlines=newlist[1::2] #slicing for even lines


print(lines)
print()
print()
print(newlist)
# open file to seprate odd lines 
odd=open("odd.txt","w")
for i in oddlines:
    odd.write(i)
    

odd.close()
#closed odd file

# open file to seprate even lines

even=open("even.txt","w")
for j in evenlines:
    even.write(j)
even.close()
#closed even file
print()
print()
print("odd lines seprated to odd.txt file")
print()
print()
print("even lines seprated to even.txt file")

# for get frequency of each character in file
frequency={} #created empty list for frequency
for char in r: 
    if char in frequency:
        frequency[char]+=1
    else:
        frequency[char]=1
print()
print("frequency of each character in file:")
for i in frequency:
    print(i," : ",frequency[i])





print("Hello world" )



