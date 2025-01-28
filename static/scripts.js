
//Takes in array of topics
//["Array", "Hashing"];
//if empty will show no tags found
function displayTopics(topics) {
    const tagContainer = document.querySelector('.tag-container');
    const button = document.querySelector('.show-tags');
    const blur = document.querySelector('.blur-background');

    button.classList.remove('fade-in');
    button.classList.add('fade-out');
    blur.classList.add('fade-out');

    setTimeout(function() {
        tagContainer.innerHTML = '';

        if(topics.length === 0){
            const topicElement = document.createElement('a');
            topicElement.classList.add('topic');
            topicElement.textContent = "No Topics Found";
            tagContainer.appendChild(topicElement);
            topicElement.classList.add('fade-in');
        }

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

const errorProblem =     
[{
    name: "Error Finding Problem",
    link: "#",
    difficulty: "Error",
    topics: []
}
];
let topic_container = [];
let problem_container = [];

async function updateBubble() {
    const bubbleLink = document.querySelector('.bubble-link');
    const bubbleName = bubbleLink.querySelector('.name');
    const bubbleDifficulty = bubbleLink.querySelector('.difficulty');

    bubbleLink.classList.remove('fade-in');
    bubbleLink.classList.add('fade-out');

    // Timeout function to reject after a specified time
    function timeout(ms) {
        return new Promise((_, reject) => setTimeout(() => reject('Timeout'), ms));
    }

    // Modify getRandomProblem to wait for a response or timeout
    async function fetchRandomProblemWithTimeout() {
        const timeoutDuration = 5000; // Set timeout duration (e.g., 5000 ms = 5 seconds)

        try {
            const problemPromise = getRandomProblem();  // API call
            const problems = await Promise.race([problemPromise, timeout(timeoutDuration)]);  // Wait for either the response or timeout
            return problems;
        } catch (error) {
            console.error('Error or Timeout:', error);
            return []; // Return empty array in case of error or timeout
        }
    }

    // Fetch the random problem or handle timeout
    const problems = await fetchRandomProblemWithTimeout();

    let randomProblem = errorProblem[0]; // Default to error problem if no valid data
    if (problems.length > 0) {
        console.log('Fetched random problem(s):', problems);
        problem_container = problems;  // Assign problems
        randomProblem = problem_container[Math.floor(Math.random() * problem_container.length)];  // Randomly pick a problem
    } else {
        console.log('Failed to fetch random problem.');
    }

    topic_container = randomProblem.topics;  // Assign topics from the selected problem

    // Updates the main bubble
    setTimeout(() => {
        bubbleLink.href = randomProblem.link;
        bubbleName.textContent = randomProblem.name;
        bubbleDifficulty.textContent = randomProblem.difficulty;

        bubbleDifficulty.classList.remove('easy', 'medium', 'hard', 'error');
        const difficultyClass = randomProblem.difficulty.toLowerCase();
        bubbleDifficulty.classList.add(difficultyClass);

        bubbleLink.classList.remove('fade-out');
        bubbleLink.classList.add('fade-in');
    }, 300);

    // Updates the topic list to match that from the bubble
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

function getRandomProblem() {
    return new Promise((resolve, reject) => {
        fetch('/random-problem')
            .then(response => {
                if (!response.ok) {
                    throw new Error('Failed to fetch random problem');
                }
                return response.json();
            })
            .then(data => {
                resolve(data);
            })
            .catch(error => {
                console.error('Error fetching random problem:', error);
                resolve([]);
            });
    });
}

document.querySelector('.show-tags').addEventListener('click', function() {
    const topics = topic_container;
    displayTopics(topics);
});

document.querySelector('.x').addEventListener('click', updateBubble);
document.querySelector('.tick').addEventListener('click', updateBubble);

document.addEventListener('DOMContentLoaded', function() {
    const bubbleElement = document.querySelector('.bubble');
    bubbleElement.classList.remove('pulse-opacity');
    updateBubble();
});