"""
Linux File Permission Manager
A Tkinter GUI to understand Unix permissions and generate chmod commands.
No third-party dependencies required.
"""
import tkinter as tk
from tkinter import ttk, messagebox
import re

PERMISSIONS = ("Read", "Write", "Execute")
ROLES = ("Owner", "Group", "Others")
BITS = {"Read": 4, "Write": 2, "Execute": 1}
SYMBOLS = {"Read": "r", "Write": "w", "Execute": "x"}

class PermissionManager(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Linux File Permission Manager")
        self.geometry("900x700")
        self.minsize(760, 620)
        self.configure(bg="#f3f6fb")
        self.vars = {
            role: {perm: tk.BooleanVar(value=default) for perm, default in
                   zip(PERMISSIONS, defaults)}
            for role, defaults in zip(ROLES, ((True, True, False), (True, False, False), (False, False, False)))
        }
        self.filename = tk.StringVar(value="myfile.txt")
        self.symbolic = tk.StringVar()
        self.octal = tk.StringVar()
        self.command = tk.StringVar()
        self._build_ui()
        self.update_preview()

    def _build_ui(self):
        header = tk.Frame(self, bg="#172554", padx=26, pady=22)
        header.pack(fill="x")
        tk.Label(header, text="LINUX FILE PERMISSION MANAGER",
                 bg="#172554", fg="white", font=("Arial", 18, "bold")).pack(anchor="w")
        tk.Label(header, text="Understand rwx permissions • Build chmod commands",
                 bg="#172554", fg="#bfdbfe", font=("Arial", 10)).pack(anchor="w", pady=(5, 0))

        main = tk.Frame(self, bg="#f3f6fb", padx=24, pady=18)
        main.pack(fill="both", expand=True)

        tk.Label(main, text="1. Select permissions", bg="#f3f6fb", fg="#172554",
                 font=("Arial", 14, "bold")).pack(anchor="w", pady=(0, 10))

        cards = tk.Frame(main, bg="#f3f6fb")
        cards.pack(fill="x")
        descriptions = {
            "Owner": "The file's user / creator",
            "Group": "Users in the assigned group",
            "Others": "Everyone else"
        }
        for role in ROLES:
            card = tk.LabelFrame(cards, text=role, bg="white", fg="#1e3a8a",
                                 font=("Arial", 11, "bold"), padx=14, pady=12,
                                 labelanchor="nw")
            card.pack(side="left", fill="both", expand=True, padx=(0, 10))
            tk.Label(card, text=descriptions[role], bg="white", fg="#64748b",
                     font=("Arial", 9), wraplength=180).pack(anchor="w", pady=(0, 12))
            for perm in PERMISSIONS:
                ttk.Checkbutton(card, text=perm, variable=self.vars[role][perm],
                                command=self.update_preview).pack(anchor="w", pady=4)

        tk.Label(main, text="2. Preview permissions", bg="#f3f6fb", fg="#172554",
                 font=("Arial", 14, "bold")).pack(anchor="w", pady=(22, 10))
        preview = tk.Frame(main, bg="white", padx=18, pady=15,
                           highlightbackground="#dbe4f0", highlightthickness=1)
        preview.pack(fill="x")
        row = tk.Frame(preview, bg="white")
        row.pack(fill="x")
        tk.Label(row, text="Symbolic permission", bg="white", fg="#475569",
                 font=("Arial", 10)).pack(side="left")
        tk.Label(row, textvariable=self.symbolic, bg="#eff6ff", fg="#1d4ed8",
                 font=("Courier New", 22, "bold"), padx=14, pady=5).pack(side="right")
        row2 = tk.Frame(preview, bg="white")
        row2.pack(fill="x", pady=(10, 0))
        tk.Label(row2, text="Octal value", bg="white", fg="#475569",
                 font=("Arial", 10)).pack(side="left")
        tk.Label(row2, textvariable=self.octal, bg="#f1f5f9", fg="#0f172a",
                 font=("Courier New", 18, "bold"), padx=14, pady=4).pack(side="right")
        self.explanation = tk.Label(preview, text="", bg="white", fg="#334155",
                                    justify="left", font=("Arial", 10), anchor="w")
        self.explanation.pack(fill="x", pady=(12, 0))

        tk.Label(main, text="3. Generate chmod command", bg="#f3f6fb", fg="#172554",
                 font=("Arial", 14, "bold")).pack(anchor="w", pady=(22, 10))
        cmd_box = tk.Frame(main, bg="white", padx=18, pady=15,
                           highlightbackground="#dbe4f0", highlightthickness=1)
        cmd_box.pack(fill="x")
        tk.Label(cmd_box, text="Target file name / path", bg="white", fg="#475569",
                 font=("Arial", 10)).pack(anchor="w")
        entry = ttk.Entry(cmd_box, textvariable=self.filename, font=("Arial", 11))
        entry.pack(fill="x", pady=(5, 12))
        entry.bind("<KeyRelease>", lambda _e: self.update_preview())
        self.command_label = tk.Label(cmd_box, textvariable=self.command, bg="#0f172a",
                                      fg="#bbf7d0", font=("Courier New", 12, "bold"),
                                      padx=12, pady=12, anchor="w")
        self.command_label.pack(fill="x")
        buttons = tk.Frame(cmd_box, bg="white")
        buttons.pack(fill="x", pady=(12, 0))
        ttk.Button(buttons, text="Copy command", command=self.copy_command).pack(side="left")
        ttk.Button(buttons, text="Reset example", command=self.reset).pack(side="left", padx=8)

        footer = tk.Label(main, text="Note: This tool generates a command only. It does not change files on your computer.",
                          bg="#f3f6fb", fg="#64748b", font=("Arial", 9))
        footer.pack(anchor="w", pady=(15, 0))

    def update_preview(self):
        groups = []
        octal = []
        explain = []
        for role in ROLES:
            chars = "".join(SYMBOLS[p] if self.vars[role][p].get() else "-" for p in PERMISSIONS)
            value = sum(BITS[p] for p in PERMISSIONS if self.vars[role][p].get())
            groups.append(chars)
            octal.append(str(value))
            labels = [p.lower() for p in PERMISSIONS if self.vars[role][p].get()]
            explain.append(f"{role}: {', '.join(labels) if labels else 'no access'}")
        self.symbolic.set("-" + "".join(groups))
        self.octal.set("".join(octal))
        self.explanation.config(text="   •   ".join(explain))
        target = self.filename.get().strip()
        if not target:
            self.command.set(f"chmod {self.octal.get()} <filename>")
        elif re.search(r"[\n\r]", target):
            self.command.set("Invalid file path")
        else:
            # Quote the path safely for a POSIX shell.
            quoted = "'" + target.replace("'", "'\\''") + "'"
            self.command.set(f"chmod {self.octal.get()} {quoted}")

    def copy_command(self):
        command = self.command.get()
        if command == "Invalid file path":
            messagebox.showerror("Invalid path", "Please enter a valid single-line file path.")
            return
        self.clipboard_clear()
        self.clipboard_append(command)
        messagebox.showinfo("Copied", "chmod command copied to clipboard.")

    def reset(self):
        defaults = ((True, True, False), (True, False, False), (False, False, False))
        for role, values in zip(ROLES, defaults):
            for perm, value in zip(PERMISSIONS, values):
                self.vars[role][perm].set(value)
        self.filename.set("myfile.txt")
        self.update_preview()

if __name__ == "__main__":
    app = PermissionManager()
    app.mainloop()
