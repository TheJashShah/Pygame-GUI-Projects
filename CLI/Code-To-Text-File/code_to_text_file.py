import os

def write(file_folder, name):

    text = ""

    for file in file_folder:

        with open(file, "r") as FILE:
            text += (" ").join(FILE.readlines())
            text += f"\n#---{file}---#\n"

    with open(os.path.join(r"C:\Users\Jash\OneDrive\Documents\code_to_text" , f"{name}.txt"), "w") as file_:
        file_.writelines(text)

def code_to_text_file():

    PATH = input("Enter your path[enter directly after pressing copy as path, and remove apostrophe]: ")
    src_question = input("Are your files in a src folder?[Y/N]: ")
    extension = input("Enter the extension properly[.py, .go, .js, .c]: ")
    
    try:

        if src_question == "Y" or src_question == "y":
            PATH += "/src"

        files = os.listdir(PATH)

        folder = []

        for file in files:
            if extension in file:
        
                path = PATH + f"/{file}"
                folder.append(path)

        name = input("Enter name of the text file: ")

        write(folder, name)

    except:
        print("Your Path or extension maybe wrong.")

code_to_text_file()
