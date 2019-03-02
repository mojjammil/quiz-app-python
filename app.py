from Questions import Question

question_prompts = [
    "What color is sky?\n(a) Green\n(b) Yellow\n(c) Blue\n\n",
    "What is Python?\n(a) Flower\n(b) Programming language\n(c) Planet\n\n",
    "What is Android?\n(a) Food\n(b) Drinks\n(c) Operating system\n\n"
]

questions = [
    Question(question_prompts[0], "c"),
    Question(question_prompts[1], "b"),
    Question(question_prompts[2], "c")
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) +" correct!")

run_test(questions)
