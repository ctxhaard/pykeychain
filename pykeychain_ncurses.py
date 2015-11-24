#!/usr/bin/env python3

import curses
import account
import copy


def prompt(text):
        _cmdwin.clear()
        _cmdwin.addstr(text.replace('\n',','))
        _cmdwin.refresh()
        return _cmdwin.getstr().decode()

def print_accounts(accounts,filterList=None):
    global _infopad
    _infopad = curses.newpad(len(accounts),curses.COLS-1)
    _infopad.bkgd(ord(' '),curses.A_REVERSE)
    line = 0
    for (i,account) in enumerate(accounts):
        if filterList == None or i in filterList:
            _infopad.addstr(line,0,'%i %s' % (i+1,account.title))
            line = line + 1
    _infopad.refresh(0,0,0,0,curses.LINES-2,curses.COLS-1)

def print_account(account):
    global _accountwin
    _accountwin = curses.newwin(10,curses.COLS-16,5,5)
    _accountwin.addstr(1,0,' Title: ')
    account.title and _accountwin.addstr(account.title)
    _accountwin.addstr(2,0,' URL: ')
    account.URL and _accountwin.addstr(account.URL)
    _accountwin.addstr(3,0,' Username: ')
    account.username and _accountwin.addstr(account.username)
    _accountwin.addstr(4,0,' Password: ')
    account.password and _accountwin.addstr(account.password)
    _accountwin.addstr(5,0,' Note: ')
    account.note and _accountwin.addstr(account.note)
    _accountwin.addstr(6,0,' Other: ')
    account.others and _accountwin.addstr(str(account.others))
    _accountwin.box(0,0)
    _accountwin.refresh()
    pass

def edit_account(account):
    result = False
    for index in range(0,5):
        if index == 0:
            value = prompt('Title [%s]: ' % account.title)
            account.title = value or account.title
        elif index == 1:
            value = prompt('URL [%s]: ' % account.URL)
            account.URL = value or account.URL
        elif index == 2:
            value = prompt('Username: [%s]' % account.username)
            account.username = value or account.username            
        elif index == 3:
            value = prompt('Password [%s]: ' % account.password)
            account.password = value or account.password 
        elif index == 4:
            value = prompt('Notes [%s]: ' % account.note)
            account.note = value or account.note 
        result = result or value
    if result:
        result =  (prompt("[s]ave or [C]ancel')? ") in 'sS')
    return result




def main(stdscr):
    stdscr.clear()
    global _cmdwin
    _cmdwin = curses.newwin(2,curses.COLS,curses.LINES-2,0)
    _cmdwin.addstr('Insert your password:',curses.A_STANDOUT)

    _cmdwin.refresh()
    curses.noecho()
    # getstr restituiscce <bytes>
    password = _cmdwin.getstr().decode()
    curses.echo() 
           
    file_name = 'archive.protected'
    in_file= account.open_decrypt(file_name,password)
    accounts = list(account.load_accounts(in_file))
    print_accounts(accounts)
    _cmdwin.clear()
    while True:
        global _accountwin
        _accountwin = None
        _cmdwin.clear()
        _cmdwin.addstr('Select an account by keyword or by index (1-%i 0:add new [Q]uit): ' % len(accounts))
        _cmdwin.refresh()
        choice = _cmdwin.getstr().decode()
        if choice in 'qQ':
            break
        elif len(choice) == 0:
            print_accounts(accounts)
        else:
            try:
               iChoice = int(choice)
#               print('You selected: ',iChoice)
            except:
               iChoice = -1

            if 0 == iChoice:
                newAccount = account.Account()
                if edit_account(newAccount):
                    accounts.append(newAccount)    
                    account.save_accounts(accounts,file_name,password)
                    print_accounts(accounts)

            elif iChoice in range(1,len(accounts)+1):
                print_account(accounts[iChoice-1])
                choice = prompt('[e]dit, [d]elete] or [C]ancel? ')
                if len(choice) == 0:
                    _accountwin = None
                    print_accounts(accounts)
                elif choice in 'eE':
                    accountToEdit = copy.copy(accounts[iChoice-1])
                    if edit_account(accountToEdit):
                        accounts[iChoice-1] = accountToEdit
                        account.save_accounts(accounts, file_name, password)
                        _accountwin = None
                        print_accounts(accounts)
                elif choice in 'dD':
                    accountToDelete = accounts[iChoice-1]
                    if prompt('Confirm to delete %s (y or n)?' % accountToDelete.title) in 'yY':
                        del accounts[iChoice-1]
                        account.save_accounts(accounts, file_name, password)
                        _accountwin = None
                        print_accounts(accounts)
                else:
                    _accountwin = None
                    print_accounts(accounts)
            else:
                matching_indexes = account.indexes_of_accounts_matching(accounts,choice)
                print_accounts(accounts,filterList=matching_indexes)

 

if __name__ == '__main__':
    curses.wrapper(main)

