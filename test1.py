from pattern.web import Twitter
from pattern.vector import KNN, count
from pattern.text.es import tag

twitter, knn = Twitter(), KNN()

for i in range(1, 3):
    for tweet in twitter.search('#win OR #fail', start=i, count=100):
        s = tweet.text.lower()
        p = '#win' in s and 'WIN' or 'FAIL'
        v = tag(s)
        v = [word for word, pos in v if pos == 'JJ'] # JJ = adjective
        v = count(v) # {'sweet': 1}
        if v:
            knn.train(v, type=p)

print(knn.classify('keonda'))
print(knn.classify('sect'))