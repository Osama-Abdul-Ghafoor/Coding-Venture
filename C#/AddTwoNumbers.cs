/*
Problem: Add Two Numbers 
Source: https://leetcode.com/problems/add-two-numbers/
Author: Osama Abdul Ghafoor
GitHub: https://github.com/Osama-Abdul-Ghafoor
*/


/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public int val;
 *     public ListNode next;
 *     public ListNode(int val=0, ListNode next=null) {
 *         this.val = val;
 *         this.next = next;
 *     }
 * }
 */

public class Solution
{
    public ListNode AddTwoNumbers(ListNode l1, ListNode l2)
    {
        ListNode resultL = new ListNode();
        ListNode resultHead = resultL;
        ListNode lastNode = null;

        ListNode head1 = l1;
        ListNode head2 = l2;
        int remainder;
        int coeff = 0;

        while (head1 != null || head2 != null)
        {
            int head1Value = 0;
            int head2Value = 0;
            bool head1Exist = head1 != null;
            bool head2Exist = head2 != null;

            if (head1Exist)
                head1Value = head1.val;
            if (head2Exist)
                head2Value = head2.val;

            int value = head1Value + head2Value + coeff;
            remainder = value % 10;
            coeff = value / 10;


            resultL.val = remainder;
            resultL.next = new ListNode();
            lastNode = resultL;
            resultL = resultL.next;

            Console.WriteLine(remainder);

            if (head1 != null)
                head1 = head1.next;
            if (head2 != null)
                head2 = head2.next;
        }
        if (coeff != 0)
            resultL.val = coeff;
        else
            lastNode.next = null;

        return resultHead;
    }
}