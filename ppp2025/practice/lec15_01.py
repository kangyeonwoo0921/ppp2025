def print_code(ch):
    print(f"{ch} => {ord(ch)}")

def print_char(code):
    print(f"{code} => {chr(code)}")


def to_upper(ch):
    # if 97 <= ord(ch) <=122:
    if 'a' <= ch <= 'z':
        return chr(ord(ch)-   32)
    return ch


def caesar_encode_ch(ch, shift):
    return chr(ord(ch) + shift)


def caesar_encode(text: str, shift: int = 3):
    full_text = []
    for ch in text:
        encoded_ch = caesar_encode_ch(ch, shift)
        full_text.append(encoded_ch)  
    print(full_text)

    return "".join(full_text)

def caesar_decode(text: str, shift: int = 3):
    return caesar_encode(text, -shift)





def main():
    print_code("a")
    print_code("b")
    print_char(97)
    print(to_upper("a"))    
    print(to_upper("B"))    
    
    print(caesar_encode("Hello"))
    print(caesar_decode("Khoor"))


if __name__=="__main__":
    main()