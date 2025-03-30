def collatz_game_with_range():
    try:
        start = int(input("Enter the start of the range (positive integer): "))
        end = int(input("Enter the end of the range (positive integer): "))

        if start <= 0 or end <= 0 or start > end:
            print("Please enter a valid positive range where start <= end.")
            return

        max_attempts = 0
        number_with_max_attempts = start

        for number in range(start, end + 1):
            attempts = 0
            current = number
            while current != 1:
                if current % 2 == 0:
                    current //= 2
                else:
                    current = current * 3 + 1
                attempts += 1

            if attempts > max_attempts:
                max_attempts = attempts
                number_with_max_attempts = number

        print(f"The number with the largest attempts is {number_with_max_attempts} with {max_attempts} attempts.")
    except ValueError:
        print("Invalid input. Please enter valid integers.")

collatz_game_with_range()