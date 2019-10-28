import vkapi
import dataBase

product_id = {
    'Помидоры': 1,
    'Сметана': 2,
    'Огурцы': 3,
    'Хлеб': 4,
    'Соус Переменка': 5,
    'Рис отвар.': 6,
    'Рассольник': 7,
    'Картофель запеч.': 8,
    'Пельмени': 9,
    'Грудка куриная по-французски': 10,
    'Жаркое с говядиной': 11,
    'Салат из свеклы, яблок, кукурузы': 12,
    'Тефтели мясные в томат соусе': 13,
    'Филе горубуши с молоч соусом': 14,
    'Салат Витаминка': 15,
    'Био Баланс 0.33л': 16,
    'Активия 0.29л': 17,
    'Bio-Max 0.27л': 18,
    'Десерт Чудо 0.1л': 19,
    'Йог Данон 0.11л': 20,
    'Йог Растишка 0.09л': 21,
    'Йог Растишка 0.2л': 22,
    'Йогурт Чудо 0.1л': 23,
    'Йогуртер Чудо 0.1л': 24,
    'Смешарики 0.2л': 25,
    'Топтыжка 0.2л': 26,
    'Имунеле 0.1л': 27,
    'Чудо 0.2л': 28,
    'Чудо шок 0.2л': 29,
    'Чудо-Детки 0.27л': 30,
    'Мажитель J7 0.27л': 31,
    'Мажитель 0.25л': 32,
    'Актимель 0.1л': 33,
    'Актуаль 0.3л': 34,
    'Злак. батончик Матти': 35,
    'Косичка зефирка': 36,
    'Пирожное Фанни Банни': 37,
    'Чоко пай': 38,
    'Пицца Кальцоне': 39,
    'Пицца с сыром': 40,
    'Слойка фруктовая': 41,
    'Шафран с яблок.': 42,
    'Пышка сдобная': 43,
    'Слойка кукуруз.': 44,
    'Слойка с сыром': 45,
    'Сосиски в тесте': 46,
    'Штрудель вишн.': 47,
    'Штрудель яблоч.': 48,
    'Элеш с куриц.': 49,
    'Эчпочмак говяжий': 50,
    'Расстегай с горбушей и луком': 51,
    'Пицца с колбасой и сыром': 52,
    'Пицца с ветчиной куриной и сыром': 53,
    'Ватрушка Франц.': 54,
    'Губадия с кортом': 55,
    'Пицца Ориг.': 56,
    'Пирожок с вишн.': 57,
    'Ватрушка с сыром': 58,
    'Сдоба с творог.': 59,
    'Пицца с куриц.,сыром': 60,
    'Губадия без яиц': 61,
    'Бэккен с капуст., яйцом': 62,
    'Вакбалиш с мяс.,рис': 63,
    'Пирожки печеные с мяс.,лук': 64,
    'Пирожки печеные с мяс.,рис': 65,
    'Пирожки слоеные с мясом': 66,
    'Пирожки с черн. смородиной': 67,
    'Творожный': 68,
    'Трехслойник': 69,
    'Домашний с маком': 70,
    'Зебра': 71,
    'Лимонный': 72,
    'С малиной': 73,
    'Земелах': 74,
    'Курабье': 75,
    'Мягкое': 76,
    'Сдобное вкусное': 77,
    'Сдобное листики': 78,
    'Сдобное шоколадное': 79,
    'Морковное': 80,
    'Сдобное Американер': 81,
    'Сдобное Американер с кунжутом': 82,
    'Заварное': 83,
    'Медовое': 84,
    'Пампушки': 85,
    'Песочное корзинка': 86,
    'Песочное нарезное': 87,
    'Песочное со сгущенкой': 88,
    'Буше': 89,
    'Кекс': 90,
    'Круассан': 91,
    'Кольцо песоч.': 92,
    'Корж молоч.': 93,
    'Корж яблоч.': 94,
    'Маффин лимон.': 95,
    'Маффин цукат.': 96,
    'Маффин шоколад.': 97,
    'Улитка с творогом': 98,
    'Улитка с орехами': 99,
    'Язык слоеный': 100,
    'Коврижка медов.': 101,
    'Сочень творог.': 102,
    'Чак-чак': 103,
    'Конвертик слоеный': 104,
    'Мешочки с яблоками': 105,
    'Холодный чай 0.5л': 106,
    'Холодный чай 0.3л': 107,
    'Нектары и соки 0.2л': 108,
    'Нектары и соки 0.95л': 109,
    'Пюре груш Агуша 0.09л': 110,
    'Соки фруктовые 0.33л': 111,
    'Напиток цитрус 0.38л': 112,
    'Напиток компотный 0.2л': 113,
    'Рита в Ритме 0.5л': 114,
    'Святая чаша 0.45л': 115,
    'Чистый глоток 0.5л': 116,
    'Вафли': 117,
    'Апельсины': 118,
    'Бананы': 119,
    'Груши': 120,
    'Колбаса полукопченая': 121,
    'Мандарины': 122,
    'Сыр': 123,
    'Яблоки': 124,
    'Компот сухофрукт 0.2л': 125,
    'Компот вишня 0.2л': 126,
    'Компот апельсин 0.2л': 127,
    'Компот смородина 0.2л': 128,
    'Компот изюм,курага 0.2л': 129,
    'Компот изюм,урюк 0.2л': 130,
    'Компот курага 0.2л': 131,
    'Компот груша 0.2л': 132,
    'Компот яблоч 0.2л': 133,
    'Компот урюк 0.2л': 134,
    'Какао с молоком 0.2л': 135,
    'Кофе с молоком 0.2л': 136,
    'Напиток клюква 0.2л': 1137,
    'Напиток шиповник 0.2л': 138,
    'Чай Гринфилд 0.2л': 139
    }

