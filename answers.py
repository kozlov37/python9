fn=input("Пожалуйста, поздоровайтесь ")
fn2=str(fn).lower()
myanswers = {"привет": "И тебе привет!", "как дела": "Лучше всех", "пока": "Увидимся"}

def get_answer(question,answers):
    return answers.get(question,"Не найдено подходящего варианта ответа")

print(get_answer(fn2, myanswers))
