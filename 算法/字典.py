voted= {}
def check(name):
    if voted.get(name):
        print('get out')
    else:
        voted[name]=True
        print('vote')
        print(voted)

# check('tom')
# check('mike')
# check('tom')


