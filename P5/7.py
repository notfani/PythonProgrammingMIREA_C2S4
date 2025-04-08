import re


def parse_data_string(input_str):
    # Регулярное выражение для извлечения секций
    section_pattern = r"<sect>(.*?)</sect>;"

    # Регулярное выражение для извлечения массива данных
    array_pattern = r"array\((.*?)\)"

    # Регулярное выражение для извлечения целевого имени
    target_pattern = r"q\((.*?)\)"

    # Регулярное выражение для извлечения имен внутри массива
    name_pattern = r"@'([^']*)'"

    # Найти все секции
    sections = re.findall(section_pattern, input_str, re.DOTALL)

    result = []

    for section in sections:
        # Извлечь массив данных
        array_match = re.search(array_pattern, section)
        if array_match:
            array_content = array_match.group(1)
            # Извлечь имена внутри массива
            names = re.findall(name_pattern, array_content)

        # Извлечь целевое имя
        target_match = re.search(target_pattern, section)
        if target_match:
            target_name = target_match.group(1)

        # Добавить пару (целевое_имя, список_данных) в результат
        result.append((target_name, names))

    return result


# Пример использования
input_str_1 = "||<sect> data array( @'cebi_815'; @'geso'; @'usla_563' ) to q(dite_207);</sect>;<sect> data array( @'zaatus_229' ; @'ave'; @'enre' )to q(raat); </sect>;||"
input_str_2 = "||<sect> data array( @'ated'; @'enso_554' ; @'edes_177') to q(lazaer);</sect>; <sect> data array( @'rela_539'; @'raradi' ; @'maques_294') to q(rive); </sect>; <sect> data array( @'vege_713' ;@'dier_208' ; @'eraxela' ) to q(erqu_432); </sect>; ||"

print(parse_data_string(input_str_1))
print(parse_data_string(input_str_2))