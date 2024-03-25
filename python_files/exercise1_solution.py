from collections import deque
 
 
# Function to generate binary numbers between 1 and `n` using the
# queue data structure
def generate(n):
 
    # create an empty queue and enqueue 1
    q = deque()
    q.append('1')
 
    # run `n` times
    for i in range(n):
        # remove the front element
        front = str(q.popleft())
 
        # append 0 and 1 to the front element of the queue and
        # enqueue both strings
        q.append(front + '0')
        q.append(front + '1')
 
        # print the front element
        print(front, end=' ')
 
 
if __name__ == '__main__':
 
    n = 16
    generate(n)
