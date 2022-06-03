# 20. Valid Parentheses

## Link
https://leetcode.com/problems/valid-parentheses/

## Solution
Iterate through the string. When you encounter a left parenthesis, add the corresponding right parenthesis to the stack. When you encounter a right parenthesis, make sure the stack is not empty and the popped item matches the current element. Verify the stack is empty post-iteration.

Time complexity: O(n)

Space complexity: O(n)
