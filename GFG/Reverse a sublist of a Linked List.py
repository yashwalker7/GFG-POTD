class Solution:
    def reverseBetween(self, head, m, n):
        temp = head
        ar = []
        i = 0
        while(temp):
            i+= 1
            if i >= m and i<= n:
                ar.append(temp.data)
            temp = temp.next
        ar = ar[::-1]
        
        temp = head
        root = temp
        i = 0
        j = 0
        while(temp):
            i+= 1
            if i >= m and i<= n:
                temp.data = ar[j]
                j+=1
            temp = temp.next
            
        return head