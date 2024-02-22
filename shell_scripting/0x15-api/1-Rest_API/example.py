import requests

url = "https://opentdb.com/api.php?amount=1&category=18"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    question = data["results"][0]["question"]
    correct_answer = data["results"][0]["correct_answer"]
    incorrect_answers = data["results"][0]["incorrect_answers"]

    print(f"Question: {question}")
    print(f"Correct Answer: {correct_answer}")
    print(f"Incorrect Answers: {', '.join(incorrect_answers)}")
else:
    print("Error fetching question:", response.status_code)
