def generate_excuse(scenario, urgency):
    excuses = {
        "work": {
            "low": "I had a minor internet issue this morning.",
            "medium": "There was a power cut in my area.",
            "high": "I had to rush for a family emergency."
        },
        "school": {
            "low": "I couldn’t access the portal.",
            "medium": "I had a fever this morning.",
            "high": "My cousin had a sudden emergency and I had to help."
        },
        "social": {
            "low": "I was tied up with housework.",
            "medium": "I had an unexpected visitor.",
            "high": "Something urgent came up and I couldn’t leave home."
        }
    }
    return excuses.get(scenario, {}).get(urgency, "Sorry, no excuse available.")
