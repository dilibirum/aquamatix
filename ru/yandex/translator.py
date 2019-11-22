import urllib.request as ur
import urllib.parse as up
import re
from .validation import Config


class Query:
    config = Config('aquamatix/apps/aquamatix_mvp/configs/config.ini')
    key = config.get_attribute('yandex', 'key')
    base = 'https://translate.yandex.net/api/v1.5/tr/translate'
    lang = 'en'
    format = 'plain'  # текст без разметки
    options = '1'
    callback = 'get_text'
    host = 'translate.yandex.net'
    accept = '* / *'
    content_type = 'application / x - www - form - urlencoded'

    @classmethod
    def get_xml_query(cls, text):
        return f'{cls.base}?key={cls.key}&text={up.quote(text)}&lang={cls.lang}&format={cls.format}&options={cls.options}'

    @classmethod
    def translate(cls, text: str) -> str:
        link = ur.urlopen(cls.get_xml_query(text))
        text = str(link.read())
        index_start = re.search('<text>', text).end()
        index_end = re.search('</text>', text).start()
        return text[index_start: index_end]
