# two functions

"""
Custom object Card:
    id
    name
    tags
    solved

Need a class that will do three functions, 
1. Insert Card
    Places a Card with a priority value inside of an array

2. Get Card
    Gets the Card with the lowest priority value

3. Update Priority
    Updates the priority value for multiple Cards, based on if the problem was solved or not.
    Sort the Card Array by how completed it is out of every question (calculate percentage completed.

    

"""

import json
import os

class Card:
    def __init__(self, priority, tag):
        # for queue purposes
        self.priority = priority

        #for retrieval purposes
        self.tag = tag
        
        

class RecommendQueue:
    def __init__(self):
        self.array = []
        self.existing_tags = set()  # To track unique tags

    def insert_card(self, card):
        """
        Inserts a card into the array based on its priority.
        Lower priority value means higher importance.
        """
        if card.tag not in self.existing_tags:
            self.array.append(card)
            self.existing_tags.add(card.tag)
            self.array.sort(key=lambda x: x.priority)

    def get_card(self, tag):
        """
        Searches for a card in the array based on the tag.
        Returns the card if found, otherwise returns None.
        """
        for card in self.array:
            if card.tag == tag:
                return card
        return None

    def update_priority(self, file_paths):
        """
        Updates the priority of cards based on the least solved ratio of each tag category.

        Args:
            file_paths (list): List of file paths containing problem data in JSON format.
        """
        # Dictionary to store solved and unsolved counts for each tag
        tag_stats = {}

        # Read data from each file and calculate solved/unsolved ratios
        for file_path in file_paths:
            try:
                with open(file_path, 'r') as file:
                    data = json.load(file)
                    tags = data.get("tags", [])
                    status = data.get("status", False)

                    for tag in tags:
                        if tag not in tag_stats:
                            tag_stats[tag] = {"solved": 0, "unsolved": 0}

                        if status:
                            tag_stats[tag]["solved"] += 1
                        else:
                            tag_stats[tag]["unsolved"] += 1
            except (FileNotFoundError, json.JSONDecodeError) as e:
                print(f"Error processing file {file_path}: {e}")

        # Calculate completion ratios for each tag
        completion_ratios = {
            tag: stats["solved"] / (stats["solved"] + stats["unsolved"])
            for tag, stats in tag_stats.items()
            if (stats["solved"] + stats["unsolved"]) > 0
        }

        # Find the least completed tag
        least_completed_tag = min(completion_ratios, key=completion_ratios.get, default=None)

        if not least_completed_tag:
            print("No valid data to update priorities.")
            return

        # Update the priority of all cards
        for card in self.array:
            if card.tag == least_completed_tag:
                card.priority = 0  # Assign highest priority (lowest number)
            else:
                card.priority += 1  # Increase priority for others

        # Re-sort the array to reflect updated priorities
        self.array.sort(key=lambda x: x.priority)

        print(f"Updated priorities based on tag: {least_completed_tag}")


if __name__ == "__main__":
    class Card:
        def __init__(self, priority, tag):
            self.priority = priority
            self.tag = tag

        def __repr__(self):
            return f"Card(priority={self.priority}, tag='{self.tag}')"

    # Initialize the queue
    queue = RecommendQueue()

    # Define the folder containing the text files
    folder_path = "output_problems"  # Replace with the path to your folder
    file_paths = []

    # Loop through all .txt files in the folder
    for file_name in os.listdir(folder_path):
        if file_name.endswith(".txt"):
            file_paths.append(os.path.join(folder_path, file_name))

    # Populate cards array
    for file_path in file_paths:
        try:
            with open(file_path, 'r') as file:
                data = json.load(file)
                tags = data.get("tags", [])
                for tag in tags:
                    # Insert a card for each tag with a default priority (e.g., 10)
                    queue.insert_card(Card(priority=10, tag=tag))
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Error processing file {file_path}: {e}")

    # Run update_priority function
    queue.update_priority(file_paths)

    # Print the updated cards array
    print("Updated Queue:")
    for card in queue.array:
        print(card)