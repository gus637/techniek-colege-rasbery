def modes(pos_mode:list[str]|tuple[str],mode:list[str]|tuple[str])-> str:
    
    #print(mode)
    code=str()
    for item in pos_mode:
        #print(item)
        if item in mode:
            code=code+"1"
            #print("true")
        else: 
            code=code+"0"
            #print("false") #bug
    #for item in mode:      #
    #    print(item)        #bug
    return code

def getNum(min:int,max:int,*defalt_num:int) -> int:
    try:
        num=int(input())

    except TypeError:
            print("pleas type a number")
            num=getNum(min,max)

    except KeyboardInterrupt:
        raise

    except RecursionError:
            try:
                defalt_num

            except NameError:
                return none

            else:
                return defalt_num[0]

    else:    
        if num < min or num >max:
            print("not in range")
            num=getNum(min,max)

            return num


def menu(options:list[str]|tuple[str],msg:str,*mode:str) -> int|str:
    """
    inport this to make a simpel menu for the user

    how to use:
    
    put a LIST with options in the first slot and a msg in the second
    then you can set the mode for the output:"int" or "str"
    mode
    "int"=makes te menu return a integer (on by default)
    "str"=make the menu return a string.

    you can also set it so that multiple choices can be made by entering "multi"
    """

    
    
    code=modes(["exit","str","multi","bug"],mode)#0="exit" 1="str"/"int" 2="multi" 3="bug"
    
    true="1"
    num=0
    str_len=0                         #
    num_len=len(str(len(options)))-1  #
    items=""
    chois=0
    coiss=[]
    if code[3]==true:
        print(code)
    if code[0]==true:
        return "exit"
    for item in options:       #iterats tru all the items in the given list of options and sets "str_len"'s integer to the len of the longest string
        if str_len<len(item):  #looks at "str_len" and the curent item to see if the item's len is diger then the last item's len
            str_len=len(item)  #if so sets "str_len" to the diger numder
    str_len+=2                 #ads 2 to the num of "str_len" 
            
    print("\n\n","                               ",msg)             #prints the given msg at the top of the menu
    print("                               ","_"*(str_len+7+num_len))#prints the top line of the menu (the line's len is dependent of the longest string
    for item in options:                                              #              
       num+=1                                                         #
       p1=str_len-len(item)                                           #
       p2=" "*p1                                                      #
       p3=len(str(num))-1
       print("                               |",num," "*(num_len-p3)+"|",item,p2,"|")
    print("                               |___"+"_"*num_len+"|"+"_"*(str_len+3)+"|")
    
    if code[2]==true:
        print("type the numbers of with optionc you want to choos")

    else:
        print("type the number of the option that you want to choos")

    if code[2]==true:
        while exit != True:
            chois=0
        for str1 in chois:
            print ("not finist")
            yield str1

    else:
        chois=getNum(1,num)
        if code[1]==true:
            return options[chois-1]
        else:
            return chois