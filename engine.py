import base_engine


class engine:
    base = base_engine.get_base()
    them = 0
    word = 0
    lesson_type = 0

    @staticmethod
    def get_themes():
        return engine.base.keys()

    @staticmethod
    def start_lesson(them1, les_type):
        engine.lesson_type = les_type
        engine.them = them1
        engine.word = 0

    @staticmethod
    def get_word():
        return engine.base[enumerate(engine.base.keys())][engine.word]
