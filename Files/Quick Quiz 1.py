question_bank = [
  ['Question', 'Choices', 'Answer'],
  ['What is the correct species for Dolphin?', ['Mammal','Bird','Amphibian'], 'Mammal'],
  ['What is the capital of USA?', ['New York', 'Washington', 'Tokyo'], 'Washington']
]

answers = []

for item in question_bank[1:]:
    print(item[0])
    for index, answer in enumerate(item[1]):
        print(f'{index+1}. {answer}')
    user_answer = input('Answer: ').strip()
    user_answer = user_answer.title()

    if user_answer == item[2]:
        answers.append(True)
    else:
        answers.append(False)

if all(answers):
    print(f'Scored: {len(answers)} out of {len(answers)}')
else:
    correct_answers = answers.count(True)
    print(f'Scored: {correct_answers} out of {len(answers)}')


