def is_valid_walk(walk):
    dic = {"n":0,"s":0,"e":0,"w":0}
    for i in walk:
        if(i in dic.keys()):
            dic[i] += 1
    return (len(walk) == 10 and dic["n"] == dic["s"] and dic["e"] == dic["w"])
  
walk = ["n","s","n","e","w","s","e","e","w","w"]
is_valid_walk(walk)

#condition: imagine count() does not exist.
