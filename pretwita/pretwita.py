import string, re
from .constants import IT_STOPWORDS, IT_ABBREVIATIONS, FUNCTIONS
from .patterns import get_multiple_spaces, get_urls, get_emoticons, get_emojis, \
                    get_hashtags, get_mentions, get_reserved_words, is_date  

class PreTwITA:
    def __init__(self, text: str):       
        self.text = text

    def clean(self, placeholder=False, additional_stopwords=None, keep_dates=False):
        """
        Full tweet cleaning pipeline

        :param placeholder: if true, replace patterns with placeholders instead of removing, defaults to False
        :type placeholder: bool, optional
        :param additional_stopwords: a list of additional stopwords to remove, defaults to None
        :type additional_stopwords: list[str], optional
        :param keep_dates: choice to remove/keep dates while removing numbers, defaults to False
        :type keep_dates: bool, optional
        :return: A clean PreTwITA object
        """        
        return self \
            .to_lower() \
            .correct_abbreviations() \
            .remove_urls(placeholder=placeholder) \
            .remove_emojis(placeholder=placeholder) \
            .remove_emoticons(placeholder=placeholder) \
            .remove_mentions(placeholder=placeholder) \
            .remove_hashtags(placeholder=placeholder) \
            .remove_reserved_words(placeholder=placeholder) \
            .remove_stopwords(additional_stopwords=additional_stopwords) \
            .remove_punctuation() \
            .remove_numbers(keep_dates=keep_dates) \
            .remove_multiple_spaces()

    def to_lower(self):
        self.text = self.text.lower()
        return self

    def correct_abbreviations(self):
        tokens = self.text.split()
        out_tokens_list = []
        for token in tokens:
            stripped = token.translate(str.maketrans('', '', string.punctuation))
            if stripped in IT_ABBREVIATIONS.keys():
                out_tokens_list.append(IT_ABBREVIATIONS[stripped])
            else:
                out_tokens_list.append(token)
        self.text = ' '.join(out_tokens_list)
        return self

    def remove_urls(self, placeholder=False):
        if placeholder:
            self.text = re.sub(pattern=get_urls(), repl='xxURLxx', string=self.text)
        else:
            self.text = re.sub(pattern=get_urls(), repl='', string=self.text)
        return self

    def remove_emojis(self, placeholder=False):
        if placeholder:
            self.text = re.sub(pattern=get_emojis(), repl='xxEMOJIxx ', string=self.text)
        else:
            self.text = re.sub(pattern=get_emojis(), repl=' ', string=self.text)

        return self

    def remove_emoticons(self, placeholder=False):
        if placeholder:
            self.text = re.sub(pattern=get_emoticons(), repl='xxEMOTICONxx', string=self.text)
        else:
            self.text = re.sub(pattern=get_emoticons(), repl='', string=self.text)
        return self

    def remove_mentions(self, placeholder=False):
        if placeholder:
            self.text = re.sub(pattern=get_mentions(), repl='xxMENTIONxx', string=self.text)
        else:
            self.text = re.sub(pattern=get_mentions(), repl='', string=self.text)
        return self

    def remove_hashtags(self, placeholder=False):
        if placeholder:
            self.text = re.sub(pattern=get_hashtags(), repl='xxHASHTAGxx', string=self.text)
        else:
            self.text = re.sub(pattern=get_hashtags(), repl='', string=self.text)
        return self

    def remove_reserved_words(self, placeholder=False):
        if placeholder:
            self.text = re.sub(pattern=get_reserved_words(), repl=' xxRESERVEDxx', string=self.text)
        else:
            self.text = re.sub(pattern=get_reserved_words(), repl=' ', string=self.text)
        return self

    def remove_stopwords(self, additional_stopwords=None):
        if additional_stopwords is None:
            additional_stopwords = []
        tokens = self.text.split()
        stop_words = IT_STOPWORDS + additional_stopwords
        out_tokens_list = []
        for token in tokens:
            if token not in stop_words:
                out_tokens_list.append(token)
        self.text = ' '.join(out_tokens_list)
        return self
   
    def remove_punctuation(self):
        self.text = self.text.translate(str.maketrans('', '', string.punctuation))
        return self 

    def remove_numbers(self, keep_dates=False):
        tokens = self.text.split()
        for token in tokens:
            if token.isnumeric():
                if keep_dates:
                    if not is_date(token):
                        tokens.remove(token)
                else:
                    tokens.remove(token)
        self.text = ' '.join(tokens)
        return self
    
    def remove_multiple_spaces(self):
        self.text = re.sub(pattern=get_multiple_spaces(), repl=' ', string=self.text)
        return self

    def get_tokens(self) -> list:
        return self.text.split()

    def __str__(self):
        return self.text

    def available_functions():
        for funct in FUNCTIONS:
            print(funct) 
    