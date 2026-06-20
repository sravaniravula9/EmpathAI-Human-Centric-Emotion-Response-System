def generate_response(emotion):
    responses = {
        "Happy": "Great! Keep smiling 😊",
        "Sad": "Don't worry. Everything will be alright ❤️",
        "Angry": "Take a deep breath and stay calm 😌",
        "Neutral": "Have a wonderful day 🙂",
        "Camera Not Found": "Camera is not available."
    }

    return responses.get(emotion, "Stay positive!")