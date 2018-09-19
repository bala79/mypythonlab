import time
sowpods = open("sowpods.txt").readlines()
sowpods = [sowpod.strip() for sowpod in sowpods]

sonnets =  open("sonnet_words.txt").readlines()
sonnets = [sonnet.strip() for sonnet in sonnets]

counter = 0
start =  time.time()
for sonnet in sonnets:
    if(sonnet not in sowpods):
        counter = counter +1
        print(sonnet +"Not in sowpod")
end = time.time()
print("Time Taken %.1f" % (end-start))
print("Total number of sonnets not in sowpod is %d" % counter)
