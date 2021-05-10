import json 

# ensure_asciiをFalseにする。 jsonstreamsの仕様上この方法でしている。
class EnsureAsciiFalseEncoder(json.JSONEncoder):

    def __init__(self, *args, **kwargs):
        kwargs['ensure_ascii'] = False
        super().__init__(*args, **kwargs)