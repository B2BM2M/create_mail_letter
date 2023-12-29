#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

namelist = []
# create a list
with open("..\\Mail_Merge_Project\\Input\\Names\\invited_names.txt", mode="r") as guess:
    contents = guess.readlines()
    for names in contents:
        namelist.append(names.strip())
#    print(namelist)

with open("..\\Mail_Merge_Project\\Input\\Letters\\starting_letter.txt") as letter:
    text_content = letter.read()

    for name in namelist:
        letter_name = text_content.replace("[name]", f"{name}")
        #print(letter_name)
        with open(f"..\\Mail_Merge_Project\\Output\\ReadyToSend\\letter_for_{name}.txt", "w") as file:
            file.write(letter_name)
