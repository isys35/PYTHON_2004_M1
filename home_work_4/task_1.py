authors = {
    "Якуб Колас": "На росстанях",
    "Янка Брыль": "Жменя сонечных промняў",
    "Васіль Быкаў": "Жураўліны крык",
    "Янка Купала": "Раскіданае гняздо",
    "Уладзімір Караткевіч": "Каласы пад сярпом тваім"
}

correct_answers = 0

for book in authors.values():
    answer_input = input(f"Кто написал '{book}'?")
    if answer_input in authors and authors[answer_input] == book:
        correct_answers += 1

print(f"Количество правильных ответов: {correct_answers}")