id_product = {
    1: 'Помидоры',
    2: 'Сметана',
    3: 'Огурцы',
    4: 'Хлеб',
    5: 'Соус Переменка',
    6: 'Рис отвар.',
    7: 'Рассольник',
    8: 'Картофель запеч.',
    9: 'Пельмени',
    10: 'Грудка куриная по-французски',
    11: 'Жаркое с говядиной',
    12: 'Салат из свеклы, яблок, кукурузы',
    13: 'Тефтели мясные в томат соусе',
    14: 'Филе горубуши с молоч соусом',
    15: 'Салат Витаминка',
    16: 'Био Баланс 0.33л',
    17: 'Активия 0.29л',
    18: 'Bio-Max 0.27л',
    19: 'Десерт Чудо 0.1л',
    20: 'Йог Данон 0.11л',
    21: 'Йог Растишка 0.09л',
    22: 'Йог Растишка 0.2л',
    23: 'Йогурт Чудо 0.1л',
    24: 'Йогуртер Чудо 0.1л',
    25: 'Смешарики 0.2л',
    26: 'Топтыжка 0.2л',
    27: 'Имунеле 0.1л',
    28: 'Чудо 0.2л',
    29: 'Чудо шок 0.2л',
    30: 'Чудо-Детки 0.27л',
    31: 'Мажитель J7 0.27л',
    32: 'Мажитель 0.25л',
    33: 'Актимель 0.1л',
    34: 'Актуаль 0.3л',
    35: 'Злак. батончик Матти',
    36: 'Косичка зефирка',
    37: 'Пирожное Фанни Банни',
    38: 'Чоко пай',
    39: 'Пицца Кальцоне',
    40: 'Пицца с сыром',
    41: 'Слойка фруктовая',
    42: 'Шафран с яблок.',
    43: 'Пышка сдобная',
    44: 'Слойка кукуруз.',
    45: 'Слойка с сыром',
    46: 'Сосиски в тесте',
    47: 'Штрудель вишн.',
    48: 'Штрудель яблоч.',
    49: 'Элеш с куриц.',
    50: 'Эчпочмак говяжий',
    51: 'Расстегай с горбушей и луком',
    52: 'Пицца с колбасой и сыром',
    53: 'Пицца с ветчиной куриной и сыром',
    54: 'Ватрушка Франц.',
    55: 'Губадия с кортом',
    56: 'Пицца Ориг.',
    57: 'Пирожок с вишн.',
    58: 'Ватрушка с сыром',
    59: 'Сдоба с творог.',
    60: 'Пицца с куриц.,сыром',
    61: 'Губадия без яиц',
    62: 'Бэккен с капуст., яйцом',
    63: 'Вакбалиш с мяс.,рис',
    64: 'Пирожки печеные с мяс.,лук',
    65: 'Пирожки печеные с мяс.,рис',
    66: 'Пирожки слоеные с мясом',
    67: 'Пирожки с черн. смородиной',
    68: 'Творожный',
    69: 'Трехслойник',
    70: 'Домашний с маком',
    71: 'Зебра',
    72: 'Лимонный',
    73: 'С малиной',
    74: 'Земелах',
    75: 'Курабье',
    76: 'Мягкое',
    77: 'Сдобное вкусное',
    78: 'Сдобное листики',
    79: 'Сдобное шоколадное',
    80: 'Морковное',
    81: 'Сдобное Американер',
    82: 'Сдобное Американер с кунжутом',
    83: 'Заварное',
    84: 'Медовое',
    85: 'Пампушки',
    86: 'Песочное корзинка',
    87: 'Песочное нарезное',
    88: 'Песочное со сгущенкой',
    89: 'Буше',
    90: 'Кекс',
    91: 'Круассан',
    92: 'Кольцо песоч.',
    93: 'Корж молоч.',
    94: 'Корж яблоч.',
    95: 'Маффин лимон.',
    96: 'Маффин цукат.',
    97: 'Маффин шоколад.',
    98: 'Улитка с творогом',
    99: 'Улитка с орехами',
    100: 'Язык слоеный',
    101: 'Коврижка медов.',
    102: 'Сочень творог.',
    103: 'Чак-чак',
    104: 'Конвертик слоеный',
    105: 'Мешочки с яблоками',
    106: 'Холодный чай 0.5л',
    107: 'Холодный чай 0.3л',
    108: 'Нектары и соки 0.2л',
    109: 'Нектары и соки 0.95л',
    110: 'Пюре груш Агуша 0.09л',
    111: 'Соки фруктовые 0.33л',
    112: 'Напиток цитрус 0.38л',
    113: 'Напиток компотный 0.2л',
    114: 'Рита в Ритме 0.5л',
    115: 'Святая чаша 0.45л',
    116: 'Чистый глоток 0.5л',
    117: 'Вафли',
    118: 'Апельсины',
    119: 'Бананы',
    120: 'Груши',
    121: 'Колбаса полукопченая',
    122: 'Мандарины',
    123: 'Сыр',
    124: 'Яблоки',
    125: 'Компот сухофрукт 0.2л',
    126: 'Компот вишня 0.2л',
    127: 'Компот апельсин 0.2л',
    128: 'Компот смородина 0.2л',
    129: 'Компот изюм,курага 0.2л',
    130: 'Компот изюм,урюк 0.2л',
    131: 'Компот курага 0.2л',
    132: 'Компот груша 0.2л',
    133: 'Компот яблоч 0.2л',
    134: 'Компот урюк 0.2л',
    135: 'Какао с молоком 0.2л',
    136: 'Кофе с молоком 0.2л',
    137: 'Напиток клюква 0.2л',
    138: 'Напиток шиповник 0.2л',
    139: 'Чай Гринфилд 0.2л'
    }

keyboard_main = {
    'one_time': False,
    'buttons': [
        [{
            'action': {
                'type': 'text',
                'payload': '',
                'label': u'Узнать школьное меню'
            },
            'color': 'positive'
        }],
        [{
            'action': {
                'type': 'text',
                'payload': '',
                'label': u'Составить обед'
            },
            'color': 'positive'
        }],
        [{
            'action': {
                'type': 'text',
                'payload': '',
                'label': u'Калькулятор веса'
            },
            'color': 'positive'
        }]
    ]
}

