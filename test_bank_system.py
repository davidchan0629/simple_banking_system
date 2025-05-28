from bank_system import *

def test_bank_system():
    bank = bank_system()

    print("### account creation test ###")

    # Test account creation
    bank.customers['Alice'] = Customer('Alice', 100)
    bank.customers['Bob'] = Customer('Bob', 50)
    assert 'Alice' in bank.customers
    assert 'Bob' in bank.customers
    assert bank.customers['Alice'].balance == 100
    assert bank.customers['Bob'].balance == 50
    print("Test 1 - Account creation test passed.\n")

    print("### deposit test ###")

    # Test deposit case 1 - valid deposit amount and valid account
    bank.deposit('Alice', 50)
    assert bank.customers['Alice'].balance == 150
    assert bank.customers['Bob'].balance == 50
    print("Test 2 - Deposit test with valid deposit amount and valid account passed.\n")

    # Test deposit case 2 - valid deposit amount but invalid account
    bank.deposit('Charlie', 100)
    assert bank.customers['Alice'].balance == 150
    assert bank.customers['Bob'].balance == 50
    print("Test 3 - Deposit test with valid deposit amount but invalid account passed.\n")

    # Test deposit case 3 - invalid deposit amount but valid account
    bank.deposit('Alice', -100)
    assert bank.customers['Alice'].balance == 150
    assert bank.customers['Bob'].balance == 50
    print("Test 4 - Deposit test with invalid deposit but valid account passed.\n")

    # Test deposit case 4 - invalid deposit amount and invalid account
    bank.deposit('Charlie', -100)
    assert bank.customers['Alice'].balance == 150
    assert bank.customers['Bob'].balance == 50
    print("Test 5 - Deposit test with invalid deposit and invalid account passed.\n")

    print("### withdrawal test ###")

    # Test withdrawal case 1 - valid withdrawal amount and valid account
    bank.withdraw('Alice', 30)
    assert bank.customers['Alice'].balance == 120
    print("Test 6 - Withdrawal test with valid withdrawal amount and valid account passed.\n")

    # Test withdrawal case 2.1 - insufficient withdrawal amount and valid account
    bank.withdraw('Alice', 300)
    assert bank.customers['Alice'].balance == 120
    print("Test 7 - Withdrawal test with valid withdrawal amount and valid account passed.\n")

    # Test withdrawal case 2.2 - invalid withdrawal amount and valid account
    bank.withdraw('Alice', -200)
    assert bank.customers['Alice'].balance == 120
    print("Test 8 - Withdrawal test with valid withdrawal amount and valid account passed.\n")

    # Test withdrawal case 3 - valid withdrawal amount and invalid account
    bank.withdraw('Charlie', 30)
    assert bank.customers['Alice'].balance == 120
    print("Test 9 - Withdrawal test with valid withdrawal amount and invalid account passed.\n")

    # Test withdrawal case 4 - invalid withdrawal amount and invalid account
    bank.withdraw('Charlie', -100)
    assert bank.customers['Alice'].balance == 120
    print("Test 10 - Withdrawal test with invalid withdrawal amount and invalid account passed.\n")

    print("### overdraft test ###")

    # Test overdrawal (should not be allowed)
    bank.withdraw('Alice', 200)
    assert bank.customers['Alice'].balance == 120
    print("Test 11 - Overdraft not allowed test passed.\n")

    print("### transfer test ###")

    # Test transfer case 1 - valid transfer amount and valid accounts
    bank.transfer('Alice', 'Bob', 20)
    assert bank.customers['Alice'].balance == 100
    assert bank.customers['Bob'].balance == 70
    print("Test 12 - Transfer test with valid transfer amount and valid accounts passed.\n")

    # Test transfer case 2 - insufficient transfer amount but valid accounts
    bank.transfer('Alice', 'Bob', 200)
    assert bank.customers['Alice'].balance == 100
    assert bank.customers['Bob'].balance == 70
    print("Test 13 - Transfer test with insufficient transfer amount but valid accounts passed.\n")

    # Test transfer case 3 - invalid transfer amount but valid accounts
    bank.transfer('Alice', 'Bob', -300)
    assert bank.customers['Alice'].balance == 100
    assert bank.customers['Bob'].balance == 70
    print("Test 14 - Transfer test with invalid transfer amount but valid accounts passed.\n")

    # Test transfer case 4 - valid transfer amount, with one valid from and one invalid to account
    bank.transfer('Alice', 'Charlie', 20)
    assert bank.customers['Alice'].balance == 100
    assert bank.customers['Bob'].balance == 70
    print("Test 15 - Transfer test with valid transfer amount, with one valid from and one invalid to account passed.\n")

    # Test transfer case 5 - valid transfer amount, with one invalid from and one invalid to account
    bank.transfer('Daisy', 'Charlie', 20)
    assert bank.customers['Alice'].balance == 100
    assert bank.customers['Bob'].balance == 70
    print("Test 16 - Transfer test with valid transfer amount, with one invalid from and one invalid to account passed.\n")

    # Test transfer case 6 - invalid transfer amount, with one invalid from and one invalid to account
    bank.transfer('Daisy', 'Charlie', -200)
    assert bank.customers['Alice'].balance == 100
    assert bank.customers['Bob'].balance == 70
    print("Test 17 - Transfer test with invalid transfer amount, with one invalid from and one invalid to account passed.\n")

    print("### save to CSV test ###")

    # Test save to csv
    bank.save_to_csv('test_bank_accounts.csv')
    print("Test 18 - Save to CSV test passed\n")

    print("### load from CSV test ###")

    # Test load from csv
    bank2 = bank_system()
    bank2.load_from_csv('test_bank_accounts.csv')
    assert 'Alice' in bank2.customers
    assert bank2.customers['Alice'].balance == 100
    assert 'Bob' in bank2.customers
    assert bank2.customers['Bob'].balance == 70
    print("Test 19 - Load from CSV test passed.\n")

    print("=== All tests completed successfully ===")

if __name__ == "__main__":
    test_bank_system()


