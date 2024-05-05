import base64
import bcrypt
from faker import Faker
fake = Faker()


class InsertUser:
    def __init__(self, collection):
        self.collection = collection

    def insert_users(self, count):
        col = self.collection

        print('\x1b[6;30;34m' +
              'insert_users: ' +
              '\x1b[0m')

        if count <= 0:
            return print('The number of inserted users must be above 0')
        elif count == 1:
            login = fake.user_name()
            email = f'{login}@{fake.free_email_domain()}'
            password = f'{login}123'
            hashed_pw = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt(10))
            hex_hash = hashed_pw.decode('utf-8')

            insert_cursor = col.insert_one({
                'login': login,
                'email': email,
                'password': hex_hash
            })

            print(insert_cursor)
        elif count > 1:
            inserted_data = []

            for i in range(0, count):
                login = fake.user_name()
                email = f'{login}@{fake.free_email_domain()}'
                password = f'{login}123'
                hashed_pw = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt(10))
                hex_hash = hashed_pw.decode('utf-8')

                inserted_data.append({
                    'login': login,
                    'email': email,
                    'password': hex_hash
                })

            print(inserted_data)

            insert_cursor = col.insert_many(inserted_data)
