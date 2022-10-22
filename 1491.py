class Solution:
    def average(self, salary: List[int]) -> float:
        sum_sal = 0
        count =0
        for i in salary: 
            if i!=max(salary) and i!=min(salary):
                sum_sal += i
                count +=1
        return (sum_sal/count)
