
print('welcome to Menu-Based Program! ')

option=("1","2","3","4","5")
def option():
    print('Please select on option :')
    print('1.Print Pattern')
    print('2.Rotate Array')
    print('3.Help')
    print('4.Exit')
option()
user_input=int(input('Option'))
while user_input !=0:

    if user_input ==1:
        n = int(input("Enter the number of rows: "))
        for i in range(n, 0, -1):
            print('*' * i)
    elif user_input ==2:
        
        # Input the number of elements and the array

        n = int(input("Enter the number of elements (n): "))

        k = int(input("Enter the number of steps to rotate (k): "))

        elements = input("Enter the array elements separated by spaces: ").split()

        elements = [int(element) for element in elements]
        def rotate_right(arr, k):
            n = len(arr)
            # Ensure k is within the range of the array size
            k = k % n
            # Use slicing and concatenation to perform the rotation
            rotated = arr[-k:] + arr[:-k]
            return rotated
        # Rotate the array
        rotated_array = rotate_right(elements, k)
        # Print the rotated array
        print("Rotated array:", rotated_array)
    elif user_input ==3:
        print("1: Print a pattern with 'n' rows of decreasing asterisks.")

        print("2: Rotate an array of 'n' elements to the right by 'k' steps.")

        print("3: Display this help message (you are here).")

        print("4: Exit the program.")
    elif user_input == 4:

        print("Exiting the program.")

        break  # This line exits the program

    else:

        print("Invalid choice. Please select a valid option (1/2/3/4).")
    print('Please select on option :')
    user_input=int(input('Option'))

    