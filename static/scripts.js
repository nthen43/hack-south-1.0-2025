let topic_container = ["Array", "Hashing"];

document.querySelector('.show-tags').addEventListener('click', function() {
    const topics = topic_container;
    displayTopics(topics);
});

function displayTopics(topics) {
    const tagContainer = document.querySelector('.tag-container');
    const button = document.querySelector('.show-tags');
    const blur = document.querySelector('.blur-background');

    button.classList.remove('fade-in');
    button.classList.add('fade-out');
    blur.classList.add('fade-out');

    setTimeout(function() {
        tagContainer.innerHTML = '';

        topics.forEach(function(topic, index) {
            const topicElement = document.createElement('a');
            topicElement.classList.add('topic');
            topicElement.textContent = topic;
            tagContainer.appendChild(topicElement);

            setTimeout(function() {
                topicElement.classList.add('fade-in');
            }, 200 * index + 100);
        });
    }, 700);
}

const problems = [
    {
        name: "Two Sum",
        link: "https://leetcode.com/problems/two-sum/description/",
        difficulty: "Easy",
        topics: ["Array", "Hashing"]
    },
    {
        name: "Add Two Numbers",
        link: "https://leetcode.com/problems/add-two-numbers/description/",
        difficulty: "Medium",
        topics: ["Linked List", "Math"]
    },
    {
        name: "Longest Substring Without Repeating Characters",
        link: "https://leetcode.com/problems/longest-substring-without-repeating-characters/description/",
        difficulty: "Hard",
        topics: ["Sliding Window", "Hashing"]
    },
    {
        name: "Valid Parentheses",
        link: "https://leetcode.com/problems/valid-parentheses/description/",
        difficulty: "Medium",
        topics: ["Stack", "String"]
    },
    {
        name: "Merge Intervals",
        link: "https://leetcode.com/problems/merge-intervals/description/",
        difficulty: "Medium",
        topics: ["Array", "Sorting", "Greedy"]
    },
    {
        name: "Best Time to Buy and Sell Stock",
        link: "https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/",
        difficulty: "Easy",
        topics: ["Array", "Dynamic Programming"]
    },
    {
        name: "Reverse Linked List",
        link: "https://leetcode.com/problems/reverse-linked-list/description/",
        difficulty: "Easy",
        topics: ["Linked List", "Recursion"]
    },
    {
        name: "Climbing Stairs",
        link: "https://leetcode.com/problems/climbing-stairs/description/",
        difficulty: "Easy",
        topics: ["Dynamic Programming"]
    },
    {
        name: "Word Ladder",
        link: "https://leetcode.com/problems/word-ladder/description/",
        difficulty: "Hard",
        topics: ["Breadth-First Search", "Graph"]
    },
    {
        name: "Binary Tree Level Order Traversal",
        link: "https://leetcode.com/problems/binary-tree-level-order-traversal/description/",
        difficulty: "Medium",
        topics: ["Tree", "Breadth-First Search"]
    },
    {
        name: "Longest Palindromic Substring",
        link: "https://leetcode.com/problems/longest-palindromic-substring/description/",
        difficulty: "Medium",
        topics: ["Dynamic Programming", "String"]
    },
    {
        name: "Find Median from Data Stream",
        link: "https://leetcode.com/problems/find-median-from-data-stream/description/",
        difficulty: "Hard",
        topics: ["Heap", "Design"]
    },
    {
        name: "Trapping Rain Water",
        link: "https://leetcode.com/problems/trapping-rain-water/description/",
        difficulty: "Hard",
        topics: ["Array", "Two Pointers", "Dynamic Programming"]
    },
    {
        name: "Maximum Subarray",
        link: "https://leetcode.com/problems/maximum-subarray/description/",
        difficulty: "Easy",
        topics: ["Array", "Dynamic Programming"]
    },
    {
        name: "Jump Game II",
        link: "https://leetcode.com/problems/jump-game-ii/description/",
        difficulty: "Medium",
        topics: ["Greedy", "Dynamic Programming"]
    },
    {
        name: "Median of Two Sorted Arrays",
        link: "https://leetcode.com/problems/median-of-two-sorted-arrays/description/",
        difficulty: "Hard",
        topics: ["Array", "Binary Search"]
    },
    {
        name: "Course Schedule",
        link: "https://leetcode.com/problems/course-schedule/description/",
        difficulty: "Medium",
        topics: ["Graph", "Topological Sort"]
    },
    {
        name: "Kth Largest Element in an Array",
        link: "https://leetcode.com/problems/kth-largest-element-in-an-array/description/",
        difficulty: "Medium",
        topics: ["Array", "Sorting", "Heap"]
    }
];

function updateBubble() {
    const bubbleLink = document.querySelector('.bubble-link');
    const bubbleName = bubbleLink.querySelector('.name');
    const bubbleDifficulty = bubbleLink.querySelector('.difficulty');

    bubbleLink.classList.remove('fade-in');
    bubbleLink.classList.add('fade-out');

    const randomProblem = problems[Math.floor(Math.random() * problems.length)];
    topic_container = randomProblem.topics;

    setTimeout(() => {
        
        bubbleLink.href = randomProblem.link;
        bubbleName.textContent = randomProblem.name;
        bubbleDifficulty.textContent = randomProblem.difficulty;

        bubbleDifficulty.classList.remove('easy', 'medium', 'hard');
        const difficultyClass = randomProblem.difficulty.toLowerCase();
        bubbleDifficulty.classList.add(difficultyClass);

        bubbleLink.classList.remove('fade-out');
        bubbleLink.classList.add('fade-in');

        
        
    }, 300);

    refreshTopics();
}

function refreshTopics(){
    const tagContainer = document.querySelector('.tag-container');

    const existingShowTags = tagContainer.querySelector('.show-tags');
    if (existingShowTags) {
        return;
    }
    
    const children = tagContainer.children;
    Array.from(children).forEach(child => {
        child.classList.remove('fade-in');
        child.classList.add('fade-out');
    });

    setTimeout(function() {
        tagContainer.innerHTML = '';

        const showTagsElement = document.createElement('p');
        showTagsElement.classList.add('show-tags');
        showTagsElement.innerText = "Show Topics";
        showTagsElement.classList.add('fade-in');
        tagContainer.appendChild(showTagsElement);
        

        const blurElement = document.createElement('div');
        blurElement.classList.add('blur-background');
        tagContainer.appendChild(blurElement);

        document.querySelector('.show-tags').addEventListener('click', function() {
            const topics = topic_container;
            displayTopics(topics);
        });

    }, 300)
}

{/* <p class="show-tags">Show Topics</p>
<div class="blur-background"> </div> */}

document.querySelector('.x').addEventListener('click', updateBubble);
document.querySelector('.tick').addEventListener('click', updateBubble);