import tkinter as tk

class SimpleCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.running_total = 0
        
        self.label_title = tk.Label(root, text="Total:", font=("Arial", 10))
        self.label_title.grid(row=0, column=0, sticky="w", padx=5, pady=(10, 2))
        
        self.label_val = tk.Label(root, text="0", font=("Arial", 10))
        self.label_val.grid(row=0, column=2, sticky="e", padx=5, pady=(10, 2))

        self.entry_num = tk.Entry(root, width=25)
        self.entry_num.grid(row=1, column=0, columnspan=3, padx=10, pady=5)
        self.entry_num.focus_set()

        self.btn_add = tk.Button(root, text="+", width=4, command=self.add)
        self.btn_add.grid(row=2, column=0, padx=5, pady=10)

        self.btn_sub = tk.Button(root, text="-", width=4, command=self.subtract)
        self.btn_sub.grid(row=2, column=1, padx=5, pady=10)

        self.btn_reset = tk.Button(root, text="Reset", width=8, command=self.reset)
        self.btn_reset.grid(row=2, column=2, padx=5, pady=10)

    def add(self):
        try:
            value = int(self.entry_num.get())
            self.running_total += value
            self.update_ui()
        except ValueError:
            pass 

    def subtract(self):
        try:
            value = int(self.entry_num.get())
            self.running_total -= value
            self.update_ui()
        except ValueError:
            pass

    def reset(self):
        self.running_total = 0
        self.update_ui()

    def update_ui(self):
        self.label_val.config(text=str(self.running_total))
        self.entry_num.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    root.config(padx=10, pady=10)
    app = SimpleCalculator(root)
    root.mainloop()