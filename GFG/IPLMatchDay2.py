
class Solution:
    def max_of_subarrays(self,arr,n,k):
        '''
        you can use collections module here.
        :param a: given array
        :param n: size of array
        :param k: value of k
        :return: A list of required values 
        '''

        st=[]

        ans=[]

        for i in range(k):

            if len(st)==0:

                st.append(i)

            else:

                while st:

                    x=st[-1]

                    if arr[x]<=arr[i]:

                        st.pop()

                    else:

                        st.append(i)

                        break

                else:

                    st.append(i)

        ans.append(arr[st[0]])

        for i in range(k,n):

            if st[0]<=i-k:

                st.pop(0)

            while st:

                if arr[st[-1]]<=arr[i]:

                    st.pop()

                else:

                    st.append(i)

                    break

            else:

                st.append(i)

            ans.append(arr[st[0]])

        return ans
