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


    ls = []
    words = ''
    
    for line in data:
        matches = re.finditer(regex_pattern, line)
        
        for m in matches: 
            line = re.sub(m.group().strip(), '', line)

        ls.append(line)

    return ls

def replace_emoticons(data, emoticon_list):
    """
    substitui chaves do dicionario emoticon_list
    pelos valores 
    """
    ls = []

    for line in data:
        for exp in emoticon_list:
            line = line.replace(exp, emoticon_list[exp])

        ls.append(line)

    return ls

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