keyboard_menu = {
    'one_time': False,
    'buttons': [
        [{
            'action': {
                'type': 'text',
                'payload': '',
                'label': u'Свободный выбор'
            },
            'color': 'positive'
        }],
        [{
            'action': {
                'type': 'text',
                'payload': '',
                'label': u'Молочная продукция'
            },
            'color': 'positive'
        }],
        [{
            'action': {
                'type': 'text',
                'payload': '',
                'label': u'Соки'
            },
            'color': 'positive'
        },
            {
                'action': {
                    'type': 'text',
                    'payload': '',
                    'label': u'Вода'
                },
                'color': 'positive'
            }
        ],
        [{
            'action': {
                'type': 'text',
                'payload': '',
                'label': u'Конфеты, шоколад'
            },
            'color': 'positive'
        }],
        [{
            'action': {
                'type': 'text',
                'payload': '',
                'label': u'Мучные изделия'
            },
            'color': 'positive'
        }],
        [{
            'action': {
                'type': 'text',
                'payload': '',
                'label': u'Холодные закуски'
            },
            'color': 'positive'
        }],
        [{
            'action': {
                'type': 'text',
                'payload': '',
                'label': u'Компоты'
            },
            'color': 'positive'
        },
            {
                'action': {
                    'type': 'text',
                    'payload': '',
                    'label': u'Напитки'
                },
                'color': 'positive'
            }],
        [{
            'action': {
                'type': 'text',
                'payload': '',
                'label': u'Конд. изделия'
            },
            'color': 'positive'
        },
            {
                'action': {
                    'type': 'text',
                    'payload': '',
                    'label': u'Вафли'
                },
                'color': 'positive'
            }
        ],
        [{
            'action': {
                'type': 'text',
                'payload': '',
                'label': u'Составить новый обед'
            },
            'color': 'default'
        }],
        [{
            'action': {
                'type': 'text',
                'payload': '',
                'label': u'Подвести итог'
            },
            'color': 'default'
        },
            {
                'action': {
                    'type': 'text',
                    'payload': '',
                    'label': u'В начало'
                },
                'color': 'negative'
            }]
    ]
}

keyboard_freeChoose = {
    'one_time': False,
    'buttons': [
        [{
            'action': {
                'type': 'text',
                'payload': '',
                'label': u'Помидоры'
            },
            'color': 'positive'
        },
            {
                'action': {
                    'type': 'text',
                    'payload': '',
                    'label': u'Сметана'
                },
                'color': 'positive'
            },
            {
                'action': {
                    'type': 'text',
                    'payload': '',
                    'label': u'Огурцы'
                },
                'color': 'positive'
            }
        ],
        [{
            'action': {
                'type': 'text',
                'payload': '',
                'label': u'Хлеб'
            },
            'color': 'positive'
        },
            {
                'action': {
                    'type': 'text',
                    'payload': '',
                    'label': u'Соус Переменка'
                },
                'color': 'positive'
            }
        ],
        [{
            'action': {
                'type': 'text',
                'payload': '',
                'label': u'Рис отвар.'
            },
            'color': 'positive'
        },
            {
                'action': {
                    'type': 'text',
                    'payload': '',
                    'label': u'Рассольник'
                },
                'color': 'positive'
            }
        ],
        [{
            'action': {
                'type': 'text',
                'payload': '',
                'label': u'Картофель запеч.'
            },
            'color': 'positive'
        },
            {
                'action': {
                    'type': 'text',
                    'payload': '',
                    'label': u'Пельмени'
                },
                'color': 'positive'
            }
        ],
        [{
            'action': {
                'type': 'text',
                'payload': '',
                'label': u'Грудка куриная по-французски'
            },
            'color': 'positive'
        }
        ],
        [{
            'action': {
                'type': 'text',
                'payload': '',
                'label': u'Жаркое с говядиной'
            },
            'color': 'positive'
        }
        ],
        [{
            'action': {
                'type': 'text',
                'payload': '',
                'label': u'Салат из свеклы, яблок, кукурузы'
            },
            'color': 'positive'
        }
        ],
        [{
            'action': {
                'type': 'text',
                'payload': '',
                'label': u'Тефтели мясные в томат соусе'
            },
            'color': 'positive'
        }
        ],
        [{
            'action': {
                'type': 'text',
                'payload': '',
                'label': u'Филе горубуши с молоч соусом'
            },
            'color': 'positive'
        }
        ],
        [{
            'action': {
                'type': 'text',
                'payload': '',
                'label': u'Салат Витаминка'
            },
            'color': 'positive'
        },
            {
                'action': {
                    'type': 'text',
                    'payload': '',
                    'label': u'Назад'
                },
                'color': 'negative'
            }
        ]
    ]
}

