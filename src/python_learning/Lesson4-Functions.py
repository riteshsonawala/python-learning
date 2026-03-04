def add(a: int, b: int) -> int:
    return a + b


def subtract(a: int, b: int) -> int:
    return a - b

def max_num(list_of_numbers: list) -> int:
    return max(list_of_numbers)

def min_num(list_of_numbers: list) -> int:
    return min(list_of_numbers)

def greet(name: str, language: str = "English") -> str:
    if language == "English":
        return f"Hello {name}, I am {language} speaking!"
    if language == "French":
        return f"Bonjour {name}, je parle {language} !"
    if language == "Spanish":
        return f"Hola {name}, soy {language}!"
    if language == "German":
        return f"Hallo {name}, ich spreche {language}!"
    if language == "Italian":
        return f"Ciao {name}, sono {language}!"
    if language == "Hindi":
        return f"Namaste {name}, I am {language} speaking!"
    if language == "Japanese":
        return f"こんにちは {name}, 私は{language}で話しています！"
    if language == "Korean":
        return f"안녕하세요 {name}, 저는 {language}로 말합니다!"
    return "I dont speak that language, but Hello there!"


if __name__ == "__main__":
    result = add(5, 3)
    print(f"5 + 3 = {result}")
    result = subtract(5, 3)
    print(f"5 - 3 = {result}")
    result = max_num([1, 2, 3, 4, 5])
    print(f"Max of [1, 2, 3, 4, 5] = {result}")
    result = min_num([1, 2, 3, 4, 5])
    print(f"Min of [1, 2, 3, 4, 5] = {result}")
    result = greet("Ritesh")
    print(f"Greeting in English: {result}")
    result = greet("Ritesh", "French")
    print(f"Greeting in French: {result}")

