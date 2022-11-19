class Solution {
    public static boolean areAnagrams(Node node1, Node node2) {
        // code here
        if (node1 == null && node2 == null) return true;
        if (node1 == null || node2 == null) return false;
        if(node1.data != node2.data) return false;
        return (areAnagrams(node1.left, node2.right) && areAnagrams(node1.right, node2.left));
    }
}
