import tkinter as tk
from tkinter import simpledialog
import rich

window = tk.Tk()
window.withdraw()

def gui_input(text: str) -> str:
    return simpledialog.askstring(title="입력창", prompt=text)




def main():
    # name = gui_input("이름이 뭔가요?")
    name ="홍길동"
    
    rich.print(f"[bold magenta]{name}[/bold magenta]님 반갑습니다! :vampire:")

if __name__=="__main__":
    main()