'''
Created on 29/mar/2015

@author: ctomasin
'''

class Account:
    def __init__(self,t=None,url=None,u=None,p=None,n=None,**others):
        self.title = t
        self.URL = url
        self.username = u
        self.password = p
        self.note = n
        self.others = others
        pass
    
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
        result = """Title: %s
\tURL: %s
\tUsername: %s
\tPassword: %s
\tNote: %s""" % (self.title,self.URL,self.username,self.password,self.note)
        if None != self.others:
            result = result + '\n\tOther: %s' % self.others
        return result
    
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
        file.write(repr(account))
    file.close()