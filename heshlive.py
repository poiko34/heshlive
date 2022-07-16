def cipher12(text: str) -> str:
    shift = 2
    alphabet_lower = '0123456789qwretgshjeywy5цкеруноуоупв43йуявЫФВЧИТМТБТЬБЮЮРШЩГНЗ6ЕКННУЕЦЙФыавпваопрлджодэжш9гзpoikoqwertyuiop[]{}asdfghjkl;:zxcvbnm,./'
    alphabet_upper = alphabet_lower.upper()

    ord_first_letter_lower = ord('а')
    ord_first_letter_upper = ord('А')

    new_text = ''

    for i in text:
        if i in alphabet_lower:
            new_text += chr(((ord(i) - ord_first_letter_lower + shift) % 32) + ord_first_letter_lower)
        elif i in alphabet_upper:
            new_text += chr(((ord(i) - ord_first_letter_upper + shift) % 32) + ord_first_letter_upper)
        else:
            new_text += i
        hexx = f"{new_text}$#SHAS#${new_text}"

    return hexx

def cipher1(text: str) -> str:
    shift = 2
    alphabet_lower = '0123456789qwretgshjeywy5цкеруноуоупв43йуявЫФВЧИТМТБТЬБЮЮРШЩГНЗ6ЕКННУЕЦЙФыавпваопрлджодэжш9гзpoikoqwertyuiop[]{}asdfghjkl;:zxcvbnm,./'
    alphabet_upper = alphabet_lower.upper()

    ord_first_letter_lower = ord('а')
    ord_first_letter_upper = ord('А')

    new_text = ''

    for i in text:
        if i in alphabet_lower:
            new_text += chr(((ord(i) - ord_first_letter_lower + shift) % 32) + ord_first_letter_lower)
        elif i in alphabet_upper:
            new_text += chr(((ord(i) - ord_first_letter_upper + shift) % 32) + ord_first_letter_upper)
        else:
            new_text += i
        hexx = f"{new_text}"

    return hexx

def cipher64(text: str) -> str:
    hexx = cipher1(text)
    hexx = cipher1(hexx)
    hexx = cipher12(hexx)
    return hexx

def cipher216(text: str) -> str:
    hexx = cipher12(text)
    hexx = cipher12(hexx)
    hexx = cipher64(hexx)
    hexx = cipher1(hexx)
    return hexx
