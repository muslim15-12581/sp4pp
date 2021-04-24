movie = {
    '1':{'title':'Avengers','s1':5, 's2':5, 's3':5},
    '2':{'title':'Spider Man','s1':5, 's2':5, 's3':5}
}

login = {'admin':'admin'}

while True:
    ch = input("Choose option:\n\t1. Login\n\t2. Register\n")

    if ch=='1' or ch=='2':
        user = input('Enter your username:')
        pas = input('Enter your password: ')

        if ch=='1':
            if login[user] == pas:
                print("You are successfully logged in.\n")
                while True:
                    for i in movie:
                        print(i, movie[i]['title'])
                    print('0 Logout')
                    x = input('Enter your choice:')

                    if x=='0':
                        break

                    print('Slot 1: 9.00am to 12.00pm')
                    print('Slot 2: 2.00pm to 05.00pm')
                    print('Slot 3: 6.00pm to 09.00pm')
                    y = input('Choose slot: ')

                    s = int(input('Enter seat number: '))

                    if y=='1':
                        if movie[x]['s1'] >= s:
                            print('Ticket purchased successfully.\n')
                            movie[x]['s1'] -= s
                        else:
                            print('Opps! Only', movie[x]['s1'], 'tickets available.\n')
                    elif y=='2':
                        if movie[x]['s2'] >= s:
                            print('Ticket purchased successfully.\n')
                            movie[x]['s2'] -= s
                        else:
                            print('Opps! Only', movie[x]['s2'], 'tickets available.\n')
                    elif y=='3':
                        if movie[x]['s3'] >= s:
                            print('Ticket purchased successfully.\n')
                            movie[x]['s3'] -= s
                        else:
                            print('Opps! Only', movie[x]['s3'], 'tickets available.\n')

            else:
                print('Wrong username or password!\n')
        elif ch == '2':
            login[user] = pas
            print("You are successfully registered.\n")
    else:
        print('Wrong Choice!')