keyboard_milkFood = {
    'one_time': False,
    'buttons': [
        [{
            'action': {
                'type': 'text',
                'payload': '',
                'label': u'Био Баланс 0.33л'
            },
            'color': 'positive'
        },
            {
                'action': {
                    'type': 'text',
                    'payload': '',
                    'label': u'Активия 0.29л'
                },
                'color': 'positive'
            }],
        [{
            'action': {
                'type': 'text',
                'payload': '',
                'label': u'Bio-Max 0.27л'
            },
            'color': 'positive'
        },
            {
                'action': {
                    'type': 'text',
                    'payload': '',
                    'label': u'Десерт Чудо 0.1л'
                },
                'color': 'positive'
            }],
        [{
            'action': {
                'type': 'text',
                'payload': '',
                'label': u'Йог Данон 0.11л'
            },
            'color': 'positive'
        },
            {
                'action': {
                    'type': 'text',
                    'payload': '',
                    'label': u'Йог Растишка 0.09л'
                },
                'color': 'positive'
            }],
        [{
            'action': {
                'type': 'text',
                'payload': '',
                'label': u'Йог Растишка 0.2л'
            },
            'color': 'positive'
        },
            {
                'action': {
                    'type': 'text',
                    'payload': '',
                    'label': u'Йогурт Чудо 0.1л'
                },
                'color': 'positive'
            }],
        [{
            'action': {
                'type': 'text',
                'payload': '',
                'label': u'Йогуртер Чудо 0.1л'
            },
            'color': 'positive'
        },
            {
                'action': {
                    'type': 'text',
                    'payload': '',
                    'label': u'Смешарики 0.2л'
                },
                'color': 'positive'
            }],
        [{
            'action': {
                'type': 'text',
                'payload': '',
                'label': u'Топтыжка 0.2л'
            },
            'color': 'positive'
        },
            {
                'action': {
                    'type': 'text',
                    'payload': '',
                    'label': u'Имунеле 0.1л'
                },
                'color': 'positive'
            }],
        [{
            'action': {
                'type': 'text',
                'payload': '',
                'label': u'Чудо 0.2л'
            },
            'color': 'positive'
        },
            {
                'action': {
                    'type': 'text',
                    'payload': '',
                    'label': u'Чудо шок 0.2л'
                },
                'color': 'positive'
            }],
        [{
            'action': {
                'type': 'text',
                'payload': '',
                'label': u'Чудо-Детки 0.27л'
            },
            'color': 'positive'
        },
            {
                'action': {
                    'type': 'text',
                    'payload': '',
                    'label': u'Мажитель J7 0.27л'
                },
                'color': 'positive'
            }],
        [{
            'action': {
                'type': 'text',
                'payload': '',
                'label': u'Мажитель 0.25л'
            },
            'color': 'positive'
        },
            {
                'action': {
                    'type': 'text',
                    'payload': '',
                    'label': u'Актимель 0.1л'
                },
                'color': 'positive'
            }],
        [{
            'action': {
                'type': 'text',
                'payload': '',
                'label': u'Актуаль 0.3л'
            },
            'color': 'positive'
        },
            {
                'action': {
                    'type': 'text',
                    'payload': '',
                    'label': u'Назад'
                },
                'color': 'negative'
            }]
    ]
}

keyboard_chocolate = {
    'one_time': False,
    'buttons': [
        [{
            'action': {
                'type': 'text',
                'payload': '',
                'label': u'Злак. батончик Матти'
            },
            'color': 'positive'
        }],
        [{
            'action': {
                'type': 'text',
                'payload': '',
                'label': u'Косичка зефирка'
            },
            'color': 'positive'
        }],
        [{
            'action': {
                'type': 'text',
                'payload': '',
                'label': u'Пирожное Фанни Банни'
            },
            'color': 'positive'
        }],
        [{
            'action': {
                'type': 'text',
                'payload': '',
                'label': u'Чоко пай'
            },
            'color': 'positive'
        }],
        [{
            'action': {
                'type': 'text',
                'payload': '',
                'label': u'Назад'
            },
            'color': 'negative'
        }]
    ]

}

keyboard_choosePastry = {
    'one_time': False,
    'buttons': [
        [{
            'action': {
                'type': 'text',
                'payload': '',
                'label': u'Мучные изделия 1'
            },
            'color': 'positive'
        }],
        [{
            'action': {
                'type': 'text',
                'payload': '',
                'label': u'Мучные изделия 2'
            },
            'color': 'positive'
        }],
        [{
            'action': {
                'type': 'text',
                'payload': '',
                'label': u'Назад'
            },
            'color': 'negative'
        }]
    ]
}

keyboard_pastry1 = {
    'one_time': False,
    'buttons': [
        [{
            'action': {
                'type': 'text',
                'payload': '',
                'label': u'Пицца Кальцоне'
            },
            'color': 'positive'
        },
            {
                'action': {
                    'type': 'text',
                    'payload': '',
                    'label': u'Пицца с сыром'
                },
                'color': 'positive'
            }
        ],
        [{
            'action': {
                'type': 'text',
                'payload': '',
                'label': u'Слойка фруктовая'
            },
            'color': 'positive'
        },
            {
                'action': {
                    'type': 'text',
                    'payload': '',
                    'label': u'Шафран с яблок.'
                },
                'color': 'positive'
            }
        ],
        [{
            'action': {
                'type': 'text',
                'payload': '',
                'label': u'Пышка сдобная'
            },
            'color': 'positive'
        },
            {
                'action': {
                    'type': 'text',
                    'payload': '',
                    'label': u'Слойка кукуруз.'
                },
                'color': 'positive'
            }
        ],
        [{
            'action': {
                'type': 'text',
                'payload': '',
                'label': u'Слойка с сыром'
            },
            'color': 'positive'
        },
            {
                'action': {
                    'type': 'text',
                    'payload': '',
                    'label': u'Сосиски в тесте'
                },
                'color': 'positive'
            }
        ],
        [{
            'action': {
                'type': 'text',
                'payload': '',
                'label': u'Штрудель вишн.'
            },
            'color': 'positive'
        },
            {
                'action': {
                    'type': 'text',
                    'payload': '',
                    'label': u'Штрудель яблоч.'
                },
                'color': 'positive'
            }
        ],
        [{
            'action': {
                'type': 'text',
                'payload': '',
                'label': u'Элеш с куриц.'
            },
            'color': 'positive'
        },
            {
                'action': {
                    'type': 'text',
                    'payload': '',
                    'label': u'Эчпочмак говяжий'
                },
                'color': 'positive'
            }
        ],
        [{
            'action': {
                'type': 'text',
                'payload': '',
                'label': u'Расстегай с горбушей и луком'
            },
            'color': 'positive'
        }],
        [{
            'action': {
                'type': 'text',
                'payload': '',
                'label': u'Пицца с колбасой и сыром'
            },
            'color': 'positive'
        }],
        [{
            'action': {
                'type': 'text',
                'payload': '',
                'label': u'Пицца с ветчиной куриной и сыром'
            },
            'color': 'positive'
        }],
        [{
            'action': {
                'type': 'text',
                'payload': '',
                'label': u'Назад в мучные изделия'
            },
            'color': 'negative'
        }]
    ]
}

