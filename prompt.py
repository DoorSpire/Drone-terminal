import os
import subprocess
import shutil

mainDir = 'Files'
canLoop = True

def rename_file(current_path, new_name):
    try:
        if os.path.isfile(current_path):
            directory = os.path.dirname(current_path)
            extension = os.path.splitext(current_path)[1]

            new_path = os.path.join(directory, new_name + extension)

            os.rename(current_path, new_path)
            print(f"File '{current_path}' renamed to '{new_name + extension}' successfully.")
        else:
            print(f"File '{current_path}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

def delete_file(file_path):
    try:
        if os.path.isfile(file_path):
            os.remove(file_path)
            print(f"File '{file_path}' has been deleted successfully.")
        else:
            print(f"File '{file_path}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

def run_exe(file_path):
    try:
        result = subprocess.run([file_path], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
        print("output:", result.stdout.decode())
        print("errors:", result.stderr.decode())
    except subprocess.CalledProcessError as e:
        print("error running the executable:", e)
    except FileNotFoundError:
        print("the specified executable was not found.")

def text_editor(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.readlines()
        
        print("current content of the file:")
        for i, line in enumerate(content, start=1):
            print(f"{i}: {line}", end='')

        print("you can start editing the file. type '~~' on a new line to save and close.")
        print("to edit a specific line, type 'edit <line_number>' and then provide the new content.")

        while True:
            command = input()
            if command == "~~":
                break
            elif command.startswith("edit "):
                try:
                    line_number = int(command.split()[1])
                    if 1 <= line_number <= len(content):
                        print(f"current content of line {line_number}: {content[line_number - 1]}", end='')
                        new_content = input(f"new content for line {line_number}: ")
                        content[line_number - 1] = new_content + '\n'
                    else:
                        print("invalid line number.")
                except ValueError:
                    print("invalid command format. use 'edit <line_number>'.")
            else:
                content.append(command + '\n')
        
        with open(file_path, 'w') as file:
            file.writelines(content)
        
        print("file saved and closed.")
    
    except FileNotFoundError:
        print(f"file not found: {file_path}")
    except Exception as e:
        print(f"an error occurred: {e}")

def print_file_contents(file_path):
    try:
        with open(file_path, 'r') as file:
            contents = file.read()
            print(contents)
    except FileNotFoundError:
        print(f"file '{file_path}' does not exist.")
    except IsADirectoryError:
        print(f"'{file_path}' is a directory, not a file.")
    except PermissionError:
        print(f"permission denied to read '{file_path}'.")
    except Exception as e:
        print(f"an error occurred while trying to read the file: {e}")

def list_files(folder_path):
    files_and_dirs = os.listdir(folder_path)
    
    files = [f for f in files_and_dirs if os.path.isfile(os.path.join(folder_path, f))]
    folders = [d for d in files_and_dirs if os.path.isdir(os.path.join(folder_path, d))]
    
    return files, folders

def create_new_folder(parent_directory, folder_name):
    new_folder_path = os.path.join(parent_directory, folder_name)
    
    if os.path.exists(new_folder_path):
        print(f"cannot create folder '{folder_name}' because it already exists in the directory.")
    else:
        os.makedirs(new_folder_path)
        print(f"folder '{folder_name}' created successfully.")

def create_new_file(directory, file_name):
    new_file_path = os.path.join(directory, file_name)
    
    if os.path.exists(new_file_path):
        print(f"cannot create file '{file_name}' because it already exists in the directory.")
    else:
        with open(new_file_path, 'w') as file:
            file.write('')
        print(f"file '{file_name}' created successfully.")

def rename_folder(current_path, new_name):
    try:
        if os.path.isdir(current_path):
            parent_dir = os.path.dirname(current_path)

            new_path = os.path.join(parent_dir, new_name)

            os.rename(current_path, new_path)
            print(f"Folder '{current_path}' renamed to '{new_name}' successfully.")
        else:
            print(f"Folder '{current_path}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

def delete_folder(folder_path):
    try:
        if os.path.isdir(folder_path):
            shutil.rmtree(folder_path)
            print(f"Folder '{folder_path}' has been deleted successfully.")
        else:
            print(f"Folder '{folder_path}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

def lex(inputt):
    global canLoop
    global mainDir

    if inputt == "exit":
        canLoop = False
    elif inputt == "help":
        print("your main directory is Files/")
        print("exit - exit the program")
        print("dir - list files in the current directory")
        print("newFo - create a new folder")
        print("newFi - create a new file")
        print("openFo - open the selected folder")
        print("openFi - edit files")
        print("print - prints the contents of a file")
        print("EXE - run an EXE file")
        print("deleteFi - delete a file.")
        print("deleteFo - delete a folder")
        print("renameFi - rename a file")
        print("renameFo - rename a folder")
    elif inputt == "dir":
        files, folders = list_files(mainDir)

        for folder in folders:
            print(folder)
        for file in files:
            print(file)
    elif inputt == "newFo":
        newInput = input(" <Folder Name> ")
        create_new_folder(mainDir, newInput)
    elif inputt == "newFi":
        newInput = input(" <File Name> ")
        create_new_file(mainDir, newInput)
    elif inputt == "openFo":
        newInput = input(" <Folder Directory> ")
        new_folder_path = os.path.join(mainDir, newInput)
        if not os.path.isdir(new_folder_path):
            print(f"directory '{newInput}' not recognized. setting main directory to 'Files'.")
            mainDir = 'Files'
        else:
            mainDir = new_folder_path
    elif inputt == "print":
        newInput = input(" <File Directory> ")
        print_file_contents(newInput)
    elif inputt == "openFi":
        file_path = input(" <File Directory> ")
        text_editor(file_path)
    elif inputt == "EXE":
        newInput = input(" <EXE Directory> ")
        run_exe(newInput)
    elif inputt == "deleteFi":
        newInput = input(" <File Directory> ")
        delete_file(newInput)
    elif inputt == "deleteFo":
        newInput = input(" <File Directory> ")
        delete_folder(newInput)
    elif inputt == "renameFi":
        newInput = input(" <File Directory> ")
        newInput2 = input(" <New Name> ")
        rename_file(newInput, newInput2)
    elif inputt == "renameFo":
        newInput = input(" <File Directory> ")
        newInput2 = input(" <New Name> ")
        rename_folder(newInput, newInput2)
    else:
        print(f"'{inputt}' is not recognized")

def main():
    userInput = input(" <Prompt> ")
    lex(userInput)

if __name__ == "__main__":
    print("|--\   |--\   /----\  |\    |  |-----          /----\  |-----")
    print("| | \  |   \  |    |  | \   |  |               |    |  |     ")
    print("| |  | |----  |    |  |  \  |  |---            |    |  |----|")
    print("| | /  |  \   |    |  |   \ |  |               |    |       |")
    print("|__/   |   \  \----/  |    \|  |-----          \----/  -----|")
    print("(C) DoorSpire 2024")

    while canLoop:
        main()