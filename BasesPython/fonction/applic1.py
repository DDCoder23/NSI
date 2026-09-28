def ma_fonction2(arg1,arg2,arg3 = 4):
    print (arg1,'et',arg2, 'et',arg3)
ma_fonction2(5,6,arg3=2) # il manque un argument
'''
ma_fonction2(arg3=2,5,3) les arguments ne
sont pas dans l'ordre
'''
ma_fonction2(5,3,arg3=2)
