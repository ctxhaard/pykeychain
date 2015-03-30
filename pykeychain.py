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
from account import load_accounts

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


# Per avere un qualcosa su cui salvare...
def main():
    password = input('Insert your password: ')
    in_file= open_decrypt('archive.protected',password)
    accounts = list(load_accounts(in_file))
    for (i,account) in enumerate(accounts):
        print(i+1,account.title)
    choice = input('Select an account by index (0 for add new): ')
    while choice < 0:
        try:
            iChoice = int(choice)
        except:
            iChoice = -1
        finally:
            print('you selected: ',iChoice)
            if 0 == iChoice:
                # TODO: aggiungere interfaccia di inserimento nuovo
                pass
            elif iChoice > 0:
                print(str(accounts[iChoice-1]))
                # TODO: aggiungere possibilità di modificare il record
            else:
                print("'",choice,"' is not a valid option")
#    print(accounts)
#    out_file = open_encrypt('archive.protected2',password)
#    save_accounts(accounts,out_file)
#    print(list(accounts))
#    print(dbData);

if __name__ == '__main__':
    main()
    
