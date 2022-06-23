

domain = set([2, 4, 8, 16])
R1 = [(2, 2),(4,4),(8,8),(2,8),(16,16)]
R2 = [(2, 2), (2, 4), (4, 2), (4, 4), (8, 16), (16, 2), (16, 16),(16,4),(8,2),(8,4)]


def antisymmetric(R,domain):
    for (a, b) in R:
        if (a,b) in R and (b,a) in R and a != b:
            return False
    return True

def reflexive(R, domain):
    
    for a in domain:
        if (a, a) not in R:
            return False
    return True

def transitive(R, domain):
    
    for a in domain:
        for b in domain:
            if (a, b) in R:
                for c in domain:
                    if (b, c) in R and (a, c) not in R:
                        return False
    return True

    
for R in [R1,R2]:
    print("Look at this set: ", R)
    print ("  reflexive: ", reflexive(R, domain))
    print ("  antisymmetric: ", antisymmetric(R, domain))
    print ("  transitive:", transitive(R, domain))
    if antisymmetric(R,domain) == True and reflexive(R,domain) == True and transitive(R,domain) == True:
        print("Because of this set is POset, the hasse diagram can be drawn.")
    else: 
        print("Because of this set is not POset, the hasse diagram cannot be drawn.")
