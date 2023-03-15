"""Markdown, класс редактора"""

class Markdown:

    def __init__(self):
        self.text = ""

    def plain(self, stri: str):
        self.text += stri + "\n"

    def bold(self, stri: str):
        self.text += f"**{stri}**\n"

    def italic(self, stri: str):
        self.text += f"*{stri}*\n"

    def inline_code(self, stri: str):
        self.text += f"`{stri}`\n"

    def link(self, stri: str, url: str):
        self.text += f"[{stri}]({url})+\n"

    def header(self, stri: str, lev: int):
        if lev > 6 or lev < 1:
            print("Пропуск - уровень должен быть не менее 1 и не более 6")
        else:
            self.text += f"{'#' * lev} {stri}\n"

    def unordered_list(self, items: list):
        for item in items:
            self.text += f"* {item}\n"

    def ordered_list(self, items: list):
        for i, item in enumerate(items):
            self.text += f"{i + 1}. {item}\n"

    def new_line(self):
        self.text += "\n"

    def save(self, filename: str):
        with open(filename, "w", encoding="utf-8") as file:
            file.write(self.text)

    def get_string(self, label: str):
        while True:
            input_str = input(f"{label}:\n> ")
            if input_str:
                return input_str
            print("Строка не может быть пустой")

    def get_int(self, label: str):
        while True:
            try:
                return int(input(f"{label}:\n> "))
            except ValueError:
                print("Не является целым числом")

    def get_list(self, label: str):
        print(label+"\n")
        length = self.get_int("Кол-во колонок")
        return [self.get_string(f"Колонка номер {i + 1}:") for i in range(length)]

    def help(self):
        print("""
        ##################################
        
        Доступные команды:
        
        plain - Простой текст
        blod - Полужирный
        italic - Курсив
        code - Код
        link - Ссылка
        header - Заголовок
        unordered - Неупорядоченый список
        ordered - Упорядоченый список
        new-line - Новая линия в студию!
        
        !help - Вывзвать помощь
        !done - Сохоанить файл
        !result - Просмотреть результат
        !exit - Закрыть
        
        ##################################\n
        """)

        pass

    def get_res_text(self):
        print(self.text)

    def start(self):
        while True:
            comm = self.get_string("Ожидается команда")
            match (comm):
                case "plain":
                    self.plain(self.get_string("Текст"))
                case "bold":
                    self.bold(self.get_string("Текст"))
                case "italic":
                    self.italic(self.get_string("Текст"))
                case "code":
                    self.inline_code(self.get_string("Текст"))
                case "link":
                    self.link(self.get_string("Текст"), self.get_string("Адресс"))
                case "header":
                    self.header(self.get_string("Текст"), self.get_int("Размер"))
                case "unordered":
                    self.unordered_list(self.get_list("Список"))
                case "ordered":
                    self.ordered_list(self.get_list("Список"))
                case "new-line":
                    self.new_line()
                    print("Новая линия добавлена")
                case "!help":
                    self.help()
                case "!done":
                    self.save(self.get_string("Имя файла"))
                case "!result":
                    self.get_res_text()
                case "!exit":
                    break
                case _:
                    print("Неизвестная команда")

        pass
