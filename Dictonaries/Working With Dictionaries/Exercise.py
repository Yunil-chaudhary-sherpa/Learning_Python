'''Use dictionary to store info of a person- firstname, lastname, age, city. Print each info individually.'''
Agent_1 = {'firstname':'Tanzen','lastname':'Dance','Age':'31','City':'Berlin'}
print(Agent_1['firstname'])
print(Agent_1['lastname'])
print(Agent_1["City"])
print(Agent_1['Age'])

'''Use dicitonary to store favourite activities of 5 names. Print each name individually.'''
Nums = {}
Nums['essen'] = 'eat'
Nums['nehmen'] = 'take'
Nums['laufen'] = 'run'
Nums['treffen'] = 'meet'
Nums['lesen'] = 'read'
print(Nums['essen'])
print(Nums['lesen'])
print(Nums['treffen'])
print(Nums['laufen'])
print(Nums['nehmen'])

# Think of  pro three words you’ve learned. Use these words as the keys, and store their meanings as values. Print each words output.
Python_dic = {'.title()':'To capitalize the first letter of a word','.upper()':'To capitalize the whole word','.lower()':'To uncapitalize the whole word'}
print(".title():"+Python_dic['.upper()']+'.')
print('.lower()'+Python_dic['.lower()']+'.')
print('.upper'+Python_dic['.title()']+'.')