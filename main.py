import pandas as pd
from fpdf import FPDF


# 1.Simulação dos Dados

data = {
    'Produto': ['Notebook', 'Mouse', 'teclado', 'Monitor', 'Impressora'],
    'Quantidade': [10, 50, 30, 20, 15],
    'Preço_Unitário':[2500.00, 150.00, 200.00, 800.00, 450.00]
}
df = pd.DataFrame(data)

# 2.Processamento de Dados
df['Total_vendas'] = df['Quantidade'] * df['Preço_Unitário']
faturamento_total = df['Total_vendas'].sum()
produto_mais_vendido = df.groupby('Produto')['Quantidade'].sum().idxmax()

# 3. Gerar Relatório em PDF
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", 'B', 16)
pdf.cell(200, 10, txt="Relatório de Vendas Semanal", ln=True, align='C')

pdf.set_font("Arial", size=12)
pdf.ln(10) # Para pular linha
pdf.cell(200, 10, txt=f"Faturamento Total: R${faturamento_total:.2f}", ln=True)
pdf.cell(200, 10, txt=f"Produto com maior volume: {produto_mais_vendido}", ln=True)

# Listando os itens no PDF
pdf.ln(5)
pdf.cell(200, 10, txt="Detalhes por item: ", ln=True)
for index, row in df.iterrows():
    pdf.cell(200, 10, txt=f"- {row['Produto']}: {row['Quantidade']} unidades | Total: R${row['Total_vendas']:.2f}", ln=True)

pdf.output("Relatorio_Vendas.pdf")
print("Relatorio gerado com sucesso: Relatorio_Vendas.pdf")