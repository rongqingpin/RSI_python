def sequentialSearch(alist, item):
    pos = 0
    found = False
    while pos < len(alist) and not found:
        if alist[pos] == item:
            found = True
        else:
            pos = pos+1
	  return found

def orderedSequentialSearch(alist, item):
    pos = 0
    found = False
    stop = False
    while pos < len(alist) and not found and not stop:
        if alist[pos] == item:
            found = True
        else:
            if alist[pos] > item:
	                stop = True
	            else:
	                pos = pos+1
   return found

# iterative binary search
def binarySearch(alist, item):
    first = 0
    last = len(alist)-1
    found = False
    while first<=last and not found:
        midpoint = (first + last)//2
        if alist[midpoint] == item:
            found = True
        else:
            if item < alist[midpoint]:
                last = midpoint-1
            else:
                first = midpoint+1
    return found

# recursive binary search: with slicing
def binarySearch(alist, item):
    if len(alist) == 0:
        return False
    else:
        midpoint = len(alist)//2
        if alist[midpoint]==item:
            return True
        else:
            if item<alist[midpoint]:
                return binarySearch(alist[:midpoint],item)
            else:
	            return binarySearch(alist[midpoint+1:],item)
# recursive binary search: without slicing
def binarySearch(alist, first, last, item):
    if first == None and last == None:
        return False
    else:
        midpoint = (last - first + 1))//2
        if alist[midpoint]==item:
            return True
        else:
            if item<alist[midpoint]:
                last = midpoint - 1
                return binarySearch(alist, first, last, item)
            else:
                first = midpoint + 1
	            return binarySearch(alist, first, last, item)
