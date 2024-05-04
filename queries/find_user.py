class UserFinder:
    def __init__(self, collection):
        self.collection = collection

    def find_one_user(self, login):
        try:
            print('\x1b[6;30;32m' +
                  'find_one_user: ' +
                  '\x1b[0m')

            col = self.collection
            user_count = col.count_documents({'login': login})

            if user_count > 0:
                user_cursor = col.find({'login': login})
                user_data = next(user_cursor)
                return user_data
            else:
                return None
        except Exception as e:
            print(f"Error finding user: {e}")
            return None

    def filter_users(self, exact_email='', exact_login='', addr_email='', login_like=''):
        try:
            print('\x1b[6;30;32m' +
                  'filter_users: ' +
                  '\x1b[0m')

            col = self.collection

            data_array = []

            if exact_email:
                user_like = col.find({'email': exact_email})
                for x in user_like:
                    data_array.append(x)
            if exact_login:
                user_like = col.find({'login': exact_login})
                for x in user_like:
                    data_array.append(x)
            if addr_email:
                user_like = col.find({'email': {
                    '$regex': f'.*{addr_email}$'
                }})
                for x in user_like:
                    data_array.append(x)
            if login_like:
                user_like = col.find({
                    'login': {
                        '$regex': f'{login_like}.*'
                    }
                })
                for x in user_like:
                    data_array.append(x)

            return data_array

        except Exception as e:
            print(e)
