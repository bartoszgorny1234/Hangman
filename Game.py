from Check_Letter import check_letter

def game(input1):
    output=len(input1)*"*"
    output=check_letter(input1," ",output)
    print(f"""
    Welcome to Hangman!
    Try to guess this!
    {output[0]}""")
    while input1!=output[0]:
        letter=str(input("Put your letter here : "))
        output=check_letter(input1,letter,output[0])
        if output[1]==False:
            pass #funkcja rysowania
        print(output)






list1 = "abcd ijkl mnop rstu vwxyz"
game(list1)