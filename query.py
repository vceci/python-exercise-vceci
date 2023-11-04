from movies import Movies

movies = Movies('./movies.txt')

def list():
    for item in movies._movies:
        print(item['name'])

def search_name():
    word = input("Enter a search term: ")
    for item in movies._movies:
        if word.lower() in item['name'].lower():
            print(item['name'])

def search_cast():
    word = input("Enter a search term: ")
    for item in movies._movies:
        z = [a.lower() for a in item['cast']]
        for items in z:
            if word.lower() in items:
                print(item['name'])
                print(items)

ans=True
while ans:
    print("\nq: quit \nlist: print all the movie names \nsn: search movie names \nsc: search cast")
    ans=input()
    if ans=='q':
        ans = None
    elif ans=='list':
        list()
    elif ans=='sn':
        search_name()
    elif ans=='sc':
        search_cast()
    else:
        ans=True