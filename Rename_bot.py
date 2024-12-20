import os

#Option menu -------------------------------------------------------------------------------
def Show_menu():
    print("\n===== RENAME MENU =====")
    print("1. Add prefix")
    print("2. Change extension")
    print("3. Replace text in names")
    print("4. Name sequentially")
    print("5. Exit")
    return input("Select an option: ")
#-------------------------------------------------------------------------------------------

#Option 1 ----------------------------------------------------------------------------------
def Get_folder():
    Folder = input("Input the route to the file: ").strip()
    if not os.path.exists(Folder) or not os.path.isdir(Folder):
        print("The Folder route is invalid. Try again")
        return Get_folder()
    return Folder
#-------------------------------------------------------------------------------------------

#Option 2 ----------------------------------------------------------------------------------
def Rename_with_prefix(Folder):
    Prefix = input("Input a prefix: ").strip()
    for File in os.listdir(Folder):
        Original_route = os.path.join(Folder, File)
        if os.path.isfile(Original_route):
            extension = os.path.splitext(File)[1]
            New_name = f"{Prefix}_{File}"
            New_route = os.path.join(Folder, New_name)
            os.rename(Original_route, New_route)
            print(f"Renamed: {File} -> {New_name}")
    print("Rename completed!")
#-------------------------------------------------------------------------------------------

#Option 3 ----------------------------------------------------------------------------------
def Change_extension(Folder):
    New_extension = input("Input the new extension (example: .txt): ").strip()
    for File in os.listdir(Folder):
        Original_route = os.path.join(Folder, File)
        if os.path.isfile(Original_route):
            Base_name = os.path.splitext(File)[0]
            New_name = f"{Base_name}{New_extension}"
            New_route = os.path.join(Folder, New_name)
            os.rename(Original_route, New_route)
            print(f"Renamed: {File} -> {New_name}")
    print("Extension change completed!")
#-------------------------------------------------------------------------------------------

#Option 4 ----------------------------------------------------------------------------------
def Replace_text(Folder):
    Text_to_replace = input("Text to replace: ").strip()
    New_text = input("New text: ").strip()
    for File in os.listdir(Folder):
        Original_route = os.path.join(Folder, File)
        if os.path.isfile(Original_route):
            New_name = File.replace(Text_to_replace, New_text)
            New_route = os.path.join(Folder, New_name)
            os.rename(Original_route, New_route)
            print(f"Renamed: {File} -> {New_name}")
    print("Text rename completed!")


#Option 5 ----------------------------------------------------------------------------------
def Name_sequentially(Folder):
    Prefix = input("Input the prefix for all Files: ").strip()
    for i, File in enumerate(os.listdir(Folder), start=1):
        Original_route = os.path.join(Folder, File)
        if os.path.isfile(Original_route):
            extension = os.path.splitext(File)[1]
            New_name = f"{Prefix}_{i}{extension}"
            New_route = os.path.join(Folder, New_name)
            os.rename(Original_route, New_route)
            print(f"Renamed: {File} -> {New_name}")
    print("Sequential renaming completed!")
#-------------------------------------------------------------------------------------------

# Programa principal
def main():
    Folder = Get_folder()
    while True:
        Option = Show_menu()
        if Option == "1":
            Rename_with_prefix(Folder)
        elif Option == "2":
            Change_extension(Folder)
        elif Option == "3":
            Replace_text(Folder)
        elif Option == "4":
            Name_sequentially(Folder)
        elif Option == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again")

if __name__ == "__main__":
    main()
