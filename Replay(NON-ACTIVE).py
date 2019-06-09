def Replay(function_to_replay):                                                             #NIE DZIAŁA JAKBYM TEGO CHCIAŁ
    rpl = input("You want to play Again? Y/N: ")
    if rpl.upper() == "Y":
        print("YES")
        function_to_replay
    elif rpl.upper() == "N":
        print("Thank you! Good bye!")
    else:
        Replay(function_to_replay)

#Replay(print("NIE ROZUMIM"))