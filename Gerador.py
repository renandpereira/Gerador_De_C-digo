import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd
from barcode import Code128
from barcode.writer import ImageWriter
import os
import sys
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

class BarcodeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gerador de Código de Barras")
        self.root.geometry("400x200")

        # Botão para importar planilha
        self.import_button = tk.Button(root, text="Importar Planilha", command=self.import_planilha)
        self.import_button.pack(pady=20)

        # Botão para gerar códigos de barras
        self.generate_barcodes_button = tk.Button(root, text="Gerar Códigos de Barras", command=self.generate_barcodes, state="disabled")
        self.generate_barcodes_button.pack(pady=20)

        # Botão para gerar PDF
        self.generate_pdf_button = tk.Button(root, text="Gerar PDF", command=self.generate_pdf, state="disabled")
        self.generate_pdf_button.pack(pady=20)

        self.filepath = None
        self.data = None

        # Define o caminho da pasta de imagens
        if getattr(sys, 'frozen', False):  # Executando como .exe
            base_dir = sys._MEIPASS  # Usado pelo PyInstaller para apontar a pasta temporária
        else:  # Executando como script Python
            base_dir = os.path.dirname(os.path.abspath(__file__))

        self.image_dir = os.path.join(base_dir, "Imagens_Barcode")

        # Cria a pasta de imagens se não existir
        if not os.path.exists(self.image_dir):
            os.makedirs(self.image_dir)

    def import_planilha(self):
        # Seleciona o arquivo Excel
        self.filepath = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx *.xls")])
        if self.filepath:
            try:
                self.data = pd.read_excel(self.filepath, dtype={'Código': str})
                self.data['Código'] = self.data['Código'].str.strip()

                if 'Código' not in self.data.columns:
                    messagebox.showerror("Erro", "A planilha precisa de uma coluna chamada 'Código'")
                    return

                messagebox.showinfo("Sucesso", "Planilha carregada com sucesso!")
                self.generate_barcodes_button.config(state="normal")
            except Exception as e:
                messagebox.showerror("Erro", f"Erro ao ler a planilha: {e}")

    def generate_barcodes(self):
        if self.data is None:
            messagebox.showerror("Erro", "Nenhuma planilha carregada.")
            return

        for idx, row in self.data.iterrows():
            codigo = str(row['Código'])
            try:
                # Define o caminho completo para o arquivo do código de barras
                barcode_path = os.path.join(self.image_dir, f"{codigo}")
                barcode = Code128(codigo, writer=ImageWriter())
                barcode.writer.set_options({
                    'module_height': 10,
                    'module_width': 0.3,
                    'quiet_zone': 6,
                })
                # Verifica se o diretório de imagens existe e cria, se necessário
                if not os.path.exists(self.image_dir):
                    os.makedirs(self.image_dir)
                barcode.save(barcode_path)
            except Exception as e:
                messagebox.showerror("Erro", f"Não foi possível criar o código de barras para {codigo}\nDetalhes do erro: {e}")

        messagebox.showinfo("Sucesso", "Códigos de barras gerados com sucesso!")
        self.generate_pdf_button.config(state="normal")

    def generate_pdf(self):
        if self.data is None:
            messagebox.showerror("Erro", "Nenhuma planilha carregada.")
            return

        # Abre um diálogo para escolher o local e o nome do arquivo PDF
        pdf_path = filedialog.asksaveasfilename(
            defaultextension=".pdf",
            filetypes=[("PDF files", "*.pdf")],
            title="Salvar PDF como"
        )
        if not pdf_path:
            return  # Se o usuário cancelar, sair da função

        c = canvas.Canvas(pdf_path, pagesize=letter)
        largura, altura = letter
        margem = 20
        espaco_entre_imagens = 5
        max_por_coluna = 11
        max_por_linha = 4
        largura_imagem = 130
        altura_imagem = 60

        x = margem
        y = altura - margem - altura_imagem

        for idx, row in self.data.iterrows():
            codigo = str(row['Código'])
            caminho_imagem = os.path.join(self.image_dir, f"{codigo}.png")

            if os.path.exists(caminho_imagem):
                try:
                    c.drawImage(caminho_imagem, x, y, width=largura_imagem, height=altura_imagem)
                except Exception as e:
                    print(f"Erro ao inserir imagem {codigo}: {e}")
            else:
                print(f"Imagem não encontrada para o código: {codigo}")

            x += largura_imagem + espaco_entre_imagens
            if (idx + 1) % max_por_linha == 0:
                x = margem
                y -= altura_imagem + espaco_entre_imagens

            if (idx + 1) % (max_por_linha * max_por_coluna) == 0:
                c.showPage()
                x = margem
                y = altura - margem - altura_imagem

        try:
            c.save()
            messagebox.showinfo("Sucesso", f"PDF gerado com sucesso em: {pdf_path}")
        except Exception as e:
            print(f"Erro ao gerar PDF: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = BarcodeApp(root)
    root.mainloop()

