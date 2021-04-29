

def print_delivery_report(the_file):                        #create a function that takes an argument hereby called the_file
    the_file = open(the_file)                               #the_file is a variable that contains the opened file passed as an argument when the function is called
    for line in the_file:                                   #loop through the file, line by line
        line = line.rstrip()                                #define a line as the line itself but without any training empty characters
        words = line.split('|')                             #break each line into indexes wherever there is a bar

        melon = words[0]                                    #"melon" is the item at the first index
        count = words[1]                                    #"melon" is the item at the second index
        amount = words[2]                                   #"melon" is the item at the third index

        print(f"Delivered {count} {melon}s for total of ${amount}") #print this statement and reference the aforementioned variables
    the_file.close()                                        #close the file


print_delivery_report(um-deliveries-20140519.txt)           #call the argument for file um-deliveries-20140519.txt
print_delivery_report(um-deliveries-20140520.txt)           #call the argument for file um-deliveries-20140520.txt
print_delivery_report(um-deliveries-20140521.txt)           #call the argument for file um-deliveries-20140521.txt


#My code does not work, and I am not sure why. 
#I am receving error messages of "invalid syntax"
#I think it has something to do with how I'm trying to give the argument
#but I hit my 30 minutes so I will review it with an instructor later! 
#Thank you for your help in advance!



#original code, with only index errors resolved:

# print("Day 1")
# the_file = open("um-deliveries-20140519.txt")
# for line in the_file:
#     line = line.rstrip()
#     words = line.split('|')

#     melon = words[0]
#     count = words[1]
#     amount = words[2]

#     print("Delivered {} {}s for total of ${}".format(
#         count, melon, amount))
# the_file.close()


# print("Day 2")
# the_file = open("um-deliveries-20140520.txt")
# for line in the_file:
#     line = line.rstrip()
#     words = line.split('|')

#     melon = words[0]
#     count = words[1]
#     amount = words[2]

#     print("Delivered {} {}s for total of ${}".format(
#         count, melon, amount))
# the_file.close()


# print("Day 3")
# the_file = open("um-deliveries-20140521.txt")
# for line in the_file:
#     line = line.rstrip()
#     words = line.split('|')

#     melon = words[0]
#     count = words[1]
#     amount = words[2]

#     print("Delivered {} {}s for total of ${}".format(
#         count, melon, amount))
# the_file.close()
