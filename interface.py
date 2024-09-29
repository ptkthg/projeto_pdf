import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from ttkthemes import ThemedTk
import backend  # Importa o back-end com as funcionalidades do PDF

def iniciar_interface():
    root = ThemedTk(theme="arc")
    root.title("Ferramenta de Manipulação de PDFs")
    root.geometry("600x400")

    style = ttk.Style()
    style.configure("TButton", padding=6, relief="flat", font=('Helvetica', 12))

    tk.Button(root, text="Abrir PDF no App Padrão", command=backend.abrir_pdf_no_app_padrao_gui).pack(pady=10)
    tk.Button(root, text="Compactar PDF", command=backend.compactar_pdf_gui).pack(pady=10)
    tk.Button(root, text="Proteger PDF com Senha", command=backend.proteger_pdf_gui).pack(pady=10)
    tk.Button(root, text="Combinar PDFs", command=backend.combinar_pdfs_gui).pack(pady=10)
    tk.Button(root, text="Dividir PDF", command=backend.dividir_pdf_gui).pack(pady=10)
    tk.Button(root, text="Rotacionar PDF", command=backend.rotacionar_pdf_gui).pack(pady=10)
    tk.Button(root, text="Exportar PDF para Imagens", command=backend.exportar_para_imagem_gui).pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    iniciar_interface()
