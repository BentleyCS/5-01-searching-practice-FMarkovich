
import random
def randomSearch(items:list, target) -> int:
    #Modify the below function such that it takes in a list of items and a target value.
    #Randomly choose an item from the list and if it isn't the target value try again.
    #print out the amount of tries it took and return the index of the target value
    x=random.randint(0,len(items)-1)
    while items[x]!=target:
        x=random.randint(0,len(items)-1)
    if items[x]==target:
        return x
    pass

def linearSearch(items:list, target) ->tuple[int,int]:
    #Modify the below function such that it implements linear search.
    #Return the index of the target value and the amount of checks it took
    #if the value is not within the list return -1 as the index.
    x=0
    y=1
    while x<len(items):

        if items[x]==target:
            return (x, y)
        else:
            x+=1
            y+=1
    return (-1,y-1)



def binarySearch(items:list, target) -> tuple[int,int]:
    # Modify the below function such that it implements linear search.
    # Return the index of the target value and the amount of checks it took
    # if the value is not within the list return -1 as the index.
    minimum=0
    maximum=len(items)-1
    checks=0
    while minimum<=maximum:
        checks += 1
        avg=(maximum+minimum)//2
        print (f"avg:{avg}, checks: {checks}")
        if items[avg]==target:
            return avg, checks
        elif items[avg]<target:
            minimum=avg+1
        elif items[avg]>target:
            maximum=avg-1
    return -1, checks


