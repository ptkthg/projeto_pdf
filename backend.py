import PyPDF2
import fitz  # PyMuPDF
from tkinter import filedialog, messagebox
import os
import platform
import subprocess

# Função para abrir o PDF no aplicativo padrão do sistema
def abrir_pdf_no_app_padrao(pdf_path):
    try:
        sistema = platform.system()  # Detecta o sistema operacional
        if sistema == "Windows":
            os.startfile(pdf_path)  # Windows: Abre o PDF no aplicativo padrão
        elif sistema == "Darwin":  # MacOS
            subprocess.run(["open", pdf_path])
        elif sistema == "Linux":
            subprocess.run(["xdg-open", pdf_path])
        else:
            messagebox.showerror("Erro", "Sistema operacional não suportado para abrir PDFs automaticamente.")
    except Exception as e:
        messagebox.showerror("Erro", f"Não foi possível abrir o PDF: {e}")

# Função para abrir o PDF através da interface gráfica
def abrir_pdf_no_app_padrao_gui():
    pdf_path = filedialog.askopenfilename(title="Selecione o PDF", filetypes=[("PDF files", "*.pdf")])
    if pdf_path:
        abrir_pdf_no_app_padrao(pdf_path)

# Função para compactar PDF
def compactar_pdf(pdf_path, output_path):
    try:
        doc = fitz.open(pdf_path)
        doc.save(output_path, garbage=4, deflate=True)  # Garbage collection para otimização
        messagebox.showinfo("Sucesso", f"PDF compactado com sucesso! Salvo em {output_path}")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao compactar o PDF: {e}")

# Função GUI para compactar PDF
def compactar_pdf_gui():
    pdf_path = filedialog.askopenfilename(title="Selecione o PDF", filetypes=[("PDF files", "*.pdf")])
    if not pdf_path:
        return  # O usuário cancelou a seleção do arquivo
    output_path = filedialog.asksaveasfilename(defaultextension=".pdf", title="Salvar PDF Compactado", filetypes=[("PDF files", "*.pdf")])
    if not output_path:
        return  # O usuário cancelou a seleção do local de salvamento
    compactar_pdf(pdf_path, output_path)

# Função para proteger o PDF com senha
def proteger_pdf_com_senha(pdf_path, senha, output_path):
    try:
        pdf_reader = PyPDF2.PdfReader(open(pdf_path, 'rb'))
        pdf_writer = PyPDF2.PdfWriter()

        for page in pdf_reader.pages:
            pdf_writer.add_page(page)

        pdf_writer.encrypt(senha)

        with open(output_path, 'wb') as output_file:
            pdf_writer.write(output_file)

        messagebox.showinfo("Sucesso", "PDF protegido com senha!")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao proteger o PDF: {e}")

# Função GUI para proteger o PDF com senha
def proteger_pdf_gui():
    pdf_path = filedialog.askopenfilename(title="Selecione o PDF", filetypes=[("PDF files", "*.pdf")])
    if not pdf_path:
        return  # O usuário cancelou a seleção do arquivo

    senha = filedialog.askstring("Senha", "Digite a senha para proteger o PDF:")
    if not senha:
        return  # O usuário cancelou a inserção da senha

    output_path = filedialog.asksaveasfilename(defaultextension=".pdf", title="Salvar PDF Protegido", filetypes=[("PDF files", "*.pdf")])
    if not output_path:
        return  # O usuário cancelou a seleção do local de salvamento

    proteger_pdf_com_senha(pdf_path, senha, output_path)

# Função para combinar PDFs
def combinar_pdfs(pdf_paths, output_path):
    try:
        pdf_writer = PyPDF2.PdfWriter()
        for pdf_path in pdf_paths:
            pdf_reader = PyPDF2.PdfReader(open(pdf_path, 'rb'))
            for page in pdf_reader.pages:
                pdf_writer.add_page(page)

        with open(output_path, 'wb') as output_file:
            pdf_writer.write(output_file)
        messagebox.showinfo("Sucesso", f"PDFs combinados com sucesso! O arquivo foi salvo em {output_path}")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao combinar os PDFs: {e}")

