import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker

# Dados de fluxo de caixa
dados = {
    'mes': ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun'],
    'entradas': [15000, 16200, 14800, 17500, 16900, 18200],
    'saidas':   [12000, 13100, 11900, 14200, 13800, 14500]
}

df = pd.DataFrame(dados)
df['saldo'] = df['entradas'] - df['saidas']

# Grafico
fig, ax = plt.subplots(figsize=(11, 6))
fig.patch.set_facecolor('#1e1e2e')
ax.set_facecolor('#1e1e2e')

x = range(len(df['mes']))
largura = 0.35

barras_entrada = ax.bar([i - largura/2 for i in x], df['entradas'],
                        width=largura, label='Entradas', color='#2ecc71', alpha=0.9)
barras_saida = ax.bar([i + largura/2 for i in x], df['saidas'],
                      width=largura, label='Saidas', color='#e74c3c', alpha=0.9)
ax.plot(x, df['saldo'], marker='o', color='#f1c40f',
        label='Saldo', linewidth=2.5, markersize=8)

ax.set_xticks(list(x))
ax.set_xticklabels(df['mes'], color='white', fontsize=11)
ax.tick_params(colors='white')
ax.yaxis.set_major_formatter(mticker.FuncFormatter(
    lambda val, _: f'R$ {val:,.0f}'.replace(',', '.')))
ax.set_title('Dashboard de Fluxo de Caixa Mensal', color='white',
             fontsize=14, fontweight='bold', pad=15)
ax.set_xlabel('Mes', color='white', fontsize=11)
ax.set_ylabel('Valor (R$)', color='white', fontsize=11)
ax.legend(facecolor='#2e2e3e', labelcolor='white', fontsize=10)
ax.spines['bottom'].set_color('#444')
ax.spines['left'].set_color('#444')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.yaxis.label.set_color('white')

for barra in barras_entrada:
    ax.text(barra.get_x() + barra.get_width()/2,
            barra.get_height() + 200,
            f'R${barra.get_height():,.0f}'.replace(',', '.'),
            ha='center', va='bottom', color='white', fontsize=8)

for barra in barras_saida:
    ax.text(barra.get_x() + barra.get_width()/2,
            barra.get_height() + 200,
            f'R${barra.get_height():,.0f}'.replace(',', '.'),
            ha='center', va='bottom', color='white', fontsize=8)

plt.tight_layout()
plt.savefig('fluxo_de_caixa.png', dpi=150, bbox_inches='tight',
            facecolor=fig.get_facecolor())
plt.show()
print('Dashboard gerado com sucesso!')