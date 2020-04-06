from collections import defaultdict


def groupAnagrams(strs):
        dicti = defaultdict(list)
        sam=[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]
        for i in strs:
            sume=1
            for l in i:
                sume*=sam[ord(l)-97]
            dicti[sume].append(i)
        arr=[]
        for value in dicti.values():
            arr.append(value)
        return(arr)