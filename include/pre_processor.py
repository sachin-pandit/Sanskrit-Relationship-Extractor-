# -*- coding: utf-8 -*-
from include import root_extractor as rx
#from sets import Set
import string

def find_list(dic): #res=>Dict with element key and main word as value (reversing the main->form1,form2,form3 etc.., for synonoyms)
    res={}
    root_keys=dic.keys()
    for ele in root_keys:
        name_keys=dic[ele]
        for n in name_keys:
            res[n]=ele
    return res

def find_relation_tuples(str,names_all,name_rel): #names_all=> Dict with names key and main word as value (addressing synonoymns)
    # #name_rel=> Dict with "n1|n2" keys and relationship value.
    str=str.translate(str.maketrans(",:","  ")).strip() # strip punctuations and replace with space
    tokens=str.split()
    names=set()
    res=[]
    rel=set()
    #print(names_all, name_rel)
    #for name in names_all:
    #    print(name, [ord(c) for c in name], bytes(name, 'utf-8'))
    #names_all=find_list(name_dic)
    #rel_all=find_list(rel_dic)
    for tok in tokens:
        root=rx.root_ext(tok)
        #print(tok, [ord(c) for c in root], bytes(root, 'utf-8'))
        if root in names_all.keys():
            names.add(names_all[root])
    print(names)
    c=[]
    for n1 in names:
        c.append(n1)
        for n2 in [x for x in names if x not in c]:
            n_key=n1+"|"+n2
            n_key_rev = n2+"|"+n1
            if n_key in name_rel:
                rel=name_rel[n_key]
            elif n_key_rev in name_rel:
                rel = name_rel[n_key_rev]
            else:
                return res
            par=[x for x in tokens if x not in [n1,n2]]
            res.append([[n1,n2],rel,par]) #first arg is name pair,second in relationship between them,final is the list of all tokes in the sentence
    print(res)
    return res

if __name__ == "__main__":
    d={"ram":["ram","shriram","shrihari","hareram"],"sita":["sita","lela","lelavati"]}
    x=find_list(d)
    print(x)
    print(find_relation_tuples("ram and sita sitting in a tree",x,{"sita|ram":"married"}))
# We can segment the input text file with "|" symbol as a list of sentences and each is passed to find_relation_tuples
#Use find list to generate names_all argument mentioned.

