text = "New to Python or choosing between Python 2 or Python 3? Read Python 2 or Python 3."

text_list = text.split(" ")
print(text_list)
for i in text_list:
    if text_list.count(i) > 0:
        print(i ,"=" ,text_list.count(i))