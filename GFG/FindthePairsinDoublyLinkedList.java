
/*

Definition for singly Link List Node
class Node
{
    int data;
    Node next,prev;
    
    Node(int x){
        data = x;
        next = null;
        prev = null;
    }
}

You can also use the following for printing the link list.
Node.printList(Node node);
*/

class Solution {
    public static ArrayList<ArrayList<Integer>> findPairsWithGivenSum(int target, Node head) {
        Node curr = head;
        int size = getfullsize(head);
        Node tail = get(head,size-1);
        Node start = head;
        Node end = tail;
        
        
        ArrayList<ArrayList<Integer>> list = new ArrayList<>();
        while(start.data<end.data){
            ArrayList<Integer> pair = new ArrayList<>();
            if((start.data + end.data) == target){
                pair.add(start.data);
                pair.add(end.data);
                list.add(pair);
                start = start.next;
                end = end.prev;
            }
            else if((start.data + end.data) < target){
                start = start.next;
            }
            else if((start.data + end.data) > target){
                end = end.prev;
            }
        }
        return list;
    }   
    
    public static int getfullsize(Node head){
        Node curr = head;
        int size = 0;
        while(curr!=null){
            size +=1;
            curr = curr.next;
        }
        return size;
    }
    
    public static int getsize(Node head,Node tail){
        Node curr = head;
        int size = 0;
        while(curr!=null){
            size +=1;
            curr = curr.next;
        }
        return size;
    }
    
    public static Node get(Node head,int index) {
        Node node = head;
        for (int i = 0; i < index; i++) {
            node = node.next;
        }
        return node;
    }
}
        