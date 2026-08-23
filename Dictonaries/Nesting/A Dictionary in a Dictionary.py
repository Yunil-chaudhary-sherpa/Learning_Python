#Dictionaries in a dictionary-
Users = {'Amit':{"first":'Amit',
                 'last':'Ray',
                 'marks':{'maths':'78',
                          'science':'65','english':'81'
                          }
                },
          'Sagar':{'first':'Sagar',
                   'last':'Rai',
                   'marks':{"maths":'85',
                            "science":'91',
                            'english':'89'
                            }
                  }
        }
for u, ui in Users.items():
  print('\nUsername: '+u)
  full_name = ui['first']+" "+ui['last']
  marks = ui['marks']
  print("\tFullname :"+full_name)
  print("\tMarks: "+str(marks))