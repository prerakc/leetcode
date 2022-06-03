# 1. Two Sum

## Link
https://leetcode.com/problems/two-sum/

## Solution
Use a hashmap to store numbers (and their corresponding indicies) that you have visited in the list. While iterating, check if the number you would need to add to the current element to produce the desired sum is in the hashmap.

Time complexity: O(n)

Space complexity: O(n)
