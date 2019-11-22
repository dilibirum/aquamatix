import configparser as c
import re


class Token:
    path = ''

    def __init__(self, path: str):
        self.path = path

    def get_rsa_key(self):
        return self.parse_rsa_key(self.file_to_text())

    def get_public_keys(self):
        return self.parse_public_keys_list(self.file_to_text())

    def parse_rsa_key(self, text: str):
        index_start = re.search('-----BEGIN RSA PUBLIC KEY-----', text).end()
        index_end = re.search('-----END RSA PUBLIC KEY-----', text).start()
        return text[index_start: index_end]

    def file_to_text(self):
        try:
            file = open(self.path, 'r')
            text = file.read()
        except FileNotFoundError:
            return 'File not found! Check the path'
        return text

    def del_rsa_key(self, text: str):
        index_start = re.search('-----END RSA PUBLIC KEY-----', text).end()
        return text[index_start + 2:]

    def parse_public_keys_list(self, text: str):
        text = self.del_rsa_key(text)
        text = text.replace('-----BEGIN PUBLIC KEY-----', '')
        keys = text.split('-----END PUBLIC KEY-----')
        for k in keys:
            k.replace(' ', '')
            if k == '\n':
                keys.remove(k)
        return keys


class Config:
    path: str

    def __init__(self, path: str):
        self.path = path

    def get_attribute(self, section: str, name: str):
        config = c.RawConfigParser()
        config.read(self.path)
        return config[section][name]
