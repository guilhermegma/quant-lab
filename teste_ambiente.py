import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

# 1. Criar dados artificiais (Simulando o Estágio 1 do seu projeto)
t = np.linspace(0, 10, 100)
# Criando uma sigmoide simples com ruído
y = 1 / (1 + np.exp(-(t - 5))) + np.random.normal(0, 0.05, 100)

# 2. Definir a função para o SciPy ajustar
def sigmoid(t, A, b, m):
    return A / (1 + np.exp(-b * (t - m)))

# 3. Executar o ajuste (O motor do seu Estágio 2)
# p0 é o "chute inicial" para A, b, m
popt, _ = curve_fit(sigmoid, t, y, p0=[1, 1, 5])

print(f"Ambiente OK! Parâmetros ajustados: A={popt[0]:.2f}, b={popt[1]:.2f}, m={popt[2]:.2f}")

# 4. Visualizar (Para o seu portfólio no GitHub)
plt.scatter(t, y, label='Dados com Ruído', alpha=0.5)
plt.plot(t, sigmoid(t, *popt), color='red', label='Curva Ajustada')
plt.title('Teste de Ambiente - Ajuste de Curva Sigmóide')
plt.legend()
plt.show()
EOF