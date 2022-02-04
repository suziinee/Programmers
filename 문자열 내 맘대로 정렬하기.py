def solution(strings, n):
     d = {}
     for word in strings :
         if word[n] in d.keys() :
             d[word[n]].append(word)
         else :
             d[word[n]] = [word]
     d = dict(sorted(d.items()))
    
     ans = []
     for k, v in d.items() :
         if len(v) == 1 :
             ans.append(v[0])
         else :
             v.sort()
             for word in v :
                 ans.append(word)
    
     return ans