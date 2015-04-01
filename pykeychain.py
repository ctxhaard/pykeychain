#!/usr/bin/env python3 
# -*- coding: utf-8 -*

# TODO: richiedere la password
# se il file è stato decrittato con successo
#   richiedere una parola chiave
#   mostrare i record che hanno match (indicizzati)
#   se nessun match chiedere se si vuole creare un nuovo record
#   se si chiedere di compilare tutti campi
#   se no tornare all'inizio
# se match
# conferma del salvataggio
# chiusura

"""
This module is a simple custom keychain manager
Test Password is:"test_password"
"""
import os
import shutil
from datetime import datetime
from account import load_accounts, save_accounts, Account
from copy import copy
from getpass import getpass

SEP = '-' * 10

def open_decrypt(file_name,password):
    """
    Decrypts the file with name 'file_name' and returns a file object
    """
    file = os.popen('openssl enc -d -aes-256-cbc -in %s -k %s' % (file_name,password),'r')
    return file

def open_encrypt(file_name,password):
    """
    Open a file to write encrypted data
    """
    file = os.popen('openssl enc -aes-256-cbc -salt -out %s -k %s' % (file_name,password),'w')
    return file

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

def print_accounts(accounts):
    print(SEP)
    for (i,account) in enumerate(accounts):
        print(i+1,account.title)
    print(SEP)
    
def print_account(account):
    print(SEP)
    print(str(account))
    print(SEP)
    
def bkp_filename(file_name):
    strDate = datetime.now().strftime('%Y%m%d%H%M%S')
    result = file_name + '_' + strDate + '.bkp'
    return result

# Per avere un qualcosa su cui salvare...
def main():
    file_name = 'archive.protected'
    password = getpass('Insert your password: ')
    in_file= open_decrypt(file_name,password)
    accounts = list(load_accounts(in_file))
    print_accounts(accounts)
    while True:
        choice = input('Select an account by index (1-%i 0:add new [Q]uit): ' % len(accounts))
        try:
            iChoice = int(choice)
            print('You selected: ',iChoice)
        except:
            iChoice = -1
#             print('You choosed to quit')
            
        if 0 == iChoice:
            newAccount = Account()
            if edit_account(newAccount):
                accounts.append(newAccount)    
                out_file = open_encrypt(file_name,password)
                save_accounts(accounts,out_file)
                print_accounts(accounts)

        elif iChoice > 0:
            print_account(accounts[iChoice-1])
            choice = input('[E]dit, [Delete] or cancel')
            if choice in 'eE':
                accountToEdit = copy(accounts[iChoice-1])
                if edit_account(accountToEdit):
                    accounts[iChoice-1] = accountToEdit
                    shutil.copy(file_name,bkp_filename(file_name))
                    out_file = open_encrypt(file_name,password)
                    save_accounts(accounts,out_file)
            elif choice in 'dD':
                accountToDelete = accounts[iChoice-1]
                if input('Confirm to delete %s (y or n)?' % accountToDelete.title) in 'yY':
                    del accounts[iChoice-1]
                    shutil.copy(file_name,bkp_filename(file_name))
                    out_file = open_encrypt(file_name,password)
                    save_accounts(accounts,out_file)
                    print_accounts(accounts)
                
            # TODO: aggiungere possibilità di modificare il record
        else:
            break
    print("Bye!")

#    print(accounts)
#    print(list(accounts))
#    print(dbData);

if __name__ == '__main__':
    main()
    
