sowpod_set = set(sowpod.strip() for sowpod in open("sowpods.txt").readlines())
sonnets = [sonnet.strip() for sonnet in open("sonnet_words.txt").readlines()]

counter = 0
for sonnet in sonnets:
    if(sonnet not in sowpod_set):
        counter = counter +1
        print(sonnet +"Not in sowpod")

print("Total number of sonnets not in sowpod is %d" % counter)
