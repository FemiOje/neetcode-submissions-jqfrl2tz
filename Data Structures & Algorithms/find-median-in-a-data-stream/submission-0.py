class MedianFinder:

    def __init__(self):
        self.arr = []
        

    def addNum(self, num: int) -> None:
        self.arr.append(num)
        self.arr.sort()
        

    def findMedian(self) -> float:
        len_arr = len(self.arr)

        if len_arr % 2 == 1: #odd length
            return self.arr[len_arr // 2]
        else: #even length
            return (self.arr[(len_arr // 2) - 1] + self.arr[len_arr // 2] ) / 2

        
        