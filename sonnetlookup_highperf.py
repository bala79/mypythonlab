sowpods = open("sowpods.txt").readlines()
sowpod_dict = dict((sowpod.strip(),1) for sowpod in sowpods)

sonnets =  open("sonnet_words.txt").readlines()
sonnets = [sonnet.strip() for sonnet in sonnets]


counter = 0
for sonnet in sonnets:
    if(sonnet not in sowpod_dict):
        counter = counter +1
        print(sonnet +"Not in sowpod")

print("Total number of sonnets not in sowpod is %d" % counter)
