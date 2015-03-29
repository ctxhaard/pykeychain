'''
Created on 29/mar/2015

@author: ctomasin
'''

class Account:
    def __init__(self,t=None,url=None,u=None,p=None,n=None,**other):
        self.title = t
        self.URL = url
        self.username = u
        self.password = p
        self.note = n
        pass
    
    def __repr__(self):
        return """Title: %s
        \tURL: %s
        \tUsername: %s
        \tPassword: %s
        \tNote: %s""" % (self.title,self.URL,self.username,self.password,self.note)
    
    
def load_accounts(file):
    """
    Reads accounts from file
    Returns a generator object giving dictionaries with records
    """
    content = {}

    # record: (url , www.cacca.it)
    for record in (line.split(':') for line in file):
        if len(record) == 0: continue
        # record: (url,www.cacca.it)
        record = list(map(str.strip,record))
        if len(record[0]) == 0:
            continue
        elif record[0][:1] == '-':
            if(len(record)):
                yield Account(**content)
                content = {}
        elif len(record) >= 2:
            key, *value = record
            content[key] = ':'.join(value)
    if len(content.keys()):
        yield Account(**content)

def save_accounts(accounts,file):
    """
    Saves accounts to file
    """
    for account in accounts:
        for key in account.keys:
            file.write('%s:%s\n' % (key,account[key]))
        else:
            file.write('%s\n' % ('-'*3))
    file.close()