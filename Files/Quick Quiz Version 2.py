
import json

with open('QuestionBankv2.json', 'r') as file:
    content = file.read()

data_import = json.loads(content)

print(data_import)

user_score = 0
for question in data_import:
    print(question['question_text'])
    for index, item in enumerate(question['answer_choices']):
        print(f'{index+1}. {item.title()}')
    user_choice = int(input("Please select the correct answer: "))
    question['user_answer'] = user_choice

    if question['user_answer'] == question['correct_answer']:
        user_score = user_score + 1
        print('Correct answer!')
    else:
        print('Wrong answer!')

print('Score Summary')
print('-------------')

print(len(data_import))

for index, item in enumerate(data_import):
    message = f"Question {index+1} - Your answer: {item['user_answer']} Correct answer: {item['correct_answer']}"
    print(message)

print(f'{user_score} / {len(data_import)}')

