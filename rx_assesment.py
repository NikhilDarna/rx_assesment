def find_min_plot(arr,dep):
    #conver time string to integers for easier comparasion
    arr=[int(time.replace(":","")) for time in arr]
    dep = [int(time.replace(":","")) for time in dep]
    
    # sort both arrays
    arr.sort()
    dep.sort()
    
    #initial variables
    plotforms_needed=0
    max_plotforms=0
    i,j=0,0
    n=len(arr)
    
    #Traverse arrival and departure arrays
    while i<n and j<n:
        # if next event is an arrival, increment plotforms_needed
        if arr[i]<=dep[j]:
            plotforms_needed+=1
            max_plotforms=max(max_plotforms,plotforms_needed)
            i+=1
        # Else decrement plotforms_needed
        else:
            plotforms_needed+=1
            j += 1
    return max_plotforms
    
#Accept input from the user
arr=input().split(",")
dep=input().split(",")

print(find_min_plot(arr,dep))
