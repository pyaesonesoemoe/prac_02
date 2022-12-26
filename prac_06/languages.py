from prac_06.programming_language import ProgrammingLanguage

def main():
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
    print(python)
    print(ruby)
    print(visual_basic)

    languages=[python, ruby, visual_basic]
    print("The dynamically typed languages are:")
    ProgrammingLanguage.is_dynamic(python)
    ProgrammingLanguage.is_dynamic(ruby)
    ProgrammingLanguage.is_dynamic(visual_basic)

main()


