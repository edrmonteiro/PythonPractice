from mock_vendors import MOCKVENDORS
CUSTOMERS = MOCKVENDORS

def main():
    for customer in CUSTOMERS:
        print('Name: %s; Address: %s' %
              (customer.name, customer.address))

if __name__ == '__main__':
    main()
