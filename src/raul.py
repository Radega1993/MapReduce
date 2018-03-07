import thread
import threading
import time

finalResults = {}

threadLock = threading.Lock()

# Define a function for the thread
def mapreduce( threadNum, nothing):
    data = [
                ["deer", "bear", "river"],
                ["car", "car", "river"],
                ["deer", "car", "bear"],
           ]

    count = {}
    for val in data[threadNum]:
        if val in count:
            count[val] += 1
        else:
            count[val] = 1

    for val in count:
    	threadLock.acquire()
        if val in finalResults:
            finalResults[val] += count[val]
        else:
            finalResults[val] = count[val]
        threadLock.release()

# Create two threads as follows
for i in range(1000):
    finalResults = {}
    try:
        thread.start_new_thread( mapreduce, (0,0) )
        thread.start_new_thread( mapreduce, (1,0) )
        thread.start_new_thread( mapreduce, (2,0) )
    except:
        print "Error: unable to start thread"
        raise
    time.sleep(0.2)
    print finalResults
    assert finalResults == {'car': 3, 'river': 2, 'deer': 2, 'bear': 2}

print finalResults