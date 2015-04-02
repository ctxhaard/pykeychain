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
import account
import account_term
import copy
from getpass import getpass

# Per avere un qualcosa su cui salvare...
def main():
    file_name = 'archive.protected'
    password = getpass('Insert your password: ')
    in_file= account.open_decrypt(file_name,password)
    accounts = list(account.load_accounts(in_file))
    account_term.print_accounts(accounts)
    while True:
        choice = input('Select an account by index (1-%i 0:add new [Q]uit): ' % len(accounts))
        try:
            iChoice = int(choice)
            print('You selected: ',iChoice)
        except:
            iChoice = -1
#             print('You choosed to quit')
            
        if 0 == iChoice:
            newAccount = account.Account()
            if account_term.edit_account(newAccount):
                accounts.append(newAccount)    
                out_file = account.open_encrypt(file_name,password)
                account.save_accounts(accounts,out_file)
                account_term.print_accounts(accounts)

        elif iChoice > 0:
            account_term.print_account(accounts[iChoice-1])
            choice = input('[E]dit, [Delete] or cancel')
            if choice in 'eE':
                accountToEdit = copy.copy(accounts[iChoice-1])
                if account_term.edit_account(accountToEdit):
                    accounts[iChoice-1] = accountToEdit
                    account.save_accounts(accounts, file_name, password)
            elif choice in 'dD':
                accountToDelete = accounts[iChoice-1]
                if input('Confirm to delete %s (y or n)?' % accountToDelete.title) in 'yY':
                    del accounts[iChoice-1]
                    account.save_accounts(accounts, file_name, password)
                    account_term.print_accounts(accounts)
                
            # TODO: aggiungere possibilità di modificare il record
        else:
            break
    print("Bye!")

#    print(accounts)
#    print(list(accounts))
#    print(dbData);

if __name__ == '__main__':
    main()
    
