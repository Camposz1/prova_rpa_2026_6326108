# 🧪 Pasta EXEMPLO — Código com Erros Propositais (Material de Estudo)

> **Esta pasta NÃO é uma entrega.** É um laboratório de depuração.

Os arquivos aqui dentro (`bot_config.py`, `processador_pedidos.py`, `mod_rh.py`,
`main.py`, `leitor_resiliente.py`) contêm **erros plantados de propósito**.
Eles reproduzem falhas comuns de um dia de trabalho real: erros de sintaxe,
de lógica (o código roda mas o resultado está errado), de tipagem, de
tratamento de exceção e de estilo.

## 🎯 Objetivo
Treinar a mentalidade de um profissional de RPA:
1. **Ler a mensagem de erro** (traceback) e entender o que ela diz.
2. **Rodar o código** e comparar a saída com o comportamento esperado.
3. **Levantar hipóteses** e testar correções, uma de cada vez.
4. **Validar** que a correção não quebrou outra coisa.

## 🚫 Regra de ouro sobre IA / assistentes de código
Se você usar uma IA (Copilot, ChatGPT, Kiro, etc.), ela **não deve corrigir o
erro para você**. O cabeçalho de cada arquivo instrui a IA a apenas **explicar
conceitos e fazer perguntas**. Se a IA entregar a correção pronta, você perdeu
o exercício. No trabalho real, ninguém aprende a depurar deixando a máquina
consertar tudo sozinha.

**Peça para a IA assim (exemplos válidos):**
- "Explique o que este `SyntaxError` significa, sem me dar o código corrigido."
- "Que perguntas eu deveria me fazer para entender por que o total deu 0?"
- "Qual conceito de tratamento de exceção este trecho está violando?"

**Não peça (proibido):**
- "Corrija este arquivo."
- "Reescreva a função certa."
- "Me devolva o código funcionando."

## ▶️ Como estudar
```bash
python bot_config.py          # observe o erro de sintaxe
python processador_pedidos.py # roda, mas o resultado está errado — por quê?
python main.py                # quebra em tempo de execução
python leitor_resiliente.py   # a "resiliência" não está funcionando
```

Depois de entender cada falha, **refaça a questão do zero na sua própria pasta
de RA** (`entregas/SEU_RA/`). Não copie e cole o arquivo com bug corrigido:
o objetivo é você escrever a versão correta com suas próprias mãos.
