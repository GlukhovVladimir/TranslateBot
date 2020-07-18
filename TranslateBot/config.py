import pymysql


TOKEN = 'TOKEN'
STARTMSG = "Привет, я бот переводчик. Для перевода используется сайт Google Translate.У бота есть два режима: 1) Изменяет правила перевода с английского на русский 2) Изменяет правила перевода с русского на аглийский. Чтобы изменить язык наберите /choose , затем кликните на нужную кнопку в окне"
CHOSEMSG = "Choose lang"
LANGUES = ['ru', 'en']
LANGDICT = {
    'ru': 'Russian',
    'en': 'English'
}


mydb = pymysql.connect(
    host="host",
    user="riptized",
    passwd="password",
    database="database1"
)