import bs4
import requests


def find_start_end(first_l):
    if "a" == first_l:
        start = 1
        end = 18
    elif "b" == first_l:
        start = 18
        end = 33
    elif "c" == first_l:
        start = 33
        end = 67
    elif "d" == first_l:
        start = 67
        end = 91
    elif "e" == first_l:
        start = 91
        end = 106
    elif "f" == first_l:
        start = 106
        end = 120
    elif "g" == first_l:
        start = 120
        end = 12
    elif "h" == first_l:
        start = 127
        end = 136
    elif "i" == first_l:
        start = 137
        end = 153
    elif "j" == first_l:
        start = 153
        end = 155
    elif "k" == first_l:
        start = 155
        end = 158
    elif "l" == first_l:
        start = 158
        end = 169
    elif "m" == first_l:
        start = 169
        end = 189
    elif "n" == first_l:
        start = 189
        end = 198
    elif "o" == first_l:
        start = 198
        end = 206
    elif "p" == first_l:
        start = 206
        end = 234
    elif "q" == first_l:
        start = 234
        end = 236
    elif "r" == first_l:
        start = 236
        end = 252
    elif "s" == first_l:
        start = 252
        end = 288
    elif "t" == first_l:
        start = 288
        end = 305
    elif "u" == first_l:
        start = 305
        end = 309
    elif "v" == first_l:
        start = 309
        end = 316
    elif "w" == first_l:
        start = 316
        end = 323
    elif "x" == first_l:
        start = 324
        end = 325
    elif "y" == first_l:
        start = 325
        end = 325
    elif "z" == first_l:
        start = 325
        end = 326

    return start, end


def inbuiltTagGen(user_tags):
    inbuilt_tags = []
    for j in range(0,len(user_tags)):
        word=user_tags[j]
        start, end = find_start_end(word[0])
        for i in range(start, end + 1):
            url1 = "https://www.oxfordreference.com/view/10.1093/acref/9780199688975.001.0001/acref-9780199688975?btog=chap&hide=true&page="
            url2 = "&pageSize=20&skipEditions=true&sort=titlesort&source=%2F10.1093%2Facref%2F9780199688975.001.0001%2Facref-9780199688975"
            no = str(i)
            url = url1 + no + url2
            res = requests.get(url)
            soup = bs4.BeautifulSoup(res.text, 'html.parser')
            soup2 = soup.find(id="searchContent")

            soup3 = soup2.findAll("div", {
                "class": "contentItem oxencycl-entry locked hasCover chunkResult hi-visible p-4 border-top"})
            print("website pass")
            for j in range(0, len(soup3)):
                string = soup3[j].getText()
                string2 = string.split()
                #print(string2)
                for i in range(0, len(string2)):
                    inbuilt_tags.append(string2[i].lower())


    return inbuilt_tags




def user_entry():
    string = input("Enter string- ")
    string=string.lower()
    print(string)
    indv_words = string.split()
    return indv_words

#matching user-tags with inbuilt-tags
def find_tags(inbuilt_tags, user_tags):
    match_tags=[]

    for i in range(0,len(user_tags)):
        for j in range(0,len(inbuilt_tags)):
            if user_tags[i]==inbuilt_tags[j]:
                match_tags.append(user_tags[i])
                break
            #else:
            #   print(user_tags[i]+"!="+inbuilt_tags[j])

    return match_tags


def convert_int(list):
    try:
    # Converting integer list to string list
        s = [str(i) for i in list]

        # Join list items using join()
        res = int("".join(s))

        return (res)
    except:
        print("Technical Snag!!!")
        return -999


def decimalToBinary(n):
    return bin(n).replace("0b", "")


'''def get_digits(num,tag_marker,count,length):
    count=count+1
    print(num)
    print("count:",count)
    if num < 10:
        #print(num)

        tag_marker.append(str(num))

    else:
        get_digits(num // 10,tag_marker,count,length)
        tag_marker.append(str(num%10))

    count=count+1

    print("length:",length," count:",count)
    if count==length or count==length-1:
        return tag_marker'''


def get_digits(n, tag_marker, count, length):
    try:
        digits = [int(x) for x in str(n)]
        for i in range(0, len(digits)):
            s = str(digits[i])
            tag_marker.append(s)

        return 1,tag_marker
    except:

        return 0,[]


def ret_tags(tags, last_index, tag_arg):
    try:
        tag_marker = []
        new_tag = []
        count = 0
        last_index = last_index - 1
        bin_last_index = decimalToBinary(last_index)
        bin_last_index = int(bin_last_index)
        # print("id:",id(tag_marker))
        # print("tag len:",len(tags))
        # print(type(bin_last_index))
        snag,tag_marker = get_digits(bin_last_index, tag_marker, count, len(tags))
        # print(tag_marker)
        if(snag==1):
            for i in range(0, len(tag_arg)):
                # print("tag_marker:",tag_marker[i]," tag_arg:",tag_arg[i])
                if int(tag_marker[i]) != 0:
                    # print("val tag_marker",tag_marker[i])
                    new_tag.append(tag_arg[i])
                    # print("appended: ",new_tag[i])

            return new_tag, tag_marker,1
        else:
            yyy=1/0
    except:
        print("Techincal Snag!!!!")
        return new_tag, tag_marker,0


