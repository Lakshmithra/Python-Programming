try:
    with open("handfile.txt" , "r") as file:
        content = file.read()
    modified_content = content.replace("Universe" , "God")
    with open("handfile.txt" , "w") as file:
        file.write(modified_content)
except FileNotFoundError:
    print("\nFile not found !")
except PermissionError:
    print("\nPermission is denied !")
except Exception as e:
    print(f"\nError occured !\nError : {e}")
