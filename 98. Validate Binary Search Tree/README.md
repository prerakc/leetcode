# 98. Validate Binary Search Tree

## Link
https://leetcode.com/problems/validate-binary-search-tree/

## Solution
Traverse the tree in-order and populate a list with the node values. Then verify that each list element is less than or equal to its successor.

Time complexity: O(n)

Space complexity: O(n)
