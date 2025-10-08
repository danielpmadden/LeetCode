# LRU Cache (Python)

**Difficulty:** Medium  
**Category:** Design / Data Structures  
**LeetCode Link:** [https://leetcode.com/problems/lru-cache/](https://leetcode.com/problems/lru-cache/)

## Description
This repository contains a Python implementation of the **Least Recently Used (LRU) Cache** problem from LeetCode.  
The goal is to design a data structure that supports O(1) time complexity for both `get` and `put` operations, while automatically evicting the least recently used element when the cache exceeds its capacity.

## Approach
The solution combines two data structures:
- **Hash Map** for direct key lookups in O(1)
- **Doubly Linked List** for tracking the order of usage and managing eviction in O(1)

The most recently used items are kept near the head, and the least recently used item near the tail.

## Files
- `solution.py` – Full Python implementation
- `explanation.md` – Step-by-step reasoning and breakdown of the approach
- `leetcode-page.pdf` – Snapshot of the original problem
- `submission-details.pdf` – Accepted LeetCode submission details