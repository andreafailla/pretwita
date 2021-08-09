<span>
<img src="./logo.png" width="100px" align="justify"/>
</span>

# PreTwITA
<code><b>PreTwITA</b></code> is an open source <b>Pre</b>processor for <b>Tw</b>eets in the <b>ITA</b>lian language written in Python. The purpose of such library is to provide the user with language-specific tools for text cleaning (i.e. the process of preparing raw text for Natural Language Processing). 

## Included features
- correction of most common italian abbreviations (e.g. <i>xk</i> replaced with <i>perché</i>)
- remove urls 
- remove emojis 
- remove emoticons 
- remove mentions 
- remove hashtags 
- remove twitter reserved words (i.e. 'rt' and 'fav')
- remove stopwords 
    - an option to define additional stopwords
- remove punctuation 
- remove numbers 
    - an option to avoid removing dates in <i>yyyy</i> format
- remove multiple spaces 
- tokenization

## Installing PreTwITA
You can install PreTwITA via pip
<br>
<code>python -m pip install pretwita</code>

## Usage
For usage and tips, please refer to the <code>demo.ipynb</code> file
