
# These are pre-defined knowledge for my agent 
goalState = {'A' : '0' , 'B' : '0' , 'C' : '0'}
action = 0       # 0 = Clean , 1 = Dirty
cost = 0
roomStates = {'A' : '0' , 'B' : '0' , 'C' : '0'}

#initial input
print ("Enter the starting location of vacuum (A/B/C) = ")
location = input()
print()

for room in roomStates:
    action = input("Enter the state of " + room + " (0 for clean /1 for dirty): ")
    roomStates[room] = action

#General Outputs

print()
print("\nCurrent State: " + str(roomStates))
print("\nGoal state: " + str(goalState))

print("\n Vacuum is placed in location " + location)

if (roomStates != goalState) :
    
    #If the starting location is room A
    if (location == 'A'):
        if (roomStates['A'] == '1'): #if dirty
            roomStates['A'] = '0'
            cost+=1
            print("Location A was dirty\nLocation A has been cleaned\nCost for cleaning is 1.")
            
        if (roomStates == goalState):
            print("Goal state has been met.")
            print("\nPerformance Measurement: " + str(cost))
            
        #If A is clean. Going from A -> B
        else:
            print("\nA is clean")
            print("\nA -> B")
            print("\nCost for moving within rooms = 1")
            cost+=1
            
            if (roomStates['B'] == '1'):#If B is dirty
                roomStates['B'] = '0'
                cost+=1
                print("Location B was dirty\nLocation B has been cleaned\nCost for cleaning is 1.")
                
            if (roomStates == goalState):
                print("Goal state has been met.")
                print("\nPerformance Measurement: " + str(cost))
                
            #As goal state wasn't met, this means that room C is dirty
            else:
                print("\nA and B are clean but C is dirty")
                print("\nB -> C")
                print("\nCost for moving within rooms = 1")
                cost+=1
                
                roomStates['C'] = '0'
                cost+=1
                print("Location C was dirty\nLocation C has been cleaned\nCost for cleaning is 1.")
                
                if (roomStates == goalState):
                    print("Goal state has been met.")
                    print("\nPerformance Measurement: " + str(cost))
                    
    #If the starting location is room B   
    elif (location == "B"):
        if(roomStates['B'] == '1'): #B is dirty
            roomStates['B'] = '0'
            cost+=1
            print("Location B was dirty\nLocation B has been cleaned\nCost for cleaning is 1.")
            
        if (roomStates == goalState):
            print("Goal state has been met.")
            print("\nPerformance Measurement: " + str(cost))
            
        #If B is clean, then we will move to A first
        else:
            print("\nB is clean")
            print("\nB -> A")
            print("\nCost for moving within rooms = 1")
            cost+=1
            
            if(roomStates['A'] == '1'): #A is dirty
                roomStates['A'] = '0'
                cost+=1
                print("Location A was dirty\nLocation A has been cleaned\nCost for cleaning is 1.")
                
                if (roomStates == goalState):
                    print("Goal state has been met.")
                    print("\nPerformance Measurement: " + str(cost))
                
                # As goal state failed, it means that C is still dirty. We will now move from A->B and then B->C
                else:
                    print("\nA is clean")
                    print("\nA -> B")
                    print("\nCost for moving within rooms = 1")
                    cost+=1

                    print("\nB is also clean")
                    print("\nB -> C")
                    print("\nCost for moving within rooms = 1")
                    cost+=1

                    roomStates['C'] = '0'
                    cost+=1
                    print("Location C was dirty\nLocation C has been cleaned\nCost for cleaning is 1.")

                    if (roomStates == goalState):
                        print("Goal state has been met.")
                        print("\nPerformance Measurement: " + str(cost))
            
            elif(roomStates['C'] == '1'): #C is Dirty
                roomStates['C'] = '0'
                cost+=1
                print("Location C was dirty\nLocation C has been cleaned\nCost for cleaning is 1.")
                
                if (roomStates == goalState):
                    print("Goal state has been met.")
                    print("\nPerformance Measurement: " + str(cost))
                
                # As goal state failed, it means that A is still dirty. We will now move from C->B and then B->A
                else:
                    print("\nC is clean")
                    print("\nC -> B")
                    print("\nCost for moving within rooms = 1")
                    cost+=1

                    print("\nB is also clean")
                    print("\nB -> A")
                    print("\nCost for moving within rooms = 1")
                    cost+=1

                    roomStates['A'] = '0'
                    cost+=1
                    print("Location A was dirty\nLocation A has been cleaned\nCost for cleaning is 1.")

                    if (roomStates == goalState):
                        print("Goal state has been met.")
                        print("\nPerformance Measurement: " + str(cost))

    #If the starting location is room C
    elif(location == 'C'):
        if (roomStates['C'] == '1'): #if dirty
            roomStates['C'] = '0'
            cost+=1
            print("Location C was dirty\nLocation C has been cleaned\nCost for cleaning is 1.")
            
        if (roomStates == goalState):
            print("Goal state has been met.")
            print("\nPerformance Measurement: " + str(cost))
            
        #If C is clean. Going from C -> B
        else:
            print("\nC is clean")
            print("\nC -> B")
            print("\nCost for moving within rooms = 1")
            cost+=1
            
            if (roomStates['B'] == '1'):#If B is dirty
                roomStates['B'] = '0'
                cost+=1
                print("Location B was dirty\nLocation B has been cleaned\nCost for cleaning is 1.")
                
            if (roomStates == goalState):
                print("Goal state has been met.")
                print("\nPerformance Measurement: " + str(cost))
                
            #As goal state wasn't met, this means that room A is dirty
            else:
                print("\nB and C are clean but A is dirty")
                print("\nB -> A")
                print("\nCost for moving within rooms = 1")
                cost+=1
                
                roomStates['A'] = '0'
                cost+=1
                print("Location A was dirty\nLocation A has been cleaned\nCost for cleaning is 1.")
                
                if (roomStates == goalState):
                    print("Goal state has been met.")
                    print("\nPerformance Measurement: " + str(cost))
    else:
        print("\nInvalid Start Location")
        
else:
    print("\nAll rooms are already clean")
    print("\nPerformance Measurement: " + str(cost))
