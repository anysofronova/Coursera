#Cравнение предложений

import re
import collections
from scipy.spatial import distance

token_texts = []
for i in texts:
    t = re.split('[^a-z]', i)
    t = [x for x in t if x]
    token_texts.append(t)

full = []
for i in token_texts:
    full += i

counter = collections.Counter(full)

dictionary = list(dict(counter).keys())
A = np.zeros((len(token_texts), len(dictionary)))
for i in range(len(token_texts)):
    count = collections.Counter(token_texts[i])
    for j in range(len(dictionary)):
        A[i,j] = count[dictionary[j]]
        
dist = [[] for i in range(len(token_texts)-1)]
for i in range(1, len(token_texts)):
    dist[i-1].append(distance.cosine(A[0], A[i]))
    dist[i-1].append(i)
    
k = sorted(dist)[:2]
l = str(k[0][1]) + ' ' + str(k[1][1])

with open('file.txt', 'w') as file:
    file.write(l)
    
#6 4
