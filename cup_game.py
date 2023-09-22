def cup_game():
    from random import shuffle
    mylist = [" ", "0", " "]
    print("Here is a glimpse")
    print(mylist)
    print("the cups are shuffled")
    mixedup_list =shuffle(mylist)
    guess='' 
    while guess not in ["0",'1','2']:
        guess=input("Where is the ball? \nPick a number: 0,1,2 \n")
    if mylist[int(guess)]=='0':
        print("corret")
        print(mylist)
    else:
        print("wrong guess!")
        print(mylist)
cup_game()

