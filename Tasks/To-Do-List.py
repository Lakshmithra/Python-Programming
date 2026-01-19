print("\nWelcome to our TO-DO-LIST program !\n")
print("Structure your day, master your goals !")
task_dict = {}
task_no = 1

while True:  
  
    print("\n1. Add Tasks\n2. View Tasks\n3. Update Status\n4. Exit\n")
    choice = int(input("Select any one option : "))
    
    if choice == 1:
            n = int(input("\nEnter number of tasks you want to add : "))
            for i in range(n):
                name = input("\nDescribe the task : ")
                task_details = {"Description":name , "Status":"Not Completed"}
                task_dict[task_no] = task_details
                print("\nYour task has been added successfully !")
                task_no += 1
              
    elif choice == 2:
      
            if len(task_dict)!= 0:
                print("-" * 58)
                print(f"{'Task no':^10} | {'Task name':^25} | {'Task Status':^15} |")
                print("-" * 58)
                for keys , values in task_dict.items():
                    print(f"{keys:^10} | {values['Description']:^25} | {values['Status']:^15} |")
                print("-" * 58)
            else:
                print("\nNo tasks added yet !")
              
    elif choice == 3:

            no = int(input("\nEnter task number : "))
            if no in task_dict.keys():
                          task_dict[no]["Status"] = "Completed"
                          print(f"\nTask {no} has been marked as completed !")
            else:
                print("\nINVALID ! Task number not found !")
    elif choice == 4:
            ques = input("\nAre you sure you want to exit ? (yes / no) : ").upper()

            if ques == 'YES':
                print("\nKeep organizing and stay productive!")
                print("\nCome back tomorrow !")
                break
            else:
                continue
