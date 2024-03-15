
number_of_books = int(input('Enter the number of books purchased this month' ))
if number_of_books == 0:
    print('You earn 0 points')
elif number_of_books == 2:
    print('You earn 5 points')
elif number_of_books == 4:
    print('You earn 15 points')
elif number_of_books == 6:
    print('You earn 30 points')
elif number_of_books >= 8:
    print('You earn 60 points')
