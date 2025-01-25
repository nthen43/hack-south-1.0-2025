from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_problem', methods=['GET'])
def get_problem():
    problems = [
        {"name": "Two Sum", "link": "https://leetcode.com/problems/two-sum/description/", "difficulty": "Easy"},
        {"name": "Add Two Numbers", "link": "https://leetcode.com/problems/add-two-numbers/description/", "difficulty": "Medium"},
        {"name": "Longest Substring Without Repeating Characters", "link": "https://leetcode.com/problems/longest-substring-without-repeating-characters/description/", "difficulty": "Hard"},
        {"name": "Valid Parentheses", "link": "https://leetcode.com/problems/valid-parentheses/description/", "difficulty": "Medium"}
    ]
    
    # Randomly select a problem
    selected_problem = random.choice(problems)
    
    return jsonify(selected_problem)

if __name__ == '__main__':
    app.run(debug=True)
    