keyboard_pastry2 = {
    'one_time': False,
    'buttons': [
        [{
            'action': {
                'type': 'text',
                'payload': '',
                'label': u'Ватрушка Франц.'
            },
            'color': 'positive'
        },
            {
                'action': {
                    'type': 'text',
                    'payload': '',
                    'label': u'Губадия с кортом'
                },
                'color': 'positive'
            }
        ],
        [{
            'action': {
                'type': 'text',
                'payload': '',
                'label': u'Пицца Ориг.'
            },
            'color': 'positive'
        },
            {
                'action': {
                    'type': 'text',
                    'payload': '',
                    'label': u'Пирожок с вишн.'
                },
                'color': 'positive'
            }
        ],
        [{
            'action': {
                'type': 'text',
                'payload': '',
                'label': u'Ватрушка с сыром'
            },
            'color': 'positive'
        },
            {
                'action': {
                    'type': 'text',
                    'payload': '',
                    'label': u'Сдоба с творог.'
                },
                'color': 'positive'
            }
        ],
        [{
            'action': {
                'type': 'text',
                'payload': '',
                'label': u'Пицца с куриц.,сыром'
            },
            'color': 'positive'
        },
            {
                'action': {
                    'type': 'text',
                    'payload': '',
                    'label': u'Губадия без яиц'
                },
                'color': 'positive'
            }
        ],
        [{
            'action': {
                'type': 'text',
                'payload': '',
                'label': u'Бэккен с капуст., яйцом'
            },
            'color': 'positive'
        },
            {
                'action': {
                    'type': 'text',
                    'payload': '',
                    'label': u'Вакбалиш с мяс.,рис'
                },
                'color': 'positive'
            }
        ],
        [{
            'action': {
                'type': 'text',
                'payload': '',
                'label': u'Пирожки печеные с мяс.,лук'
            },
            'color': 'positive'
        }],
        [{
            'action': {
                'type': 'text',
                'payload': '',
                'label': u'Пирожки печеные с мяс.,рис'
            },
            'color': 'positive'
        }],
        [{
            'action': {
                'type': 'text',
                'payload': '',
                'label': u'Пирожки слоеные с мясом'
            },
            'color': 'positive'
        }],
        [{
            'action': {
                'type': 'text',
                'payload': '',
                'label': u'Пирожки с черн. смородиной'
            },
            'color': 'positive'
        }],
        [{
            'action': {
                'type': 'text',
                'payload': '',
                'label': u'Назад в мучные изделия'
            },
            'color': 'negative'
        }]
    ]
}

keyboard_sweet = {
    'one_time': False,
    'buttons': [
        [{
            'action': {
                'type': 'text',
                'payload': '',
                'label': u'Пироги'
            },
            'color': 'positive'
        }],
        [{
            'action': {
                'type': 'text',
                'payload': '',
                'label': u'Печенье'
            },
            'color': 'positive'
        }],
        [{
            'action': {
                'type': 'text',
                'payload': '',
                'label': u'Пирожное'
            },
            'color': 'positive'
        }],
        [{
            'action': {
                'type': 'text',
                'payload': '',
                'label': u'Другое'
            },
            'color': 'positive'
        }],
        [{
            'action': {
                'type': 'text',
                'payload': '',
                'label': u'Назад'
            },
            'color': 'negative'
        }]
    ]
}

keyboard_pirogi = {
    'one_time': False,
    'buttons': [
        [{
            'action': {
                'type': 'text',
                'payload': '',
                'label': u'Творожный'
            },
            'color': 'positive'
        }],
        [{
            'action': {
                'type': 'text',
                'payload': '',
                'label': u'Трехслойник'
            },
            'color': 'positive'
        }],
        [{
            'action': {
                'type': 'text',
                'payload': '',
                'label': u'Домашний с маком'
            },
            'color': 'positive'
        }],
        [{
            'action': {
                'type': 'text',
                'payload': '',
                'label': u'Зебра'
            },
            'color': 'positive'
        }],
        [{
            'action': {
                'type': 'text',
                'payload': '',
                'label': u'Лимонный'
            },
            'color': 'positive'
        }],
        [{
            'action': {
                'type': 'text',
                'payload': '',
                'label': u'С малиной'
            },
            'color': 'positive'
        }],
        [{
            'action': {
                'type': 'text',
                'payload': '',
                'label': u'Назад конд.изделия'
            },
            'color': 'negative'
        }]
    ]
}

keyboard_pecenie = {
    'one_time': False,
    'buttons': [
        [{
            'action': {
                'type': 'text',
                'payload': '',
                'label': u'Земелах'
            },
            'color': 'positive'
        }],
        [{
            'action': {
                'type': 'text',
                'payload': '',
                'label': u'Курабье'
            },
            'color': 'positive'
        }],
        [{
            'action': {
                'type': 'text',
                'payload': '',
                'label': u'Мягкое'
            },
            'color': 'positive'
        }],
        [{
            'action': {
                'type': 'text',
                'payload': '',
                'label': u'Сдобное вкусное'
            },
            'color': 'positive'
        }],
        [{
            'action': {
                'type': 'text',
                'payload': '',
                'label': u'Сдобное листики'
            },
            'color': 'positive'
        }],
        [{
            'action': {
                'type': 'text',
                'payload': '',
                'label': u'Сдобное шоколадное'
            },
            'color': 'positive'
        }],
        [{
            'action': {
                'type': 'text',
                'payload': '',
                'label': u'Морковное'
            },
            'color': 'positive'
        }],
        [{
            'action': {
                'type': 'text',
                'payload': '',
                'label': u'Сдобное Американер'
            },
            'color': 'positive'
        }],
        [{
            'action': {
                'type': 'text',
                'payload': '',
                'label': u'Сдобное Американер с кунжутом'
            },
            'color': 'positive'
        }],
        [{
            'action': {
                'type': 'text',
                'payload': '',
                'label': u'Назад конд.изделия'
            },
            'color': 'negative'
        }]
    ]
}

