def cipher(text, shift, encrypt=True):
    """
    Encrypts or decrypts a Caeser cipher.
    Parameters
    ---
    text: string
        Input string to be encrypted or decrypted. 
    shift: integer
        Integer value for alphabet shift times.
    encrypt: bool
        Boolean value determining whether the function encrypts or decrypts 'text' which defaults to be 'True'. Use false for decrypting. 
    Returns
    ---
    string
        The encrypted or decrypted 'text'.
    Examples
    ---
    Encryption:
    >>> from cipher_yz4122 import cipher_yz4122
    >>> cipherpkg.cipher('hi', 2, encrypt = True)
    'jk'
    Decryption:
    >>> from cipher_yz4122 import cipher_yz4122
    >>> cipherpkg.cipher('jk', 2, encrypt = False)
    'hi'
    """
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    new_text = ''
    for c in text:
        index = alphabet.find(c)
        if index == -1:
            new_text += c
        else:
            new_index = index + shift if encrypt == True else index - shift
            new_index %= len(alphabet)
            new_text += alphabet[new_index:new_index+1]
    return new_text