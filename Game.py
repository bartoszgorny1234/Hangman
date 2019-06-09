from Check_Letter import check_letter
from  Draw import draw
from Words import word_generator



def game(wins=0,lost=0):
    input1 = word_generator()
    output={}
    output[0]=len(input1)*"*"
    fail = 0
    win = wins
    lose = lost
    special = ",!@$%^&*(){}: #.'"
    for sign in special:
        output=check_letter(input1,sign,output[0])
    print('\n' * 50)
    print(f"""
    Welcome to Hangman!
    Try to guess this!
    {output[0]}""")
    while input1 != output[0] and fail!=12:
        letter=str(input("Put your letter here (or final word): "))
        print('\n'*50)
        if letter == input1:
            break
        elif len(letter) == 1:
            output=check_letter(input1,letter,output[0])
            if output[1] == False:
                fail += 1
        else:
            fail += 1
            print("You do something wrong!")
        print(output[0])
        draw(fail)
    if fail==12:
        lose += 1
        print(f'The word is :{input1}')
    else:
        print("CONGRATULATIONS YOU WIN!")
        print(f'The word is :{input1}')
        win +=1
    print(f"YOUR WINS: {win}.")
    print(f"YOUR LOSSES: {lose}.")
    check=True
    while check==True:
        rpl = input("You want to play Again? Y/N: ")
        if rpl.upper() == "Y":
            game(win,lose)
            check=False
        elif rpl.upper() == "N":
            print("Thank you! Good bye!")
            check=False
        else:
            print("You do something wrong!")



if __name__ == '__main__':
    game()