import os

def check_path_access(path):
    access_info = {
        "existence": os.path.exists(path),
        "readability": os.access(path, os.R_OK),
        "writability": os.access(path, os.W_OK),
        "executability": os.access(path, os.X_OK)
    }
    return access_info

def main():
    path = input("Enter the path to be checked: ")

    access_info = check_path_access(path)

    print("\nAccess information for path:", path)

    #1
    print("Existence: ", end = "")
    if access_info["existence"]:
        print("Exits")
    else:
        print("Does not exist")
    
    #2
    print("Readability: ", end = "")
    if access_info["readability"]:
        print("Readable")
    else:
        print("Not readable")
    
    #3
    print("Writability: ", end = "")
    if access_info["writability"]:
        print("Writable")
    else:
        print("Not writable")

    #4
    print("Executability: ", end = "")
    if access_info["executability"]:
        print("Executable")
    else:
        print("Not executable")

main()
