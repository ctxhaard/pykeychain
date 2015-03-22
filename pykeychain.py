#!/usr/bin/env python3 

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

def load_accounts(file):
    """
    Reads accounts from file
    Returns a generator object giving dictionaries with records
    """
    account = {}

    for record in (line.split(':') for line in file):
        if len(record) == 0: continue
        record = list(map(str.strip,record))
        if len(record[0]) == 0:
            continue
        elif record[0][:1] == '-':
            if(len(record)):
                yield account
                account = {}
        elif len(record) >= 2:
            key, *value = record
            account[key] = ':'.join(value)
    yield account

def save_accounts(accounts,file):
    """
    Saves accounts to file
    """
    for account in accounts:
        for key in account:
            file.write('%s:%s\n' % (key,account[key]))
        else:
           file.write('%s\n' % ('-'*3))
    file.close()

# Per avere un qualcosa su cui salvare...
def main():
    password = input('Insert your password: ')
    in_file= open_decrypt('archive.protected',password)
    accounts = list(load_accounts(in_file))
    print(accounts)
    out_file = open_encrypt('archive.protected2',password)
    save_accounts(accounts,out_file)
#    print(list(accounts))
#    print(dbData);

if __name__ == '__main__':
    main()
    
