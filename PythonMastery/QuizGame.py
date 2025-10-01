# Quiz Game (random Q&A + scoring).
import random
import json

FILENAME = "quizes.json"
result_file = "quiz_result.txt"

def load_questions():
    try:
        with open(FILENAME, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"File '{FILENAME}' not found!")
        return {}
    except json.JSONDecodeError:
        print(f"Error decoding JSON from '{FILENAME}'")
        return {}    

def quiz_games(questions):
    # load quiz_result
    name = input("Enter your name: ")

    if not questions:
        print("No questions available to play!")
        return
    score = 0
    # shuffle questions
    questions = random.sample(questions, len(questions))

    for q in questions:
        print("\n" + q["question"])
        for option in q["options"]:
            print(option)

        answer = input("Your answer (A/B/C/D: )".strip().upper())

        if(answer == q["answer"]):
            print("Correct")
            score += 1
        else:
            print(f"Wrong! The correct answwer is {q['answer']}.")

    final_score = score/len(questions)
    print(f"\n Quiz finished! Your score: {score}/{len(questions)}")

    # write to quiz_result.txt
    with open(result_file, "a") as f:
        f.write(f"Score of {name}: {score}/{len(questions)}\n")

def main():
    questions = load_questions()
    quiz_games(questions)

if __name__ == "__main__":
    main()
