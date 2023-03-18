"""Markdown, класс редактора"""

class Markdown:

    def __init__(self):
        self.text = ""

    """Описание
        
        Добавляет строчку текста
        
        Параметры:
        stri (str): Строка для добавления

        Ничего не возвращает
       """
    def plain(self, stri: str):
        self.text += stri + "\n"

    """Описание
            
            Добавляет строчку жирного текста
        
        Параметры:
        stri (str): Строка для добавления

        Ничего не возвращает
       """
    def bold(self, stri: str):
        self.text += f"**{stri}**\n"

    """Описание
        
        Добавляет строчку курсива
        
        Параметры:
        stri (str): Строка для добавления

        Ничего не возвращает
       """
    def italic(self, stri: str):
        self.text += f"*{stri}*\n"

    """Описание
    
        Добавляет строчку кода

        Параметры:
        stri (str): Строка для добавления

        Ничего не возвращает
       """
    def inline_code(self, stri: str):
        self.text += f"`{stri}`\n"

    """Описание
    
        Добавляет ссылку (Как строку)

        Параметры:
        stri (str): Строка для добавления
        url (str): Адресс, на который ссылается ссылка
        
        Ничего не возвращает
       """
    def link(self, stri: str, url: str):
        self.text += f"[{stri}]({url})+\n"

    """Описание
        
        Добавляет *Заголовок* заданного размера, допускается от 1 до 6.
        
        Параметры:
        stri (str): Строка для добавления
        lev (str): Уровень. Чем больше тем больше размер, от 1 до 6

        Ничего не возвращает
       """
    def header(self, stri: str, lev: int):
        if lev > 6 or lev < 1:
            print("Пропуск - уровень должен быть не менее 1 и не более 6")
        else:
            self.text += f"{'#' * lev} {stri}\n"

    """Описание
    
        Добавляет НЕПРОНУМЕРОВАНЫЕ строки, форматированые под список

        Параметры:
        items (list): Лист СТРОК для добавления

        Ничего не возвращает
       """
    def unordered_list(self, items: list):
        for item in items:
            self.text += f"* {item}\n"

    """Описание

        Добавляет ПРОНУМЕРОВАНЫЕ строки, форматированые под список

        Параметры:
        items (list): Лист СТРОК для добавления

        Ничего не возвращает
       """
    def ordered_list(self, items: list):
        for i, item in enumerate(items):
            self.text += f"{i + 1}. {item}\n"

    """Описание
    
        Добавляет новую пустую строку

        Ничего не требует

        Ничего не возвращает
       """
    def new_line(self):
        self.text += "\n"

    """Описание
    
        Сохраняет наработанный буфер в файл

        Параметры:
        filename (str): Имя файла, в который сохранится буфе

        Ничего не возвращает
       """
    def save(self, filename: str):
        with open(filename, "w", encoding="utf-8") as file:
            file.write(self.text)

    """Описание
    
        Получает от пользователя строку

        Параметры:
        label (str): Коментарий запроса

        Возвращает:
        str: Строка, полученная с вывода
       """
    def get_string(self, label: str):
        while True:
            input_str = input(f"{label}:\n> ")
            if input_str:
                return input_str
            print("Строка не может быть пустой")

    """Описание
    
        Получает от пользователя целое число

        Параметры:
        label (str): Коментарий запроса

        Возвращает:
        int: Целое число, полученное с вывода
       """
    def get_int(self, label: str):
        while True:
            try:
                return int(input(f"{label}:\n> "))
            except ValueError:
                print("Не является целым числом")

    """Описание
    
        Получает от пользователя список

        Параметры:
        label (str): Коментарий запроса

        Возвращает:
        list: Лист СТРОК, полученных с вывода
       """
    def get_list(self, label: str):
        print(label+"\n")
        length = self.get_int("Кол-во колонок")
        return [self.get_string(f"Колонка номер {i + 1}:") for i in range(length)]

    """Описание
    
        Выдаёт пользователю справку

        Ничего не требует

        Ничего не возвращает
       """
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

    """Описание
    
        Выдает пользователю буффер с набраным текстом

        Ничего не требует

        Ничего не возвращает
       """
    def get_res_text(self):
        print(self.text)

    """Описание
    
        Функция для запуска работы редактора

        Ничего не требует

        Ничего не возвращает
       """

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