keyboard_pirojnoe = {
    'one_time': False,
    'buttons': [
        [{
            'action': {
                'type': 'text',
                'payload': '',
                'label': u'Заварное'
            },
            'color': 'positive'
        }],
        [{
            'action': {
                'type': 'text',
                'payload': '',
                'label': u'Медовое'
            },
            'color': 'positive'
        }],
        [{
            'action': {
                'type': 'text',
                'payload': '',
                'label': u'Пампушки'
            },
            'color': 'positive'
        }],
        [{
            'action': {
                'type': 'text',
                'payload': '',
                'label': u'Песочное корзинка'
            },
            'color': 'positive'
        }],
        [{
            'action': {
                'type': 'text',
                'payload': '',
                'label': u'Песочное нарезное'
            },
            'color': 'positive'
        }],
        [{
            'action': {
                'type': 'text',
                'payload': '',
                'label': u'Песочное со сгущенкой'
            },
            'color': 'positive'
        }],
        [{
            'action': {
                'type': 'text',
                'payload': '',
                'label': u'Буше'
            },
            'color': 'positive'
        }],
        [{
            'action': {
                'type': 'text',
                'payload': '',
                'label': u'Назад конд.изделия'
            },
            'color': 'negative'
        }]
    ]
}

keyboard_otherSweet = {
    'one_time': False,
    'buttons': [
        [{
            'action': {
                'type': 'text',
                'payload': '',
                'label': u'Кекс'
            },
            'color': 'positive'
        },
            {
                'action': {
                    'type': 'text',
                    'payload': '',
                    'label': u'Круассан'
                },
                'color': 'positive'
        },
            {
                'action': {
                    'type': 'text',
                    'payload': '',
                    'label': u'Кольцо песоч.'
                },
                'color': 'positive'
        }],
        [{
            'action': {
                'type': 'text',
                'payload': '',
                'label': u'Корж молоч.'
            },
            'color': 'positive'
        },
            {
                'action': {
                    'type': 'text',
                    'payload': '',
                    'label': u'Корж яблоч.'
                },
                'color': 'positive'
        }],
        [{
            'action': {
                'type': 'text',
                'payload': '',
                'label': u'Маффин лимон.'
            },
            'color': 'positive'
        },
            {
                'action': {
                    'type': 'text',
                    'payload': '',
                    'label': u'Маффин цукат.'
                },
                'color': 'positive'
        }],
        [{
            'action': {
                'type': 'text',
                'payload': '',
                'label': u'Маффин шоколад.'
            },
            'color': 'positive'
        },
            {
                'action': {
                    'type': 'text',
                    'payload': '',
                    'label': u'Улитка с творогом'
                },
                'color': 'positive'
        }],
        [{
            'action': {
                'type': 'text',
                'payload': '',
                'label': u'Улитка с орехами'
            },
            'color': 'positive'
        },
            {
                'action': {
                    'type': 'text',
                    'payload': '',
                    'label': u'Язык слоеный'
                },
                'color': 'positive'
        }],
        [{
            'action': {
                'type': 'text',
                'payload': '',
                'label': u'Коврижка медов.'
            },
            'color': 'positive'
        },
            {
                'action': {
                    'type': 'text',
                    'payload': '',
                    'label': u'Сочень творог.'
                },
                'color': 'positive'
        }],
        [{
            'action': {
                'type': 'text',
                'payload': '',
                'label': u'Чак-чак'
            },
            'color': 'positive'
        },
            {
                'action': {
                    'type': 'text',
                    'payload': '',
                    'label': u'Конвертик слоеный'
                },
                'color': 'positive'
        }],
        [{
            'action': {
                'type': 'text',
                'payload': '',
                'label': u'Мешочки с яблоками'
            },
            'color': 'positive'
        }],
        [{
            'action': {
                'type': 'text',
                'payload': '',
                'label': u'Назад конд.изделия'
            },
            'color': 'negative'
        }]
    ]
}

keyboard_juice = {
    'one_time': False,
    'buttons': [
        [{
            'action': {
                'type': 'text',
                'payload': '',
                'label': u'Холодный чай 0.5л'
            },
            'color': 'positive'
        }],
        [{
            'action': {
                'type': 'text',
                'payload': '',
                'label': u'Холодный чай 0.3л'
            },
            'color': 'positive'
        }],
        [{
            'action': {
                'type': 'text',
                'payload': '',
                'label': u'Нектары и соки 0.2л'
            },
            'color': 'positive'
        }],
        [{
            'action': {
                'type': 'text',
                'payload': '',
                'label': u'Нектары и соки 0.95л'
            },
            'color': 'positive'
        }],
        [{
            'action': {
                'type': 'text',
                'payload': '',
                'label': u'Пюре груш Агуша 0.09л'
            },
            'color': 'positive'
        }],
        [{
            'action': {
                'type': 'text',
                'payload': '',
                'label': u'Соки фруктовые 0.33л'
            },
            'color': 'positive'
        }],
        [{
            'action': {
                'type': 'text',
                'payload': '',
                'label': u'Напиток цитрус 0.38л'
            },
            'color': 'positive'
        }],
        [{
            'action': {
                'type': 'text',
                'payload': '',
                'label': u'Напиток компотный 0.2л'
            },
            'color': 'positive'
        }],
        [{
            'action': {
                'type': 'text',
                'payload': '',
                'label': u'Назад'
            },
            'color': 'negative'
        }]
    ]
}

