'''
Created on 29/mar/2015

@author: ctomasin
'''
import os
import shutil
from datetime import datetime
import sys
import re

class Account:
    def __init__(self,t=None,url=None,u=None,p=None,n=None,**others):
        self.title = t
        self.URL = url
        self.username = u
        self.password = p
        self.note = n
        self.others = ((others.keys() and others) or None)
    
    def __repr__(self):
        result = """---
t: %s
url: %s
u: %s
p: %s
n: %s
""" % (self.title,self.URL,self.username,self.password,self.note)
        if None != self.others:
            rows = [': '.join((key,self.others[key])) for key in self.others]
            result += '\n'.join(rows)
        return result
        
    
    def __str__(self):
        result = """1 Title: %s
2 URL: %s
3 Username: %s
4 Password: %s
5 Note: %s""" % (self.title,self.URL,self.username,self.password,self.note)
        if None != self.others:
            result = result + '\nOthers: %s' % self.others
        return result

    def matches(self,keyword):
        attributes = dir(self)
        for attr in attributes:
            value = getattr(self,attr)
            if isinstance(value,str) and re.search(keyword,value,flags=re.IGNORECASE):
                return True
        return False
    
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
    content = {}
    key = None
    # linea tipica:url: www.cacca.it
    for line in file:
        # print(type(line)) => <class 'str'>
        record = line.split(':')
        # record: (url,www.cacca.it)
        record = list(map(str.strip,record))

        if len(record) == 1:
            if record[0][:1] == '-':
                # separatore di record
                if(len(content.keys())):
                    yield Account(**content)
                    content = {}
            elif key != None:
                # campi composti da più righe
                content[key] = '\n\t'.join((content[key],record[0]))
            continue
        else:
            key, *value = record
            content[key] = ':'.join(value)
    if len(content.keys()):
        yield Account(**content)

def save_accounts(accounts,file_name,password):
    """
    Saves accounts to file
    """
    shutil.copy(file_name,bkp_filename(file_name))
    out_file = open_encrypt(file_name,password)

    for account in accounts:
        # print(account.title)
        out_file.write(repr(account))
    out_file.close()
    
def bkp_filename(file_name):
    strDate = datetime.now().strftime('%Y%m%d%H%M%S')
    result = file_name + '_' + strDate + '.bkp'
    return result

def indexes_of_accounts_matching(accounts,keyword):
    """
    Returns a list of accounts having keyword in one of its attributes
    """
    result = []
    for (index,account) in enumerate(accounts):
        if account.matches(keyword): result.append(index)
    return result



