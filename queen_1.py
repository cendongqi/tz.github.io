from pythonds.basic.queue import Queue


def hotPotato(namelist, num):
    simqueue = Queue()
    for name in namelist:
        simqueue.enqueue(name)

    while simqueue.size() > 1:
        for i in range(num):
            simqueue.enqueue(simqueue.dequeue())
            print(simqueue.size())

        s = simqueue.dequeue()

    return s


print(hotPotato(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'], 3))
