import pprint as p
import copy
M = [
     [1,1,1,1,1,1],
     [1,1,1,1,1,1],
     [1,1,0,0,1,1],
     [1,1,1,1,1,0],
     [1,0,1,0,0,1],
     [1,1,1,1,1,1]
     ]

M_2 = [
       [1,1,1,1,1,1,1,1,1,1,1,1],
       [1,1,1,1,1,1,1,1,1,1,1,1],
       [1,1,0,0,1,1,1,1,1,1,1,1],
       [1,1,1,1,1,0,1,1,1,1,1,1],
       [1,0,1,0,0,1,1,1,1,1,1,1],
       [1,1,1,1,1,1,1,1,1,1,1,1],
       [0,1,1,1,1,1,1,1,1,1,1,1],
       [1,1,1,1,1,1,1,1,1,1,1,1],
       [1,1,0,0,1,1,1,1,1,1,1,1],
       [1,1,1,1,0,0,1,0,1,1,1,0],
       [1,0,1,0,1,0,0,1,0,0,0,1],
       [1,1,1,1,1,1,1,1,1,1,1,1]
      ]

M_3 = [
       [1,0],
       [1,1]
      ]

def findPath_iter(M):
    if not M or len(M) != len(M[0]): return None
    edge = len(M)-1
    x = y = 0
    res = 0
    path = [(x,y)]
    while not x == y == edge:
        # go right as far as possible and append every (x,y) pair to path
        while y<edge and M[x][y+1] == 1:
            y+=1
            path.append((x,y))
        if y == edge-1 and M[x][y+1] == 1: 
            y+=1
            path.append((x,y))
        # go down as far as possible and append every (x,y) pair to path
        while x<edge and M[x+1][y] == 1:
            x+=1
            path.append((x,y))
        if x == edge-1 and M[x+1][y] == 1:
            x+=1
            path.append((x,y))
        # if the above conditions all failed we have reached a dead end
        # prevent reaching the same dead end twice by setting M[x][y] = 0
        # remove dead end from path and go back to previous position
        if res == x+y:
            M[x][y]=0
            path.pop()
            x,y = path[-1]
        res = x + y
    # values in path are kept when x == y == edge
    # set every value not in path to 0
    for i in range(edge+1):
        for j in range(edge+1):
            if not (i,j) in path:
                M[i][j] = 0
    return M

def clean(M,path):
    for i in range(len(M)):
        for j in range(len(M)):
            if not (i,j) in path:
                M[i][j] = 0
    return M


if __name__ == '__main__':
    
    examples = copy.deepcopy([M_3,M,M_2])
    for i, v in enumerate(examples):
        print('\nExample {}:'.format(i+1))
        print('\nMatrix:\n')
        p.pprint(v)
        print('\nPath:\n')
        p.pprint(findPath_iter(v))
