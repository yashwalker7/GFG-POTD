

//User function Template for Java


/*Complete The Function Provided
Given Below is The Node Of Tree
class Node
{
    int data;
    Node left, right;
    public Node(int data)
    {
        this.data = data;
         left = right = null;
    }
}*/


class Solution{
    //Function to return list containing elements of right view of binary tree.
    ArrayList<Integer> rightView(Node node) {
        //add code here.
        ArrayList<Integer> ans = new ArrayList<Integer>();
        Queue<Node> q = new LinkedList<Node>();
        if (node != null)q.add(node);
        while(!q.isEmpty())
        {
            int size = q.size();
            int val = -1;
            while (size -- > 0)
            {
                Node top = q.poll();
                val = top.data;
                if(top.left != null)q.offer(top.left);
                if(top.right != null)q.offer(top.right);
            }
            ans.add(val);
        }
        return ans;
    }
}
