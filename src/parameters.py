FIELDS_ALIAS = {
    'наименование': ['наименование', 'услуги'],
    'ставка': ['ставка'],
    'вход': ['вход']
}

FIELDS_ALIAS_REVERSED = {}
for name1C, key_words_list in FIELDS_ALIAS.items():
    for key_word in key_words_list:
        FIELDS_ALIAS_REVERSED[key_word.lower()] = name1C

SERVICES1C = [
    "Фрахт",
    "Транспортно-Экспедиторское обслуживание",
    "Организация ЖД перевозки",
    "Организация автовывоза"
]

_SERVICES_KEYWORDS = {
    "Фрахт": ['фрахт', 'организация морской перевозки'],
    "Транспортно-Экспедиторское обслуживание": ['транспортно-экспедиторское обслуживание', 'экспедирование',
                                                'вознаграждение'],
    "Организация ЖД перевозки": ['организация жд перевозки', "ржд"],
    "Организация автовывоза": ['организация автовывоза', 'автовывоз', 'организация автоперевозки', 'автоперевозка',
                               "организация автомобильной перевозки"]
}

SERVICES_KEYWORDS = {}
for name1C, key_words_list in _SERVICES_KEYWORDS.items():
    for key_word in key_words_list:
        SERVICES_KEYWORDS[key_word.lower()] = name1C
