from contextlib import contextmanager
import os

@contextmanager
def safe_write(filename):
    # Сохраняем исходное содержимое файла, если он существует
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            original = f.read()
    except FileNotFoundError:
        original = None

    file = None
    try:
        file = open(filename, 'w', encoding='utf-8')
        yield file
    except Exception as e:
        # Закрываем файл, если он открыт
        if file and not file.closed:
            file.close()

        # Восстанавливаем исходное состояние
        if original is not None:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(original)
        else:
            # Если файла не было, удаляем созданный пустой файл
            try:
                os.remove(filename)
            except FileNotFoundError:
                pass

        # Выводим сообщение об исключении
        print(f"Во время записи в файл было возбуждено исключение {type(e).__name__}")
    else:
        # Если исключений не было — просто закрываем файл
        if file and not file.closed:
            file.close()


with safe_write('under_tale.txt') as file:
    file.write('Тень от руин нависает над вами, наполняя вас решительностью\n')
    
with safe_write('under_tale.txt') as file:
    print('Под весёлый шорох листвы вы наполняетесь решительностью', file=file, flush=True)
    raise ValueError

with open('under_tale.txt', encoding='utf-8') as file:
    print(file.read())