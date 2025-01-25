document.querySelector('.show-tags').addEventListener('click', function() {
    const tagContainer = document.querySelector('.tag-container');

    const button = document.querySelector('.show-tags');
    const blur = document.querySelector('.blur-background');
    button.classList.add('fade-out');
    blur.classList.add('fade-out');

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

    }, 700);

    
});

document.querySelector('.x').addEventListener('click', function() {
    console.log('Skip clicked');
});

document.querySelector('.tick').addEventListener('click', function() {
    console.log('Done clicked');
});