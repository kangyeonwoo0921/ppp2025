def str2float(text:str, default_value: float = -999) -> float:
    try:
        return float(text)
    except ValueError:
        print(f"에러났어요...!{text}!")
        return default_value


def main():
    print(str2float("0.5", 0))
    print(str2float("3.555", 0))
    print(str2float("3.5.55", 0))

if __name__=="__main__":
    main()