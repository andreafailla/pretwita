import re, string

def is_date(token:str):
    # TODO add punctuation guard...
    token = token.translate(str.maketrans('', '', string.punctuation))
    return (len(token) == 4) and (1900 <= int(token) <= 2099)

def get_urls():
    return re.compile(
        r'(https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|https?:\/\/(?:www\.|(?!www))'
        r'[a-zA-Z0-9]\.[^\s]{2,}|www\.[a-zA-Z0-9]\.[^\s]{2,})')

def get_emojis():
    try:
        # UCS-4
        emojis_pattern = re.compile(u'([\U00002600-\U000027BF])|([\U0001f300-\U0001f64F])|([\U0001f680-\U0001f6FF])')
    except re.error:
        # UCS-2
        emojis_pattern = re.compile(
            u'([\u2600-\u27BF])|([\uD83C][\uDF00-\uDFFF])|([\uD83D][\uDC00-\uDE4F])|([\uD83D][\uDE80-\uDEFF])')
    return emojis_pattern

def get_emoticons():
    eyes, noses, mouths = r":;8BX=", r"-~'^", r")(/\|DP"
    emoticons = "[%s][%s]?[%s]" % tuple(map(re.escape, [eyes, noses, mouths]))
    return re.compile(emoticons)

def get_hashtags():
    return re.compile(r'#\w*')

def get_reserved_words():
    return re.compile(r'\s+(RT|rt|FAV|fav)')

def get_mentions():
    return re.compile(r'@\w*')

def get_multiple_spaces():
    return re.compile(r'\s{2,}|\t')

def get_element(pattern):
    pass