# Função GUI para combinar PDFs
def combinar_pdfs_gui():
    pdf_paths = filedialog.askopenfilenames(title="Selecione os PDFs", filetypes=[("PDF files", "*.pdf")])
    if not pdf_paths:
        return  # O usuário cancelou a seleção
    output_path = filedialog.asksaveasfilename(defaultextension=".pdf", title="Salvar PDF combinado", filetypes=[("PDF files", "*.pdf")])
    if not output_path:
        return  # O usuário cancelou a seleção do local de salvamento
    combinar_pdfs(pdf_paths, output_path)

# Função para dividir PDF
def dividir_pdf(pdf_path, inicio, fim, output_path):
    try:
        pdf_reader = PyPDF2.PdfReader(open(pdf_path, 'rb'))
        pdf_writer = PyPDF2.PdfWriter()

        num_paginas = len(pdf_reader.pages)
        if inicio < 1 or fim > num_paginas:
            messagebox.showwarning("Aviso", "O intervalo de páginas está fora do limite do PDF.")
            return

        for i in range(inicio - 1, fim):
            pdf_writer.add_page(pdf_reader.pages[i])

        with open(output_path, 'wb') as output_file:
            pdf_writer.write(output_file)

        messagebox.showinfo("Sucesso", "PDF dividido com sucesso!")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao dividir o PDF: {e}")

# Função GUI para dividir PDF
def dividir_pdf_gui():
    pdf_path = filedialog.askopenfilename(title="Selecione o PDF", filetypes=[("PDF files", "*.pdf")])
    if not pdf_path:
        return

    try:
        inicio = int(input("Página de início: "))
        fim = int(input("Página de fim: "))
        output_path = filedialog.asksaveasfilename(defaultextension=".pdf", title="Salvar PDF dividido", filetypes=[("PDF files", "*.pdf")])
        if not output_path:
            return
        dividir_pdf(pdf_path, inicio, fim, output_path)
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores numéricos válidos para as páginas.")

# Função para rotacionar PDF
def rotacionar_pdf(pdf_path, output_path, angulo=90):
    try:
        pdf_reader = PyPDF2.PdfReader(open(pdf_path, 'rb'))
        pdf_writer = PyPDF2.PdfWriter()

        for page in pdf_reader.pages:
            page.rotate_clockwise(angulo)
            pdf_writer.add_page(page)

        with open(output_path, 'wb') as output_file:
            pdf_writer.write(output_file)

        messagebox.showinfo("Sucesso", f"PDF rotacionado em {angulo} graus!")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao rotacionar o PDF: {e}")

# Função GUI para rotacionar PDF
def rotacionar_pdf_gui():
    pdf_path = filedialog.askopenfilename(title="Selecione o PDF", filetypes=[("PDF files", "*.pdf")])
    angulo = int(input("Ângulo de rotação (90, 180, 270): "))
    output_path = filedialog.asksaveasfilename(defaultextension=".pdf", title="Salvar PDF rotacionado", filetypes=[("PDF files", "*.pdf")])
    rotacionar_pdf(pdf_path, output_path, angulo)

# Função para exportar PDF para imagens
def exportar_para_imagem(pdf_path, output_dir):
    try:
        doc = fitz.open(pdf_path)
        for page_num in range(len(doc)):
            page = doc.load_page(page_num)
            pix = page.get_pixmap()
            output_image = f"{output_dir}/pagina_{page_num + 1}.png"
            pix.save(output_image)

        messagebox.showinfo("Sucesso", f"Páginas exportadas como imagens no diretório {output_dir}")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao exportar PDF para imagens: {e}")

# Função GUI para exportar PDF para imagens
def exportar_para_imagem_gui():
    pdf_path = filedialog.askopenfilename(title="Selecione o PDF", filetypes=[("PDF files", "*.pdf")])
    output_dir = filedialog.askdirectory(title="Selecione o diretório de saída")
    exportar_para_imagem(pdf_path, output_dir)
