#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

#在output创建一个txt，复制start信件

#以名字为条件的while循环

with open("./Input/Names/invited_names.txt") as f1:
    name = f1.readline()
    while name:
        name = name.strip()
        with open("./Input/Letters/starting_letter.txt") as f2:
            new_letter = f2.read()
            new_letter = new_letter.replace("[name]", name)
            with open(f"./Output/ReadyToSend/{name}_letter.txt", "w") as f3:
                f3.write(new_letter)
        name = f1.readline()




