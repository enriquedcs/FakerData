from faker import Faker
import csv

#fake.first_name()
#fake.last_name()
#fake.postalcode()
#fake.company()
#fake.credit_card_expire
#fake.credit_card_security_code
#fake.street_name
#fake.city()


fake_data = Faker()

# Create fake name
name = fake_data.name()
print(name)

# Create fake address
address = fake_data.address()
print(address)

# Create fake email
email = fake_data.email()
print(email)

# display name, address, email
print('Name: {}, Address: {}, email: {}'.format(name,address,email))

# function to fill a list
def create_names_list (how_many):
    names = []
    for _ in range(0,how_many):
        names.append(fake_data.first_name())
    return names

# generate a large set of fake data
# for _ in range(0,20):
#     print(fake_data.email())


# create person objects with name, address, etc
# class Customer:
#     def __init__(self, name, address, email):
#         self.name = name
#         self.address = address
#         self.email = email
#
#     #special method
#     def __repr__(self):
#         return 'name: {}, address: {}, email: {}'.format(self.name,self.address,self.email)
#
# #instance of customer
# customer1 = Customer(fake_data.name(),fake_data.address(),fake_data.email())
# print(customer1)


#write fake data to csv file

RECORD_COUNT = 10000
with open("fake_date.csv", "w", newline = '') as csvfile:
    fieldnames = ['first_name', 'last_name', 'email', 'address', 'city', 'state',
                  'country']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for i in range(RECORD_COUNT):
        writer.writerow(
            {
                'first_name': fake_data.name(),
                'last_name': fake_data.name(),
                'email': fake_data.email(),
                'address': fake_data.street_address(),
                'city': fake_data.city(),
                'state': fake_data.state(),
                'country': fake_data.country()
            }

        )

