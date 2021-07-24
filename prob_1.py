# participate 1
print("Input all marks of participate1:")
p1 = [int(i) for i in input(). split()]
participate1 = 0
for i in range (0, len(p1)):
    participate1 = participate1 + p1[i]

# participate 2
print("Input all marks of participate2:")
p2 = [int(i) for i in input(). split()]
participate2 = 0
for i in range (0, len(p2)):
    participate2 = participate2 + p2[i]

# participate 3
print("Input all marks of participate3:")
p3 = [int(i) for i in input(). split()]
participate3 = 0
for i in range (0, len(p3)):
    participate3 = participate3 + p3[i]

# # sort mark
# mark = [participate1, participate2, participate3]
# mark.sort()

def largest(participate1, participate2, participate3):
    if (participate1 > participate2 and participate1 > participate3 ):
        print (f"Top mark scored by {participate1 = }")
    elif (participate2 > participate1 and participate2 > participate3):
        print (f"Top mark scored by {participate2 = }")
    elif (participate3 > participate1 and participate3 > participate2):
        print (f"Top mark scored by {participate3 = }")
    elif (participate3 == participate1 and participate3 > participate2):
        print (f"Top mark scored by {participate1 and participate3 = }")
    elif (participate1 == participate2 and participate1 > participate3 ):
        print (f"Top mark scored by {participate1 and participate2 = }")
    elif (participate2 > participate1 and participate2 == participate3):
        print (f"Top mark scored by {participate2 and participate3 = }")
    else:
        print ("All participates got = ", participate1)
        
def smallest(participate1, participate2, participate3):
    if (participate1 < participate2 and participate1 < participate3 ):
        print (f"Lowest mark scored by {participate1 = }")
    elif (participate2 < participate1 and participate2 < participate3):
        print (f"Lowest mark scored by {participate2 = }")
    elif (participate3 < participate1 and participate3 < participate2):
        print (f"Lowest mark scored by {participate3 = }")
    elif (participate3 == participate1 and participate3 < participate2):
        print (f"Lowest mark scored by {participate1 and participate3 = }")
    elif (participate1 == participate2 and participate1 < participate3 ):
        print (f"Lowest mark scored by {participate1 and participate2 = }")
    elif (participate2 < participate1 and participate2 == participate3):
        print (f"Lowest mark scored by {participate2 and participate3 = }")
    else:
        participate1 = participate2

largest(participate1, participate2, participate3)
smallest(participate1, participate2, participate3)

# avg score
total = participate1 + participate2 + participate3
avg = total/3
print("Avg Score:", avg)