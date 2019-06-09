def draw(fails):
    print("HANGMAN DRAW")
    if fails==0:
        print("Good work! Go on!")
    elif fails==1:
        print(f"""




              /
              LEFT {11-fails} FAILS
              """)
    elif fails==2:
        print(f"""




              /|
              LEFT {11-fails} FAILS
              """)
    elif fails==3:
        print(f"""

               |
               |
               |
              /|
              LEFT {11-fails} FAILS
              """)
    elif fails==4:
        print(f"""
               _______
               |
               |
               |
              /|
              LEFT {11-fails} FAILS
              """)
    elif fails==5:
        print(f"""
               _______
               |/
               |
               |
              /|
              LEFT {11-fails} FAILS
              """)
    elif fails==6:
        print(f"""
                _______
               |/     |
               |
               |
              /|
              LEFT {11-fails} FAILS
              """)
    elif fails==7:
        print(f"""
                _______
               |/     |
               |      O
               |
              /|
              LEFT {11-fails} FAILS
              """)
    elif fails==8:
        print(f"""
                _______
               |/     |
               |      O
               |      |
              /|
              LEFT {11-fails} FAILS
              """)
    elif fails==9:
        print(f"""
                _______
               |/     |
               |     \O
               |      |
              /|
              LEFT {11-fails} FAILS
              """)
    elif fails==10:
        print(f"""
                _______
               |/     |
               |     \O/
               |      |
              /|
              LEFT {11-fails} FAIL
              """)
    elif fails==11:
        print(f"""
                _______
               |/     |
               |     \O/
               |      |
              /|     /
              LEFT {11-fails} FAILS
              """)
    elif fails==12:
        print(f"""
                _______
               |/     |
               |     \O/
               |      |
              /|     /|
              YOU ARE DEAD
              """)

