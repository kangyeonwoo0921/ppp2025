def caesar_encode_ch(ch, shift):
    return chr(ord(ch) + shift)


def caesar_encode(text: str, shift: int = 3) -> str:
    full_text =[]
    for ch in text:
        encoded_ch = caesar_encode_ch(ch, shift)
        full_text.append(encoded_ch)
    
    return "".join(full_text)



def caesar_decode(text: str, shift: int = 3) -> str:
    return caesar_encode(text, -shift)

def  main():
    x = input("인코딩할 문자를 입력하시오:")
    print(caesar_encode(x))
    
    y = input("디코딩할 문자를 입력하시오:")
    print(caesar_decode(y))
    
if __name__=="__main__":
    main()