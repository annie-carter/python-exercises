# View Balance, Credit, Debit, and Exit
# print( 'Welcome! Please select an option from the menu ?')
# print('balance\ncredit\ndebit\nexit\n')

# choice = input('Please select')
#
# balance = 'View Balance'
# credit = 'Credit'
# debit = 'Debit '
# exit_checkbook = 'Exit'
#
# if choice == balance:
#     print(balance)
# elif choice == credit:
#     print(credit)
# elif choice == debit:
#     print(debit)
# elif choice == exit_checkbook:
#     print(exit_checkbook)

ledger = open('ledger.txt')
print(ledger.read())
ledger.close()

with open('ledger.txt', 'w') as file:
    print(file.write('550'))




