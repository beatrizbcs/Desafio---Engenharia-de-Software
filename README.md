Gerenciador de Projetos em Python 🛠️📚
📌 Visão Geral
Este projeto refatora um código legado para torná-lo modular, testável e aderente aos princípios SOLID, garantindo 100% de cobertura de testes e modelagem UML.

As principais entidades são: Projeto, Tarefa, TarefaUrgente, Membro, TarefaRepository e RelatorioGerador.

✨ Principais Características
SRP: Cada classe tem uma única responsabilidade, garantindo modularidade.

OCP / LSP: Extensões como TarefaUrgente sem necessidade de modificar código-base.

ISP: Relatório segregado via RelatorioGerador, permitindo diferentes implementações.

DIP: Projeto recebe qualquer TarefaRepository ou RelatorioGerador via injeção de dependência.

Testes automatizados: pytest com 100% de cobertura.

Tratamento de erros: Exceção customizada TarefaNaoEncontrada para melhor diagnóstico.

Diagrama UML: Gerado via pyreverse e disponível em uml/diagrama.png.

🗂️ Estrutura do Projeto
src/
 ├─ __init__.py
 ├─ projeto.py              # Orquestra membros e tarefas
 ├─ tarefa.py               # Tarefa + TarefaUrgente
 ├─ membro.py               # Representação de membros do projeto
 ├─ repository.py           # Interface + implementação do repositório
 ├─ relatorio.py            # Interface ISP para geração de relatórios
 ├─ exceptions.py           # Exceções customizadas
tests/
 ├─ test_projeto.py         # Testes para a classe Projeto
 ├─ test_dip_ocp.py         # Testes para dependência inversa e subtipos
uml/
 ├─ diagrama.png            # Diagrama UML gerado via pyreverse
requirements.txt
README.md
🚀 Instalação e Configuração
1️⃣ Clonar o Repositório
bash
git clone https://github.com/<seu-usuario>/gerenciador-projetos.git
cd gerenciador-projetos
2️⃣ Criar e Ativar o Ambiente Virtual
bash
python -m venv .venv

# Windows
.venv\Scripts\Activate.ps1  

# Linux / macOS
source .venv/bin/activate  
3️⃣ Instalar Dependências
bash
pip install -r requirements.txt  
✅ Executar Testes e Verificar Cobertura
bash
pytest -q            # Executa todos os testes
python -m coverage run -m pytest
python -m coverage report -m
python -m coverage html && start htmlcov/index.html  # Gera e abre o relatório gráfico
📢 Cobertura esperada: 100% ✅

🖼️ Gerar/Regerar o Diagrama UML
bash
# Usando pyreverse (incluído no pylint)
pyreverse -o png -p projeto src  
📢 O diagrama será gerado em: uml/diagrama.png ✅

> Alternativamente, utilize draw.io ou PlantUML para criar a estrutura visual.

🧩 Exemplo de Uso no REPL
python
>>> from src import Projeto, Membro, Tarefa
>>> from datetime import date

>>> p = Projeto("App", date(2025, 12, 1), "Demo DIP")
>>> dev = Membro("Leo", "Dev")

>>> p.adicionar_membro(dev)
>>> p.adicionar_tarefa(Tarefa("API", "Criar endpoints", dev))

>>> print(p.gerar_relatorio())

Projeto: App
Prazo: 01/12/2025
Descrição: Demo DIP
Membros:
 - Leo (Dev)
Tarefas:
 - API [pendente] - Resp.: Leo