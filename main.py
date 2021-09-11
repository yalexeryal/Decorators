from datetime import datetime
import os


def logger_creation(file_logger):
    counter = 0

    def logger(old_func):
        def new_func(*args, **kwargs):
            nonlocal counter
            counter += 1
            result = old_func(*args, **kwargs)
            date_function = datetime.today().strftime("%d.%m.%Y %H:%M:%S")
            if os.path.exists(file_logger):
                file_opening_attribute = 'a'
            else:
                file_opening_attribute = 'w'
            with open(file_logger, file_opening_attribute) as file:
                file.write(
                    f'{counter}; {date_function}; {old_func.__name__}; {args, kwargs}; {result} \n'
                )
            return result

        return new_func

    file_loggers = f'{os.path.dirname(__file__)}\\{file_logger}'
    print(file_loggers)

    return logger


filename = 'logs.txt'


@logger_creation(filename)
def hash_generator(filename):
    file = open(str(filename))
    for line in file.readline():
        yield hash(line)
    file.close()


if __name__ == '__main__':
    hash_generator(filename)
