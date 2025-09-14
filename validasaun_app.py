import re
import tkinter as tk
from tkinter import ttk, messagebox

class ValidasaunApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Validasaun Númeru Telefone no Email - Timor-Leste")
        self.root.geometry("500x400")
        self.root.configure(bg="#f0f0f0")
        
        # Style configuration
        style = ttk.Style()
        style.configure("TFrame", background="#f0f0f0")
        style.configure("TLabel", background="#f0f0f0", font=("Arial", 10))
        style.configure("TButton", font=("Arial", 10))
        style.configure("Header.TLabel", font=("Arial", 14, "bold"), foreground="#2c3e50")
        
        # Create main frame
        main_frame = ttk.Frame(root, padding="20")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Header
        header = ttk.Label(main_frame, text="Validasaun Númeru Telefone no Email", style="Header.TLabel")
        header.grid(row=0, column=0, columnspan=2, pady=(0, 20))
        
        # Phone validation section
        phone_label = ttk.Label(main_frame, text="Númeru Telefone (Timor-Leste):")
        phone_label.grid(row=1, column=0, sticky=tk.W, pady=(5, 2))
        
        self.phone_entry = ttk.Entry(main_frame, width=30, font=("Arial", 10))
        self.phone_entry.grid(row=2, column=0, sticky=(tk.W, tk.E), pady=(0, 10))
        self.phone_entry.insert(0, "77xxxxxx")
        
        phone_btn = ttk.Button(main_frame, text="Validasaun", command=self.validate_phone)
        phone_btn.grid(row=2, column=1, padx=(10, 0))
        
        self.phone_result = ttk.Label(main_frame, text="", foreground="red")
        self.phone_result.grid(row=3, column=0, columnspan=2, sticky=tk.W, pady=(0, 20))
        
        # Email validation section
        email_label = ttk.Label(main_frame, text="Email:")
        email_label.grid(row=4, column=0, sticky=tk.W, pady=(5, 2))
        
        self.email_entry = ttk.Entry(main_frame, width=30, font=("Arial", 10))
        self.email_entry.grid(row=5, column=0, sticky=(tk.W, tk.E), pady=(0, 10))
        self.email_entry.insert(0, "exemplu@gmail.com")
        
        email_btn = ttk.Button(main_frame, text="Validasaun", command=self.validate_email)
        email_btn.grid(row=5, column=1, padx=(10, 0))
        
        self.email_result = ttk.Label(main_frame, text="", foreground="red")
        self.email_result.grid(row=6, column=0, columnspan=2, sticky=tk.W, pady=(0, 20))
        
        # Examples section
        examples_label = ttk.Label(main_frame, text="Ezemplu sira:", style="Header.TLabel")
        examples_label.grid(row=7, column=0, sticky=tk.W, pady=(10, 5))
        
        examples_text = tk.Text(main_frame, height=8, width=50, font=("Arial", 9), bg="white", relief=tk.FLAT)
        examples_text.grid(row=8, column=0, columnspan=2, sticky=(tk.W, tk.E))
        
        examples = """
        Númeru Telefone Válidu:
        • 77123456, 78123456, 73123456, 74123456, 75123456
        
        Email Válidu:
        • lucas180502@gmail.com, exemplo@hotmail.com, nome.apelido@xyz.org
        """
        
        examples_text.insert(tk.END, examples)
        examples_text.config(state=tk.DISABLED)
        
        # Configure grid weights
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(0, weight=1)
    
    def valida_numero_telemovel(self, numero):
        """
        Funsaun atu valida númeru telemóvel iha Timor-Leste.
        
        Padraun regex: ^(77|78|73|74|75)\d{6}$
        - ^: komesa ho
        - (77|78|73|74|75): númeru komesa ho 77, 78, 73, 74, ka 75
        - \d{6}: tuirmai ho númeru 6
        - $: hotu ho
        """
        # Remove espaços e outros caracteres não numéricos
        numero = re.sub(r'\D', '', numero)
        
        padraun = re.compile(r'^(77|78|73|74|75)\d{6}$')
        if padraun.match(numero):
            return True
        else:
            return False
    
    def valida_email(self, email):
        """
        Funsaun atu valida email.
        
        Padraun regex: ^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$
        - ^: komesa ho
        - [a-zA-Z0-9._%+-]+: karakter alfanumeriku (letra, numeru) no simbolu (_ . % + -) ida ka liu
        - @: tuir ho simbolu @
        - [a-zA-Z0-9.-]+: tuir ho karakter alfanumeriku (letra, numeru) no simbolu (. -) ida ka liu
        - \.: tuir ho pontu ida
        - [a-zA-Z]{2,}: tuir ho letra 2 ka liu (ez: com, net, org)
        - $: hotu ho
        """
        padraun = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
        if padraun.match(email):
            return True
        else:
            return False
    
    def validate_phone(self):
        numero = self.phone_entry.get()
        if self.valida_numero_telemovel(numero):
            self.phone_result.config(text="Númeru Telefone VÁLIDU!", foreground="green")
        else:
            self.phone_result.config(text="Númeru Telefone INVALIDU!", foreground="red")
    
    def validate_email(self):
        email = self.email_entry.get()
        if self.valida_email(email):
            self.email_result.config(text="Email VÁLIDU!", foreground="green")
        else:
            self.email_result.config(text="Email INVALIDU!", foreground="red")

def main():
    root = tk.Tk()
    app = ValidasaunApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()