document.querySelector('.show-tags').addEventListener('click', function() {
    const tagContainer = document.querySelector('.tag-container');

    const button = document.querySelector('.show-tags');
    const blur = document.querySelector('.blur-background');
    button.classList.add('fade-out');
    blur.classList.add('fade-out');

    const container = document.querySelector('.container');

    const topics = ["Topic 1", "Topic 2", "Topic 3", "Topic 4"];

    setTimeout(function() {
        tagContainer.innerHTML = '';

        topics.forEach(function(topic, index) {
            const topicElement = document.createElement('a');
            topicElement.classList.add('topic');
            topicElement.textContent = topic;
            tagContainer.appendChild(topicElement);

            setTimeout(function() {
                topicElement.classList.add('fade-in');
            }, 200 * index);
        });

        // const hideTags = document.createElement('p');
        // hideTags.classList.add('hide-topics');
        // topicElement.textContent = "Hide Topics";
        // tagContainer.appendChild();

    }, 700);

    
});

const problems = [
    {
        name: "Two Sum",
        link: "https://leetcode.com/problems/two-sum/description/",
        difficulty: "Easy"
    },
    {
        name: "Add Two Numbers",
        link: "https://leetcode.com/problems/add-two-numbers/description/",
        difficulty: "Medium"
    },
    {
        name: "Longest Substring Without Repeating Characters",
        link: "https://leetcode.com/problems/longest-substring-without-repeating-characters/description/",
        difficulty: "Hard"
    },
    {
        name: "Valid Parentheses",
        link: "https://leetcode.com/problems/valid-parentheses/description/",
        difficulty: "Medium"
    }
];


function updateBubble() {
    const bubbleLink = document.querySelector('.bubble-link');
    const bubbleName = bubbleLink.querySelector('.name');
    const bubbleDifficulty = bubbleLink.querySelector('.difficulty');

    bubbleLink.classList.remove('fade-in');
    bubbleLink.classList.add('fade-out');

    setTimeout(() => {
        const randomProblem = problems[Math.floor(Math.random() * problems.length)];

        bubbleLink.href = randomProblem.link;
        bubbleName.textContent = randomProblem.name;
        bubbleDifficulty.textContent = randomProblem.difficulty;

        bubbleDifficulty.classList.remove('easy', 'medium', 'hard');
        const difficultyClass = randomProblem.difficulty.toLowerCase();
        bubbleDifficulty.classList.add(difficultyClass);

        bubbleLink.classList.remove('fade-out');
        bubbleLink.classList.add('fade-in');
    }, 300);
}

document.querySelector('.x').addEventListener('click', updateBubble);
document.querySelector('.tick').addEventListener('click', updateBubble);