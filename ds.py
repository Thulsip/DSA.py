def merge(arr):
    if len(arr)>1:
        mid=len(arr)//2
        left=arr[:mid]
        right=arr[mid:]
        merge(left)
        merge(right)
        lp=0
        rp=0
        fp=0
        while lp<len(left)and rp<len(right):
            if left[lp]<right[rp]:
                arr[fp]=left[lp]
                lp+=1
            else:
                arr[fp]=right[rp]
                rp+=1
                fp+=1
                while lp<len(left):
                    arr[fp]=left[lp]
                    fp+=1
                    lp+=1
                    while rp<len(right):
                        arr[fp]=right[rp]
                        fp+=1
                        rp+=1
                        print(arr)
