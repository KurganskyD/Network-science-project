import multiprocessing as mp,os
import time

t0 = time.time()

text = []
def process_wrapper(lineID):
    with open("vocab.kos.txt") as f:
        for i,line in enumerate(f):
            if i != lineID:
                continue
            else:
                return line
                break
            
def chunkify(fname,size=100):
    fileEnd = os.path.getsize(fname)
    with open(fname,"rb") as f:
        chunkEnd = f.tell()
        while True:
            chunkStart = chunkEnd
            f.seek(size,1)
            f.readline()
            chunkEnd = f.tell()
            yield chunkStart, chunkEnd - chunkStart
            if chunkEnd > fileEnd:
                break
                
if __name__ == '__main__':

    #init objects
    pool = mp.Pool(4)
    jobs = []
    
    #create jobs
    for chunkStart,chunkSize in chunkify("vocab.kos.txt"):
        print((chunkStart,chunkSize))
        jobs.append( pool.apply_async(process_wrapper,(chunkStart,chunkSize)) )
    
    #wait for all jobs to finish
    for job in jobs:
        text.append(job.get())
    
    #clean up
    pool.close()

    
t1 = time.time()

total = t1-t0