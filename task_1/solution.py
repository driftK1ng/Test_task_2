import inspect

def before_func(values: dict, input_types: dict):
    """Проверяет, соответстуют ли типы параметров функции, типам в аннотации функции

    Args:
        values (dict): Параметры проверяемой функции
        input_types (dict): Типы данных в аннотации
    """
    for key in values.keys():
        if not isinstance(values[key], input_types[key]):
            raise TypeError(f"Parameter ( {key} ) " 
                            f"must be {input_types[key]} not {type(values[key])}")

def after_func(expected_type, result, func_name):
    """Проверяет возвращаемое значение функции на соответствие, аннотации
    
    Args:
        expected_type (type): Ожидаемый тип данных
        result (Any): Возвращаемое значение функции
        func_name (str): Имя функции
    """
    if not isinstance(result, expected_type):
        raise TypeError(f"Result of function ( {func_name} ) "
                        f"must be {expected_type} not {type(result)}")


def strict(func):
    """Проверяет, входные и выходные данные на соответствие аннотации

    Args:
        func (function): Рассматриваемая функция

    Returns:
        Any: Выходное значение функции
    """
    sign = inspect.signature(func)
    input_types = func.__annotations__
    def wrapper(*args, **kwargs):
        values = sign.bind(*args, **kwargs).arguments
        before_func(values, input_types)
        result = func(*args, **kwargs)
        after_func(input_types['return'], result, func.__name__)
        return result
    return wrapper
