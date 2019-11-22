from ru.yandex import translator as tr
from ru.yandex.validation import Config

s = 'Тестирование перевода'
print(tr.Query.translate(s))

path = 'aquamatix/apps/aquamatix_mvp/configs/config.ini'
print(open(path, 'r'))
name = Config(path).get_attribute('maria_db', 'NAME')
user = Config(path).get_attribute('maria_db', 'USER')
password = Config(path).get_attribute('maria_db', 'PASSWORD')
host = Config(path).get_attribute('maria_db', 'HOST')
print(name, user, password, host)
