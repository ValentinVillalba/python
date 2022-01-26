def is_valid_walk(walk):
    dic = {"n":0,"s":0,"e":0,"w":0}
    steps = 0
    for i in walk:
        if(i in dic.keys()):
            dic[i] += 1
            steps += 1
    return (steps == 10 and dic["n"] == dic["s"] and dic["e"] == dic["w"])
  
walk = ["n","s","n","e","o","s"]
is_valid_walk(walk)

#imagine count() does not exits.
