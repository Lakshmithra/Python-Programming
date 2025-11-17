def display_seats(seat_matrix , show_no):
    row = ['A','B','C','D','E']
    cols = [1,2,3,4,5]
    for i in  seat_matrix.keys():
       if i == show_no:
           print(" ", end = "")
           for l in cols:
               print(" ",l,end = "")
           print()
           for j ,k in enumerate(seat_matrix[i]):
               print(row[j] , k)

def book_seats(seat_matrix , show_no):
    n = int(input("Enter number of seats : "))
    seats = []
    rows = ['A','B','C','D','E']
    cols = [1,2,3,4,5]
    booked = 0
    for i in range(n):
        seat_no = input("Enter seat no : ").upper()
        row_index = rows.index(seat_no[0])
        col_index = int(seat_no[1])-1
        if seat_matrix[show_no][row_index][col_index] == 0:
            seat_matrix[show_no][row_index][col_index] = 1
            print(f"Seat {seat_no} booked successfully !")
            booked += 1
        else:
            print(f"Seat {seat_no} is already booked !Choose another seat.")
    print("\nSeat Matrix after booking\n")
    display_seats(seat_matrix , show_no)

    ticket_price = 150
    tax_price = 0.05
    s = ticket_price * booked
    total = s + (s * tax_price)
    print(f"\nTotal amount (with tax) : {total}")

def cancel_seats(seat_matrix , show_no):
    n = int(input("Enter number of seats : "))
    seats = []
    rows = ['A','B','C','D','E']
    cols = [1,2,3,4,5]
    for i in range(n):
        seat_no = input("Enter seat no : ").upper()
        row_index = rows.index(seat_no[0])
        col_index = int(seat_no[1])-1
        if seat_matrix[show_no][row_index][col_index] == 1:
            seat_matrix[show_no][row_index][col_index] = 0
            print(f"Seat {seat_no} cancelled successfully !")
        else:
            print(f"Seat {seat_no} wasn't booked !")
    print("\nSeat Matrix after cancelling\n")
    display_seats(seat_matrix , show_no)
    

seat_matrix = {'show1': [[0] * 5 for i in range(5)],
               'show2': [[0] * 5 for i in range(5)]}

show_name = input("Enter show name(showno) : ")

while(1):
    print("\n1.Display seats\n2.Book seats\n3.Cancel seats\n4.Exit\n")
    choice = int(input("Enter your choice (1/2/3/4) : "))
    if choice == 1:
        display_seats(seat_matrix , show_name)
    elif choice == 2:
        book_seats(seat_matrix , show_name)
    elif choice == 3:
        cancel_seats(seat_matrix , show_name)
    elif choice == 4:
        break
    else:
        print("Invalid choice !")