keyboard_water = {
    'one_time': False,
    'buttons': [
        [{
            'action': {
                'type': 'text',
                'payload': '',
                'label': u'Рита в Ритме 0.5л'
            },
            'color': 'positive'
        }],
        [{
            'action': {
                'type': 'text',
                'payload': '',
                'label': u'Святая чаша 0.45л'
            },
            'color': 'positive'
        }],
        [{
            'action': {
                'type': 'text',
                'payload': '',
                'label': u'Чистый глоток 0.5л'
            },
            'color': 'positive'
        }],
        [{
            'action': {
                'type': 'text',
                'payload': '',
                'label': u'Назад'
            },
            'color': 'negative'
        }]
    ]
}

keyboard_waffle = {
    'one_time': False,
    'buttons': [
        [{
            'action': {
                'type': 'text',
                'payload': '',
                'label': u'Вафли'
            },
            'color': 'positive'
        }],
        [{
            'action': {
                'type': 'text',
                'payload': '',
                'label': u'Назад'
            },
            'color': 'negative'
        }]
    ]
}

keyboard_coldFood = {
    'one_time': False,
    'buttons': [
        [{
            'action': {
                'type': 'text',
                'payload': '',
                'label': u'Апельсины'
            },
            'color': 'positive'
        }],
        [{
            'action': {
                'type': 'text',
                'payload': '',
                'label': u'Бананы'
            },
            'color': 'positive'
        }],
        [{
            'action': {
                'type': 'text',
                'payload': '',
                'label': u'Груши'
            },
            'color': 'positive'
        }],
        [{
            'action': {
                'type': 'text',
                'payload': '',
                'label': u'Колбаса полукопченая'
            },
            'color': 'positive'
        }],
        [{
            'action': {
                'type': 'text',
                'payload': '',
                'label': u'Мандарины'
            },
            'color': 'positive'
        }],
        [{
            'action': {
                'type': 'text',
                'payload': '',
                'label': u'Сыр'
            },
            'color': 'positive'
        }],
        [{
            'action': {
                'type': 'text',
                'payload': '',
                'label': u'Яблоки'
            },
            'color': 'positive'
        }],
        [{
            'action': {
                'type': 'text',
                'payload': '',
                'label': u'Назад'
            },
            'color': 'negative'
        }]
    ]
}

keyboard_compot = {
    'one_time': False,
    'buttons': [
        [{
            'action': {
                'type': 'text',
                'payload': '',
                'label': u'Компот сухофрукт 0.2л'
            },
            'color': 'positive'
        }],
        [{
            'action': {
                'type': 'text',
                'payload': '',
                'label': u'Компот вишня 0.2л'
            },
            'color': 'positive'
        }],
        [{
            'action': {
                'type': 'text',
                'payload': '',
                'label': u'Компот апельсин 0.2л'
            },
            'color': 'positive'
        }],
        [{
            'action': {
                'type': 'text',
                'payload': '',
                'label': u'Компот смородина 0.2л'
            },
            'color': 'positive'
        }],
        [{
            'action': {
                'type': 'text',
                'payload': '',
                'label': u'Компот изюм,курага 0.2л'
            },
            'color': 'positive'
        }],
        [{
            'action': {
                'type': 'text',
                'payload': '',
                'label': u'Компот изюм,урюк 0.2л'
            },
            'color': 'positive'
        }],
        [{
            'action': {
                'type': 'text',
                'payload': '',
                'label': u'Компот курага 0.2л'
            },
            'color': 'positive'
        }],
        [{
            'action': {
                'type': 'text',
                'payload': '',
                'label': u'Компот груша 0.2л'
            },
            'color': 'positive'
        }],
        [{
            'action': {
                'type': 'text',
                'payload': '',
                'label': u'Компот яблоч 0.2л'
            },
            'color': 'positive'
        }],
        [{
            'action': {
                'type': 'text',
                'payload': '',
                'label': u'Компот урюк 0.2л'
            },
            'color': 'positive'
        },
            {
            'action': {
                'type': 'text',
                'payload': '',
                'label': u'Назад'
            },
            'color': 'negative'
        }]
    ]
}

keyboard_drinks = {
    'one_time': False,
    'buttons': [
        [{
            'action': {
                'type': 'text',
                'payload': '',
                'label': u'Какао с молоком 0.2л'
            },
            'color': 'positive'
        }],
        [{
            'action': {
                'type': 'text',
                'payload': '',
                'label': u'Кофе с молоком 0.2л'
            },
            'color': 'positive'
        }],
        [{
            'action': {
                'type': 'text',
                'payload': '',
                'label': u'Напиток клюква 0.2л'
            },
            'color': 'positive'
        }],
        [{
            'action': {
                'type': 'text',
                'payload': '',
                'label': u'Напиток шиповник 0.2л'
            },
            'color': 'positive'
        }],
        [{
            'action': {
                'type': 'text',
                'payload': '',
                'label': u'Чай Гринфилд 0.2л'
            },
            'color': 'positive'
        }],
        [{
            'action': {
                'type': 'text',
                'payload': '',
                'label': u'Назад'
            },
            'color': 'negative'
        }]
    ]
}

keyboard_calc = {
    'one_time': True,
    'buttons': [
        [{
            'action': {
                'type': 'text',
                'payload': '',
                'label': u'Рассчитать идеальный вес'
            },
            'color': 'default'
        }],
        [{
            'action': {
                'type': 'text',
                'payload': '',
                'label': u'Рассчитать ИМТ'
            },
            'color': 'default'
        }],
        [{
            'action': {
                'type': 'text',
                'payload': '',
                'label': u'В начало'
            },
            'color': 'negative'
        }]
    ]
}

def get_answer(body):
   message = "Привет, я новый бот!"
   return message

