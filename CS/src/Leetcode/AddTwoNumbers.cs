// 2. Add Two Numbers

namespace Leetcode
{
    public partial class Algorithm
    {
        public static ListNode AddTwoNumbers(ListNode l1, ListNode l2)
        {
            ListNode result = new ListNode(0);
            ListNode currNode = result;
            int carry = 0;
            int sum = 0;

            for (; l1 != null && l2 != null; l1 = l1.Next, l2 = l2.Next)
            {
                (sum, carry) = GetSum(l1, l2, carry);
                currNode = AppendNode(currNode, sum);
            }

            for (; l1 != null; l1 = l1.Next)
            {
                (sum, carry) = GetSum(l1, l2, carry);
                currNode = AppendNode(currNode, sum);
            }

            for (; l2 != null; l2 = l2.Next)
            {
                (sum, carry) = GetSum(l1, l2, carry);
                currNode = AppendNode(currNode, sum);
            }

            if (carry == 1)
            {
                currNode = AppendNode(currNode, carry);
            }

            /* first node is dummy */
            return result.Next;
        }

        private static (int sum, int newCarry) GetSum(ListNode l1, ListNode l2, int carry)
        {
            int val1 = l1 != null ? l1.Val : 0;
            int val2 = l2 != null ? l2.Val : 0;

            int sum = val1 + val2 + carry;
            int newCarry = sum > 9 ? 1 : 0;
            sum %= 10;

            return (sum: sum, newCarry: newCarry);
        }

        private static ListNode AppendNode(ListNode curr, int val)
        {
            curr.Next = new ListNode(val);
            return curr.Next;
        }
    }
}
