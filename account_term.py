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
    for index in range(0,5):
        if index == 0:
            value = input('Title [%s]: ' % account.title)
            account.title = value or account.title
        elif index == 1:
            value = input('URL [%s]: ' % account.URL)
            account.URL = value or account.URL
        elif index == 2:
            value = input('Username: [%s]' % account.username)
            account.username = value or account.username            
        elif index == 3:
            value = input('Password [%s]: ' % account.password)
            account.password = value or account.password 
        elif index == 4:
            value = input('Notes [%s]: ' % account.note)
            account.note = value or account.note 
        result = result or value

    if result:
        result =  (input("[s]ave or [C]ancel')? ") in 'sS')
    return result

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