def create_answer(data, token):
    user_id = data['user_id']
    request = data['body']
    parser = request.split(" ")
    if request.lower() == u'меню':
        message = u'Привет'
        vkapi.send_message(user_id, token, message, keyboard_main)
    elif request == u'Узнать школьное меню':
        message = u'http://www.poelidovolen.ru/parents/school-menu'
        vkapi.send_message(user_id, token, message, None)
    elif request == u'Назад':
        message = u'Выберите категорию'
        vkapi.send_message(user_id, token, message, keyboard_menu)
    elif request == u'Назад конд.изделия':
        message = u'Выберите категорию'
        vkapi.send_message(user_id, token, message, keyboard_sweet)
    elif request == u'Назад в мучные изделия':
        message = u'Выберите категорию'
        vkapi.send_message(user_id, token, message, keyboard_choosePastry)
    elif request == u'Составить обед':
        message = u'Здесь ты можешь составить себе обед'
        vkapi.send_message(user_id, token, message, keyboard_menu)
    elif request == u'Свободный выбор':
        message = u'Выберите блюдо'
        vkapi.send_message(user_id, token, message, keyboard_freeChoose)
    elif request == u'Молочная продукция':
        message = u'Выберите молочную продукцию'
        vkapi.send_message(user_id, token, message, keyboard_milkFood)
    elif request == u'Мучные изделия':
        message = u'Выберите мучные изделия'
        vkapi.send_message(user_id, token, message, keyboard_choosePastry)
    elif request == u'Мучные изделия 1':
        message = u'Выберите мучные изделия'
        vkapi.send_message(user_id, token, message, keyboard_pastry1)
    elif request == u'Мучные изделия 2':
        message = u'Выберите мучные изделия'
        vkapi.send_message(user_id, token, message, keyboard_pastry2)
    elif request == u'Вафли':
        message = u'Выберите вафли'
        vkapi.send_message(user_id, token, message, keyboard_waffle)
    elif request == u'Конфеты, шоколад':
        message = u'Выберите сладкое'
        vkapi.send_message(user_id, token, message, keyboard_chocolate)
    elif request == u'Соки':
        message = u'Выберите сок'
        vkapi.send_message(user_id, token, message, keyboard_juice)
    elif request == u'Вода':
        message = u'Выберите воду'
        vkapi.send_message(user_id, token, message, keyboard_water)
    elif request == u'Конд. изделия':
        message = u'Выберите тип кондитерского изделия'
        vkapi.send_message(user_id, token, message, keyboard_sweet)
    elif request == u'Пироги':
        message = u'Выберите пирог'
        vkapi.send_message(user_id, token, message, keyboard_pirogi)
    elif request == u'Печенье':
        message = u'Выберите печенье'
        vkapi.send_message(user_id, token, message, keyboard_pecenie)
    elif request == u'Пирожное':
        message = u'Выберите пирожное'
        vkapi.send_message(user_id, token, message, keyboard_pirojnoe)
    elif request == u'Другое':
        message = u'Выберите кондитерское изделие'
        vkapi.send_message(user_id, token, message, keyboard_otherSweet)
    elif request == u'Холодные закуски':
        message = u'Выберите холодные закуски'
        vkapi.send_message(user_id, token, message, keyboard_coldFood)
    elif request == u'Компоты':
        message = u'Выберите компот'
        vkapi.send_message(user_id, token, message, keyboard_compot)
    elif request == u'Напитки':
        message = u'Выберите напиток'
        vkapi.send_message(user_id, token, message, keyboard_drinks)
    elif request == u'Калькулятор веса':
        message = u'Выберите, что вы хотите рассчитать'
        vkapi.send_message(user_id, token, message, keyboard_calc)
    elif request == u'Рассчитать ИМТ':
        message = u'Для того, чтобы рассчитать ИМТ, напиши мне сообщение в формате:\n ИМТ рост вес (пример: ИМТ 170 60)'
        vkapi.send_message(user_id, token, message, keyboard_calc)
    elif request == u'Рассчитать идеальный вес':
        message = u'Для того, чтобы рассчитать идеальный вес, напиши мне сообщение в формате:\n ИВ пол(одна буква) рост (пример: ИВ М 170)'
        vkapi.send_message(user_id, token, message, keyboard_calc)
    elif parser[0].lower() == u'имт':
        ln = int(parser[1]) / 100
        w = int(parser[2])
        imt = w / (ln * ln)
        message = u'ИМТ: ' + str(imt) + '\n'
        if imt < 16:
            message += 'Выраженный дефицит массы тела'
        elif imt < 18.5:
            message += 'Недостаточная масса тела'
        elif imt < 25:
            message += 'Нормальный вес'
        elif imt < 30:
            message += 'Избыточная масса тела (предожирение)'
        elif imt < 35:
            message += 'Ожирение первой степени'
        elif imt < 40:
            message += 'Ожирение второй степени'
        else:
            message += 'Ожирение третьей степени'
        vkapi.send_message(user_id, token, message, keyboard_calc)
    elif parser[0].lower() == "ив":
        ln = int(parser[2])
        iw = 0
        if parser[1].lower() == "м":
            iw = (ln - 100) * 0.9
        else:
            iw = (ln - 100) * 0.85
        message = u'Ваш идеальный вес: ' + str(iw)
        vkapi.send_message(user_id, token, message, keyboard_calc)
    elif request == 'В начало':
        message = u'Выберите действие'
        vkapi.send_message(user_id, token, message, keyboard_main)
    elif request in product_id:
        dataBase.add(user_id, product_id[request])
        message = u'Блюдо добавлено в Ваш список'
        vkapi.send_message(user_id, token, message, keyboard_menu)
    elif request == u'Подвести итог':
        rows = dataBase.show(user_id)
        message = u'Ваш выбор:\n'
        counter = 0
        for i in rows:
            counter += 1
            message += str(counter) + '. ' + id_product[i[1]] + '\n'
        if counter == 0:
            message = u'Вы еще не сделали выбор'
        dataBase.delete(user_id)
        vkapi.send_message(user_id, token, message, keyboard_menu)
    elif request == u'Составить новый обед':
        dataBase.delete(user_id)