def stack_access(tag_arg):
    tags = tag_arg
    flag = 1
    snag=1
    while (True):
        if(snag==0):
            print("Exit due to error")
            break
        try:
            # print("in try block:",tags)
            url = "https://stackoverflow.com/tags/"
            count = 0
            for tag in tags:
                if count == 0:
                    url = url + tag
                    count = count + 1
                else:
                    url = url + "+" + tag

            print(url)

            res = requests.get(url)
            # print(res.text)

            soup = bs4.BeautifulSoup(res.text, 'html.parser')

            # soup2=soup.find(id="question-summary-57101356")
            # str=soup2.find("a", {"class": "question-hyperlink"}).getText()
            # print(str)

            soup2 = soup.find(id="questions")
            qs_summary = soup2.findAll("div", {"class": "question-summary"})
            length = len(qs_summary)
            try:
                for i in range(0, 15):
                    qs = qs_summary[i].find("a", {"class": "question-hyperlink"})
                    string = qs.getText()
                    hyper_l = "https://stackoverflow.com" + qs.get('href')
                    print(i,".",string)
                    print("Link:", hyper_l)
                    # string-matching alogorithm with user's input

                # print("Last ",qs.getText())
                break
            except:
                print("--END Result----")
                break
        except:
            # print("Oopsie")
            tag_marker = []
            if flag == 1:
                last_index = (2 ** (len(tags))) - 1
                flag = 0
            # print("fail:-",last_index)
            tags, tag_marker,snag = ret_tags(tags, last_index, tag_arg)
            # print("Hello")
            tag_marker_int = convert_int(tag_marker)
            if(tag_marker_int==-999):
                snag=0
                break
            # print("tag_maker:",tag_marker," tag_marker_int:",tag_marker_int)
            s = str(tag_marker_int)
            # print(type(s))
            last_index = int(s, 2)
            # print("LAST_INDEX:",last_index)

    if(snag==0):
        return 0
    else:
        return 1





def matcher(choice,tags):
    c=1
    while(c==1):
        if choice == 1:
            flag = stack_access(tags)

        if choice==2:
            user_tags = user_entry()
            inbuilt_tags= inbuiltTagGen(user_tags)
            match_tags=find_tags(inbuilt_tags, user_tags)
            #match_tags=user_tags
            flag=stack_access(match_tags)
            tags=match_tags
            choice=1


        if(flag==0):
            c=int(input("Would you like to restart the same search(1:Yes/0:No)?"))

        if(flag==1):
            break

    temp=int(input("Do another Search?(1:Yes/0:No)"))
    return temp

#---------------------------------------------------------------------------------------

def main():
    i=1
    while(i!=3):
        exit=0
        print("\n\n-----------------SEARCHING FOR USER QUERY ON STACKOVERFLOW-------------------")
        print("1.Search by Tags(Recommended)")
        print("2.Search by Query(Still in Development)")
        print("3.Exit")
        try:
            exit=int(input("Enter your choice(1/2/3)- "))
            if(exit==3):
                break
            while(exit!=3):
                if(exit==1):
                    print("------SEARCH BY TAGS-------\n")
                    print("Enter a tag and press ""Enter"" to provide the next tag")
                    print("When done type 'done' to continue.")
                    tags = []
                    while (True):
                        string = input("Enter Tag: ")
                        if string.upper() == "DONE":
                            break
                        tags.append(string)
                    #print(tags)
                    if(tags==[]):
                        print("No tags were entered.")
                        print("Program Restarts.")
                        temp=1
                    else:
                        temp=matcher(exit,tags)

                if(exit==2):
                    print("\n------SEARCH BY QUERY-------")
                    print("NOTE: MIGHT TAKE A WHILE!!!!")
                    print("NOTE:Try to avoid spelling mistakes")
                    print("Please wait as we Load the results\n")
                    temp=matcher(exit,[])
                if(exit==3):
                    break
                if(temp!=0):
                    print("1.Search by Tags(Recommended)")
                    print("2.Search by Query")
                    print("3.Exit")
                    exit = int(input("Enter your choice(1/2/3)- "))

                if(temp==0):
                    break

                else:
                 print("Not a available option.")
        except:
            print("Error: Invalid entry\n Programs Restart.\n")




    print("Program terminated")




#----main()---------------------------------------->>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
if __name__ == "__main__":
    main()
