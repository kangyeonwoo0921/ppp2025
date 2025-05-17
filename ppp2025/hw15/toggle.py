def toggle_text(text:str) -> str:
    
    result = ""
    for ch in text:
        if 'a' <= ch <= 'z':
            result += chr(ord(ch)-32)
        
        elif 'A' <= ch <="Z":
            result += chr(ord(ch) + 32)
        
        else:
            result += ch
        
    return result




def main():
    
    x = input("문자를 입력하시오: ")
    print(toggle_text(x))
    
    
    
    
if __name__=="__main__":
    main()