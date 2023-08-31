import random
roll=input("Press 'y' to roll and 'n' to exit:")
roll=roll.lower()
while roll=='y':
    no=random.randint(1,6)
    if no==1:
        print("[-----]")
        print("[     ]")
        print("[  0  ]")
        print("[     ]")
        print("[-----]")
    elif no==2:
        print("[-----]")
        print("[  0  ]")
        print("[     ]")
        print("[   0 ]")
        print("[-----]")
    elif no==3:
        print("[-----]")
        print("[  0  ]")
        print("[  0  ]")
        print("[  0  ]")
        print("[-----]")
    elif no==4:
        print("[-----]")
        print("[0   0]")
        print("[  0  ]")
        print("[0   0]")
        print("[-----]")
    else:
        print("[-----]")
        print("[0 0 0]")
        print("[     ]")
        print("[0 0 0]")
        print("[-----]")
    roll=input("Press 'y' to roll again and 'n' to exit:")