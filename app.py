from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

ProblemList = [
    {
        "name": "Two Sum",
        "link": "https://leetcode.com/problems/two-sum/description/",
        "difficulty": "Easy",
        "topics": ["Array", "Hashing"]
    },
    {
        "name": "Add Two Numbers",
        "link": "https://leetcode.com/problems/add-two-numbers/description/",
        "difficulty": "Medium",
        "topics": ["Linked List", "Math"]
    },
    {
        "name": "Longest Substring Without Repeating Characters",
        "link": "https://leetcode.com/problems/longest-substring-without-repeating-characters/description/",
        "difficulty": "Hard",
        "topics": ["Sliding Window", "Hashing"]
    },
    {
        "name": "Valid Parentheses",
        "link": "https://leetcode.com/problems/valid-parentheses/description/",
        "difficulty": "Medium",
        "topics": ["Stack", "String"]
    },
    {
        "name": "Merge Intervals",
        "link": "https://leetcode.com/problems/merge-intervals/description/",
        "difficulty": "Medium",
        "topics": ["Array", "Sorting", "Greedy"]
    },
    {
        "name": "Best Time to Buy and Sell Stock",
        "link": "https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/",
        "difficulty": "Easy",
        "topics": ["Array", "Dynamic Programming"]
    },
    {
        "name": "Reverse Linked List",
        "link": "https://leetcode.com/problems/reverse-linked-list/description/",
        "difficulty": "Easy",
        "topics": ["Linked List", "Recursion"]
    },
    {
        "name": "Climbing Stairs",
        "link": "https://leetcode.com/problems/climbing-stairs/description/",
        "difficulty": "Easy",
        "topics": ["Dynamic Programming"]
    },
    {
        "name": "Word Ladder",
        "link": "https://leetcode.com/problems/word-ladder/description/",
        "difficulty": "Hard",
        "topics": ["Breadth-First Search", "Graph"]
    },
    {
        "name": "Binary Tree Level Order Traversal",
        "link": "https://leetcode.com/problems/binary-tree-level-order-traversal/description/",
        "difficulty": "Medium",
        "topics": ["Tree", "Breadth-First Search"]
    },
    {
        "name": "Longest Palindromic Substring",
        "link": "https://leetcode.com/problems/longest-palindromic-substring/description/",
        "difficulty": "Medium",
        "topics": ["Dynamic Programming", "String"]
    },
    {
        "name": "Find Median from Data Stream",
        "link": "https://leetcode.com/problems/find-median-from-data-stream/description/",
        "difficulty": "Hard",
        "topics": ["Heap", "Design"]
    },
    {
        "name": "Trapping Rain Water",
        "link": "https://leetcode.com/problems/trapping-rain-water/description/",
        "difficulty": "Hard",
        "topics": ["Array", "Two Pointers", "Dynamic Programming"]
    },
    {
        "name": "Maximum Subarray",
        "link": "https://leetcode.com/problems/maximum-subarray/description/",
        "difficulty": "Easy",
        "topics": ["Array", "Dynamic Programming"]
    },
    {
        "name": "Jump Game II",
        "link": "https://leetcode.com/problems/jump-game-ii/description/",
        "difficulty": "Medium",
        "topics": ["Greedy", "Dynamic Programming"]
    },
    {
        "name": "Median of Two Sorted Arrays",
        "link": "https://leetcode.com/problems/median-of-two-sorted-arrays/description/",
        "difficulty": "Hard",
        "topics": ["Array", "Binary Search"]
    },
    {
        "name": "Course Schedule",
        "link": "https://leetcode.com/problems/course-schedule/description/",
        "difficulty": "Medium",
        "topics": ["Graph", "Topological Sort"]
    },
    {
        "name": "Kth Largest Element in an Array",
        "link": "https://leetcode.com/problems/kth-largest-element-in-an-array/description/",
        "difficulty": "Medium",
        "topics": ["Array", "Sorting", "Heap"]
    }
]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/random-problem')
def random_problem():
    random_problems = random.sample(ProblemList, k=3)
    return jsonify(random_problems)

if __name__ == '__main__':
    app.run(debug=True)
    
