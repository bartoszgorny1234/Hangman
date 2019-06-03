def check_letter(input_text ,letter,output1):
    output1=list(output1)
    output2=""
    check=False
    for index, element in  enumerate(input_text):
        if element==letter and element != output1[index]:
            output2+=element
            check=True
        else:
            output2+=output1[index]
    return output2, check

#
# list1="abcd efgh ijkl mnop rstu vwxyz"
# list2=str(len(list1)*"*")
# print(list1)
# print(list2)
# print(check_letter(list1," ",list2))

# output=(len("abcd efgh ijkl mnop rstu vwxyz")*"*")
# output2=""
# print(output2+list(output)[1])
