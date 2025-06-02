import os
import sys
import json
import csv
import customtkinter as ctk
# Importa os diálogos da biblioteca padrão tkinter para garantir compatibilidade
from tkinter import messagebox, filedialog 
from openai import OpenAI
from dotenv import load_dotenv

# Carrega variáveis de ambiente do arquivo .env
load_dotenv()

# --- LÓGICA DE ANÁLISE (BACK-END) - INALTERADA ---
def analisar_phishing(assunto, corpo, client):
    """
    Analisa um e-mail para detectar phishing usando a API da OpenAI,
    retornando uma classificação e uma justificativa.
    """
    prompt = f"""
    Analise o seguinte e-mail para determinar se é uma tentativa de phishing.
    Assunto: {assunto}
    Corpo: {corpo}

    Responda em formato JSON com duas chaves:
    1. "classificacao": pode ser "phishing" ou "nao_phishing".
    2. "justificativa": explique em 2 ou 3 frases os motivos da sua classificação, 
       apontando elementos suspeitos como urgência, links estranhos, erros gramaticais, etc.
    """
    try:
        response = client.chat.completions.create(
            model="gpt-4.1-nano",
            messages=[
                {"role": "system", "content": "Você é um especialista em segurança cibernética. Sua tarefa é analisar e-mails e fornecer uma classificação de phishing com uma justificativa clara e concisa em formato JSON."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.2,
            max_tokens=200,
            response_format={"type": "json_object"}
        )
        resultado_json_str = response.choices[0].message.content
        resultado = json.loads(resultado_json_str)
        return resultado
    except Exception as e:
        return {"classificacao": "erro", "justificativa": f"Erro ao chamar a API da OpenAI: {e}"}

# --- INTERFACE GRÁFICA (FRONT-END) COM CUSTOMTKINTER ---

class PhishingAnalyzerApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        # --- Configuração da Janela e Tema ---
        self.title("Analisador de Phishing com IA")
        self.geometry("900x700")
        
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        # Configura o layout da grid para ser responsivo
        self.grid_columnconfigure(0, weight=1) 
        self.grid_rowconfigure(2, weight=1)

        # --- Inicialização do Cliente OpenAI ---
        try:
            self.api_key = os.getenv("OPENAI_API_KEY")
            if not self.api_key:
                # CORREÇÃO: Usando o messagebox padrão do tkinter
                messagebox.showerror("Erro de Configuração", "A chave da API (OPENAI_API_KEY) não foi encontrada no .env.")
                self.quit()
                return
            self.client = OpenAI(api_key=self.api_key)
        except Exception as e:
            messagebox.showerror("Erro de Inicialização", f"Não foi possível iniciar o cliente OpenAI: {e}")
            self.quit()
            return

        # --- Widgets da Interface ---
        self.app_font = ctk.CTkFont(family="Segoe UI", size=14)
        self.title_font = ctk.CTkFont(family="Segoe UI", size=18, weight="bold")

        top_frame = ctk.CTkFrame(self, corner_radius=10)
        top_frame.grid(row=0, column=0, padx=20, pady=(20, 10), sticky="ew")
        top_frame.grid_columnconfigure(0, weight=1)
        top_frame.grid_columnconfigure(1, weight=1)

        single_frame = ctk.CTkFrame(top_frame, corner_radius=10)
        single_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        single_frame.grid_columnconfigure(0, weight=1)

        ctk.CTkLabel(single_frame, text="Análise de E-mail Único", font=self.title_font).grid(row=0, column=0, padx=15, pady=10, sticky="w")
        
        self.assunto_entry = ctk.CTkEntry(single_frame, placeholder_text="Assunto do e-mail", font=self.app_font, height=35)
        self.assunto_entry.grid(row=1, column=0, padx=15, pady=(5, 10), sticky="ew")

        self.corpo_text = ctk.CTkTextbox(single_frame, wrap="word", font=self.app_font, height=150)
        self.corpo_text.grid(row=2, column=0, padx=15, pady=5, sticky="nsew")

        analyze_button = ctk.CTkButton(single_frame, text="Analisar E-mail", font=self.app_font, height=35, command=self.analisar_email_unico)
        analyze_button.grid(row=3, column=0, padx=15, pady=15, sticky="e")

        batch_frame = ctk.CTkFrame(top_frame, corner_radius=10)
        batch_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
        batch_frame.grid_columnconfigure(0, weight=1)
        batch_frame.grid_rowconfigure(1, weight=1)

        ctk.CTkLabel(batch_frame, text="Análise em Lote (.csv)", font=self.title_font).grid(row=0, column=0, padx=15, pady=10, sticky="w")
        
        batch_button = ctk.CTkButton(batch_frame, text="Selecionar Arquivo e Analisar", font=self.app_font, height=35, command=self.analisar_em_lote)
        batch_button.grid(row=1, column=0, padx=15, pady=60)

        results_frame = ctk.CTkFrame(self, corner_radius=10)
        results_frame.grid(row=2, column=0, padx=20, pady=(10, 20), sticky="nsew")
        results_frame.grid_rowconfigure(0, weight=1)
        results_frame.grid_columnconfigure(0, weight=1)

        self.results_text = ctk.CTkTextbox(results_frame, wrap="word", font=self.app_font, state='disabled', corner_radius=10)
        self.results_text.grid(row=0, column=0, padx=15, pady=15, sticky="nsew")

    def mostrar_resultado(self, texto):
        self.results_text.configure(state='normal')
        self.results_text.insert("end", texto + "\n\n")
        self.results_text.configure(state='disabled')
        self.results_text.see("end")

    def analisar_email_unico(self):
        assunto = self.assunto_entry.get()
        corpo = self.corpo_text.get("1.0", "end-1c")

        if not assunto.strip() or not corpo.strip():
            # CORREÇÃO: Usando o messagebox padrão do tkinter
            messagebox.showwarning("Entrada Inválida", "Por favor, preencha o assunto e o corpo do e-mail.")
            return

        resultado = analisar_phishing(assunto, corpo, self.client)
        
        self.results_text.configure(state='normal')
        self.results_text.delete('1.0', "end")
        
        resultado_formatado = f"--- Análise Individual ---\n"
        resultado_formatado += f"Classificação: {resultado.get('classificacao', 'N/A').upper()}\n"
        resultado_formatado += f"Justificativa: {resultado.get('justificativa', 'N/A')}"
        
        self.mostrar_resultado(resultado_formatado)

    def analisar_em_lote(self):
        # CORREÇÃO: Usando o filedialog padrão do tkinter
        filepath = filedialog.askopenfilename(
            title="Selecione um arquivo CSV",
            filetypes=(("Arquivos CSV", "*.csv"), ("Todos os arquivos", "*.*"))
        )
        if not filepath: return

        try:
            with open(filepath, mode='r', encoding='utf-8', newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                if 'assunto' not in reader.fieldnames or 'corpo' not in reader.fieldnames:
                    messagebox.showerror("Erro de Formato", "O arquivo CSV deve conter as colunas 'assunto' e 'corpo'.")
                    return
                
                self.results_text.configure(state='normal')
                self.results_text.delete('1.0', "end")
                self.mostrar_resultado(f"--- Iniciando Análise em Lote do arquivo: {os.path.basename(filepath)} ---")
                
                for i, row in enumerate(reader):
                    assunto = row['assunto']
                    corpo = row['corpo']
                    resultado = analisar_phishing(assunto, corpo, self.client)
                    
                    resultado_formatado = f"E-mail #{i+1} | Classificação: {resultado.get('classificacao', 'N/A').upper()}\n"
                    resultado_formatado += f"Assunto: {assunto}\n"
                    resultado_formatado += f"Justificativa: {resultado.get('justificativa', 'N/A')}\n"
                    resultado_formatado += "-"*30
                    
                    self.mostrar_resultado(resultado_formatado)
                    self.update_idletasks()
        except Exception as e:
            messagebox.showerror("Erro de Processamento", f"Ocorreu um erro ao ler o arquivo: {e}")

if __name__ == "__main__":
    app = PhishingAnalyzerApp()
    app.mainloop()