import yfinance as yf
import matplotlib.pyplot as plt
import numpy as np

msft = yf.Ticker("MSFT")
income_statement = msft.financials.to_dict()
interesting_stats = ['Total Revenue', 'Operating Income', 'Net Income', 'Diluted EPS', 'EBIT', 'EBITDA']
 
fig, ax = plt.subplots(figsize=plt.figaspect(0.5))
cmap = plt.get_cmap('Dark2')
colors = [cmap(i) for i in np.linspace(0, 1, len(interesting_stats))]
for i, stat in enumerate(interesting_stats):
    values = [income_statement[date].get(stat, None) for date in income_statement]
    ax.plot(list(income_statement.keys()), values, label=stat, color=colors[i])
ax.set_xticks(list(income_statement.keys()))
fig.suptitle('Income Statement Trends', fontsize=16)
ax.set_title('(Four Years)')
ax.set_xlabel('Date')
ax.set_ylabel('Value (in Hundred Billions)')
ax.legend(loc='upper left')
plt.tight_layout()
plt.show()