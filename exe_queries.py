from queries.find_user import UserFinder
from queries.insert_user import InsertUser


def check_existence(var, iterate):
    if var is not None:
        if iterate:
            for obj in var:
                print('Data: \n', obj)
        else:
            print('Data: \n', var)
    else:
        print('No data satisfies this query')


def exe_queries(collection):

    finder = UserFinder(collection)

    one_user_data = finder.find_one_user('Qwe')
    check_existence(one_user_data, False)

    filter_user_data = finder.filter_users(addr_email='@mail.com')
    check_existence(filter_user_data, True)

    insert = InsertUser(collection)

    insert.insert_users(2)
