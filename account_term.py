'''
Created on 02/apr/2015

@author: ctomasin
'''
from getpass import getpass

SEP = '-' * 10

def edit_account(account):
    result = False
#     print('-' * 10)
#     print(1,'Title:',account.title)
#     print(2,'URL:',account.URL)
#     print(3,'Username:',account.username)
#     print(4,'Password:',account.password)
#     print('-' * 10)
    while True:
        choice = input("Select index ('s:save C:cancel'): ")
        if choice == '1':
            account.title = input('Title: ')
            result = True
        elif choice == '2':
            account.URL = input('URL: ')
            result = True
        elif choice == '3':
            account.username = input('Username: ')
            result = True
        elif choice == '4':
            account.password = getpass('Password: ')
            result = True
        elif choice == '5':
            account.note = input('Notes: ')
            result = True
        elif choice == 's':
            break
        else:
            result = False
            break
    return result # in teoria non dovrebbe mai arrivare qui

def print_accounts(accounts,filter=None):
    """
    Prints a list of account titles filtere using a list of indexes.
    If filer is None all account titles are printed
    """
    print(SEP)
    for (i,account) in enumerate(accounts):
        if filter == None or i in filter:
            print(i+1,account.title)
    print(SEP)
    
def print_account(account):
    print(SEP)
    print(str(account))
    print(SEP)

if __name__ == '__main__':
    pass
