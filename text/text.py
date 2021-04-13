from nltk.tokenize import wordpunct_tokenize

import re 


def remove_url(data: str) -> list:
    """Remove a ocorrencia de urls em blocos de texto.

    Args:
        data (str): bloco de texto que você quer remover os urls.

    Returns:
        list: lista com cada letra.
    """

    output = []
    words = ''
    
    http_str = 'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
    www_str = 'www?.(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'

    http_exp = re.compile(http_str)
    www_exp = re.compile(www_str)

    url_exps = [http_exp, www_exp]
    
    for line in data:

        for exp in url_exps:
            urls = exp.findall(line)
            for u in urls:
                line = line.replace(u, ' ')    
            
        output.append(line)
    
    return output

def remove_regex(data, regex_pattern):
    """
    remove um dado padrão regex
    """


    output = []
    words = ''
    
    for line in data:
        matches = re.finditer(regex_pattern, line)
        
        for m in matches: 
            line = re.sub(m.group().strip(), '', line)

        output.append(line)

    return output

def remove_emoticons(data: str) -> list:
    """Remove emoticons de um dado texto

    Args:
        data (str): Texto no qual quer remover emoticons

    Returns:
        list: lista de caracteres sem emoticon
    """
    
    emoticon_regex = re.compile(pattern = "["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           "]+", flags = re.UNICODE)
    
    output = []

    for line in data:
        line =  emoticon_regex.sub(r'',line)

        output.append(line)

    return output

def tokenize_text(data):
    """
    tokeniza
    """
    ls = []

    for line in data:
        tokens = wordpunct_tokenize(line)
        ls.append(tokens)

    return ls

def apply_standardization(tokens, std_list):
    """
    padroniza

    exemplo de std_list : std_list = {'eh': 'é', 'vc': 'você' ... etc}
    """
    ls = []

    for tk_line in tokens:
        new_tokens = []
        
        for word in tk_line:
            if word.lower() in std_list:
                word = std_list[word.lower()]
                
            new_tokens.append(word) 
            
        ls.append(new_tokens)

    return ls

def remove_stopwords(tokens, stopword_list):
    """
    remove palavras de passagem
    """
    ls = []

    for tk_line in tokens:
        new_tokens = []
        
        for word in tk_line:
            if word.lower() not in stopword_list:
                new_tokens.append(word) 
            
        ls.append(new_tokens)
        
    return ls

def apply_stemmer(tokens):
    """
    Aplica o stemmer aos tokes
    """
    ls = []
    stemmer = nltk.stem.RSLPStemmer()

    for tk_line in tokens:
        new_tokens = []
        
        for word in tk_line:
            word = str(stemmer.stem(word))
            new_tokens.append(word) 
            
        ls.append(new_tokens)
        
    return ls

def untokenize_text(tokens):
    """
    destokeniza
    """
    ls = []

    for tk_line in tokens:
        new_line = ''
        
        for word in tk_line:
            new_line += word + ' '
            
        ls.append(new_line)
        
    return ls

def get_text_cloud(tokens):
    """
    faz a nuvem
    """
    text = ''

    for tk_line in tokens:
        new_tokens = []
        
        for word in tk_line:
            text += word + ' '
        
    return text

def get_freq_dist_list(tokens):
    """
    fprepara os tokens para obter a lista de frequencia das palavras usando FreqDist
    from nltk.probability import FreqDist (nao curto muito essa abordagem aqui)
    """
    ls = []

    for tk_line in tokens:
        for word in tk_line:
            ls.append(word)

    return ls
