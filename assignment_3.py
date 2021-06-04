names_list = ["bob","jimmy","max b","bernie","jordan","future hendrix"]
longest_name = ("")
for string in names_list:
    if len(string) > len(longest_name):
        longest_name = string
    else:
        print(longest_name)