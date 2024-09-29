# unification of 2 lists

a = [1,3,5]
b = [1,2,3]                             #since lists allow duplicates i will try to convert the to sets first
c = [6, 7, 8]
def unification(list1, list2, list3):   # i found a code that uses (*lists) instead of putting the amount of lists manually, might need to ask legolas later 
    unified_set = set()                 #the unified_set variable is empty, i used it as a container to convert the lists later into a set
    for lst in list1, list2, list3: 
        unified_set.update(lst)         #here the lists is put into unified_set and turns into a set
    return list(unified_set)            #this converts the set back into lists

result = unification(a, b, c)
print(result)


#text multiplier function

def text_multiplier(a, b):
    result = []
    for number, text in zip(a, b):
        result.append(text * number)
    return ''.join(result)


a = (4, 2, 7)
b = "pan"
output = text_multiplier(a, b)
print(output)
