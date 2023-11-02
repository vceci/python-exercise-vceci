from movies import Movies

movies = Movies('./movies.txt')

def list():
    for item in movies._movies:
        print(item['name'])

ans=True
while ans:
    print("q: quit \nlist: print all the movie names")
    ans=input()
    if ans=='q':
        ans = None
    elif ans=='list':
        list()
    else:
        ans=True

    