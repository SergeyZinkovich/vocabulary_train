import base_engine


class Engine:
    base = []
    them = 0
    word = 0
    lesson_type = 0

    @staticmethod
    def get_themes():
        return base_engine.get_themes()

    @staticmethod
    def start_lesson(them1, les_type):
        Engine.base = base_engine.get_base(them1 if them1 != -1 else None)
        Engine.lesson_type = les_type
        if les_type == 1:
            Engine.base = [[i[1], i[0]] for i in Engine.base]
        Engine.them = them1
        Engine.word = 0

    @staticmethod
    def get_word():
        return Engine.base[Engine.word]

    @staticmethod
    def pass_word(passed):
        Engine.word += 1

    @staticmethod
    def has_next_word():
        return Engine.word < len(Engine.base)
