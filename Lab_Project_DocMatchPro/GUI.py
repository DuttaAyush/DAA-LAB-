import tkinter as tk
from tkinter import filedialog, messagebox
from DocMatchPro.docmatchpro import compare_documents

class DocMatchProUI:
    def __init__(self, root):
        self.root = root
        self.root.title("DocMatchPro - Plagiarism Checker")
        self.root.geometry("500x350")
        self.root.resizable(False, False)
        self.root.configure(bg="#f4f4f4")

        tk.Label(root, text="DocMatchPro", font=("Helvetica", 18, "bold"), bg="#f4f4f4", fg="#1b73e8").pack(pady=15)
        tk.Label(root, text="Select two documents to compare:", font=("Arial", 11), bg="#f4f4f4").pack()

        self.file1 = tk.StringVar()
        self.file2 = tk.StringVar()

        frame = tk.Frame(root, bg="#f4f4f4")
        frame.pack(pady=15)

        tk.Entry(frame, textvariable=self.file1, width=40, font=("Arial", 10)).grid(row=0, column=0, padx=5, pady=5)
        tk.Button(frame, text="Browse Doc 1", command=self.browse_doc1, bg="#1b73e8", fg="white", width=12).grid(row=0, column=1)

        tk.Entry(frame, textvariable=self.file2, width=40, font=("Arial", 10)).grid(row=1, column=0, padx=5, pady=5)
        tk.Button(frame, text="Browse Doc 2", command=self.browse_doc2, bg="#1b73e8", fg="white", width=12).grid(row=1, column=1)

        tk.Button(root, text="Check Plagiarism", command=self.run_check, bg="#34a853", fg="white", font=("Arial", 11, "bold"), width=20).pack(pady=20)

        self.result_label = tk.Label(root, text="", font=("Arial", 12, "bold"), bg="#f4f4f4", fg="#202124")
        self.result_label.pack(pady=10)

    def browse_doc1(self):
        path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        if path:
            self.file1.set(path)

    def browse_doc2(self):
        path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        if path:
            self.file2.set(path)

    def run_check(self):
        f1, f2 = self.file1.get(), self.file2.get()
        if not f1 or not f2:
            messagebox.showwarning("Missing File", "Please select both documents.")
            return
        try:
            result = compare_documents(f1, f2)
            self.result_label.config(text="{:.2f}% Plagiarism Detected\n✔ Plagiarism check completed!\nReport saved as 'comparison_report.csv'".format(result))
        except Exception as e:
            messagebox.showerror("Error", f"Something went wrong:\n{e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = DocMatchProUI(root)
    root.mainloop()
