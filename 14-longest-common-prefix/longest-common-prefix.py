class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        '''if len(strs)==1:
            return strs[0]
        
        i=x=j=y=0
        temp=res=""
        while i < len(strs[0]):
            j=strs[1].find(strs[0][i])
            if j!= -1:
                
                while i+x<len(strs[0]) and j+y<len(strs[1]):
                    if strs[0][i+x]==strs[1][j+y]:
                        x,y=x+1,y+1
                    else:
                        break
                temp=strs[0][i:i+x]
                #b=1
                c=0
                for b in range(len(temp)):
                    for a in range(2,len(strs)):
                        if strs[a].find(temp[:b+1]) ==-1:
                            c=1
                            break
                    if c==0:
                        res=res+temp[b]
                        i+=1
                        
                    else:
                        break
                if res:
                    return res
            i+=1
        
        return res'''
        
        a = ''
        if len(strs[0]) == 0:
            print('hi')
            return a
        t = min(strs)
        for j in range(len(t)):
            
            for i in strs:
                if i[j] == t[j]:
                    pass
                else:
                    return a
            a = a+t[j]
        return a