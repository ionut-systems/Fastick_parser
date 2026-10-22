import os
import subprocess
import time
import tkinter as tk
from tkinter import messagebox, scrolledtext
import matplotlib.pyplot as plt
import pandas as pd

EXECUTABLE = "./fast_parser.exe"
DATA_FILE = "simulation_ticks.csv"

def arret_securise(event=None):
    """Ferme proprement l'application et libère les ressources."""
    try:
        plt.close('all')
    except Exception:
        pass
    root.destroy()

class FastickApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Fastick - Moteur C++ & Analytics UI")
        self.root.geometry("650x500")
        self.root.configure(bg="#1e1e1e")

        # Titre de l'application
        title_label = tk.Label(root, text="FASTICK - HIGH PERFORMANCE TICK PARSER", font=("Arial", 12, "bold"), bg="#1e1e1e", fg="#00ffcc")
        title_label.pack(pady=10)

        # Cadre pour les boutons
        btn_frame = tk.Frame(root, bg="#1e1e1e")
        btn_frame.pack(pady=5)

        self.run_btn = tk.Button(btn_frame, text="🚀 Exécuter le Moteur C++", command=self.run_parser_gui, bg="#007acc", fg="white", font=("Arial", 10, "bold"), padx=10, relief="flat")
        self.run_btn.pack(side=tk.LEFT, padx=5)

        self.plot_btn = tk.Button(btn_frame, text="📊 Afficher le Graphique", command=self.analyze_and_plot_gui, bg="#28a745", fg="white", font=("Arial", 10, "bold"), padx=10, relief="flat")
        self.plot_btn.pack(side=tk.LEFT, padx=5)

        # Zone de logs / rapport intégrée dans l'interface
        self.log_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=75, height=20, font=("Consolas", 10), bg="#252526", fg="#d4d4d4", insertbackground="white")
        self.log_area.pack(pady=15, padx=15)
        self.log_area.insert(tk.END, "[*] Interface Tkinter prête. En attente d'action...\n")

    def run_parser_gui(self):
        """Exécute le parseur C++ et affiche le résultat dans la zone de texte."""
        if not os.path.exists(EXECUTABLE):
            messagebox.showerror("Erreur", f"L'exécutable {EXECUTABLE} est introuvable !")
            return

        self.log_area.insert(tk.END, "\n[*] Lancement du moteur C++ Fastick...\n")
        self.root.update()

        start_time = time.time()
        result = subprocess.run([EXECUTABLE, DATA_FILE], capture_output=True, text=True)
        elapsed = (time.time() - start_time) * 1000

        if result.returncode != 0:
            self.log_area.insert(tk.END, f"[ERREUR] Le parseur a échoué :\n{result.stderr}\n")
        else:
            self.log_area.insert(tk.END, result.stdout)
            self.log_area.insert(tk.END, f"[SUCCÈS] Exécution globale en {elapsed:.2f} ms\n[SYSTÈME] Appuyez sur [Entrée] pour quitter en toute sécurité.\n")

    def analyze_and_plot_gui(self):
        """Charge les données via Pandas et ouvre le graphique Matplotlib."""
        if not os.path.exists(DATA_FILE):
            messagebox.showwarning("Attention", f"Fichier de données {DATA_FILE} introuvable.")
            return
        try:
            df = pd.read_csv(DATA_FILE)
            plt.figure("Fastick Analytics", figsize=(8, 5))
            plt.plot(df.index, df.iloc[:, 0], label="Ticks", color="#00ffcc")
            plt.title("Analyse des Ticks - Fastick")
            plt.xlabel("Index")
            plt.ylabel("Valeur")
            plt.legend()
            plt.grid(True, linestyle="--", alpha=0.6)
            plt.show()
        except Exception as e:
            messagebox.showerror("Erreur Graphique", f"Impossible d'afficher le graphique :\n{e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = FastickApp(root)
    root.bind('<Return>', arret_securise)
    root.mainloop()