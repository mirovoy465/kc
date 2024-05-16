# Мы в Karpov.Courses заводим Text-to-Speech модель для клонирования голоса: хотим добавить боту на основе ChatGPT озвучку голосом Толи. 
# Этот бот уже активно используется как помощник в Симулятор SQL. 
# Для настройки моделей используются конфиги (конфигурационный файл, config) большого уровня вложенности, 
# параметры из которых периодически требуется устанавливать в качестве переменных окружения.
# Коллеги попросили написать утилиту для парсинга конфигов в переменные окружения и обратно. 
# Конфиги хранятся в формате YAML (Yet Another Markup Language).
# Напишите две функции
# yaml_to_env — функция принимает на вход текст конфига и возвращает текст с переменными окружения.
# env_to_yaml — функция принимает на вход текст с переменными окружения и возвращает текст с конфигом иерархической структуры.

import yaml

def yaml_to_env(config_file: str) -> str:
    """
    Convert YAML configuration from a file to environment variable format.

    Args:
        config_file (str): Path to the YAML configuration file.

    Returns:
        str: Environment variable format string.
    """
    yaml_dict = yaml.load(config_file, Loader=yaml.FullLoader)

    def _t(yaml_dict: dict, parent_str: str = ''):
        result = []
        for key, value in yaml_dict.items():
            if isinstance(value, dict):
                result.extend(_t(value, f'{parent_str}{key}.'))
            else:
                result.append(f'{parent_str}{key}={value}\n')
        return result

    result = ''.join(_t(yaml_dict))
    return result

def env_to_yaml(env_str: str) -> str:
    """
    Convert environment variable format string to YAML format.

    Args:
        env_str (str): Environment variable format string.

    Returns:
        str: YAML format string.
    """
    def _convert_value(value: str) -> any:
        if value.lower() == 'true':
            return True
        elif value.lower() == 'false':
            return False
        try:
            if '.' in value:
                return float(value)
            else:
                return int(value)
        except ValueError:
            return value

    result_dict = {}
    for line in env_str.split('\n'):
        if line == '':
            continue
        key, value = line.split('=', 1)
        keys = key.split('.')
        current_dict = result_dict
        for k in keys[:-1]:
            current_dict = current_dict.setdefault(k, {})
        current_dict[keys[-1]] = _convert_value(value)
    result = yaml.dump(result_dict, default_style='', default_flow_style=False)
    return result


with open('./yaml_config/config.yml') as f:
    yaml_str = f.read()
with open('./yaml_config/config.txt','w') as f:
    f.write(yaml_to_env(yaml_str))

with open('./yaml_config/config.txt') as f:
    env_str = f.read()
with open('./yaml_config/config_env.yml','w') as f:
    f.write(env_to_yaml(env_str))


