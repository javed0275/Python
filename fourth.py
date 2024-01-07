#Write a function that capitalizes the first and fourth letters of a name .

def first_fourth(name):

    first_letter= name[0]
    inbetween = name[1:3]
    fourth_letter= name[3]
    rest = name[4:]

    return first_letter.upper()+inbetween+fourth_letter.upper()+rest

print(first_fourth('macdonald'))

