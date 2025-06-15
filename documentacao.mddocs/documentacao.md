📄 Documentação do Projeto
📌 1. Objetivo do Projeto
Este projeto tem como objetivo refatorar e organizar um código legado, aplicando boas práticas de programação e os princípios SOLID para garantir modularidade, extensibilidade e facilidade de manutenção.

📌 2. Estrutura e Responsabilidades das Classes
🔹 Classe Projeto
✅ Responsabilidade: Gerenciar membros e tarefas dentro de um projeto. ✅ Métodos principais:

adicionar_tarefa(tarefa: Tarefa) -> None → Adiciona uma nova tarefa ao projeto.

adicionar_membro(membro: Membro) -> None → Adiciona um novo membro ao projeto.

concluir_tarefa(titulo: str) -> None → Marca uma tarefa como concluída.

gerar_relatorio() -> str → Retorna um relatório detalhado do projeto.

📌 Contratos (dependências):

Usa TarefaRepository para persistência.

Usa RelatorioGerador para geração de relatórios.

🔹 Classe Tarefa
✅ Responsabilidade: Representa uma tarefa dentro de um projeto. ✅ Métodos principais:

marcar_como_concluida() -> None → Define a tarefa como concluída.

definir_prazo(data: date) -> None → Estabelece um prazo para a tarefa.

📌 Herança:

TarefaUrgente herda de Tarefa, adicionando prioridade extra.

🔹 Classe Membro
✅ Responsabilidade: Representa um participante do projeto. ✅ Métodos principais:

atribuir_tarefa(tarefa: Tarefa) -> None → Liga o membro a uma tarefa.

📌 Relação:

Projeto contém vários Membro.

🔹 Interface TarefaRepository
✅ Responsabilidade: Define um contrato para a persistência de tarefas. ✅ Métodos esperados:

salvar_tarefa(tarefa: Tarefa) -> None → Salva uma tarefa.

buscar_por_titulo(titulo: str) -> Tarefa → Retorna uma tarefa pelo título.

📌 Implementação:

InMemoryTarefaRepo implementa TarefaRepository.

🔹 Interface RelatorioGerador
✅ Responsabilidade: Define um contrato para geração de relatórios. ✅ Métodos esperados:

gerar(projeto: Projeto) -> str → Retorna o relatório do projeto.

📌 Implementação:

TextoRelatorioGerador implementa RelatorioGerador.

📌 3. Tratamento de Erros
TarefaNaoEncontrada(Exception) → Exceção personalizada para tarefas inexistentes.

📌 4. Testes Automatizados e Cobertura
✅ Implementamos testes unitários com Pytest, cobrindo:

CRUD de Tarefas (test_projeto.py).

DIP e OCP aplicados (test_dip_ocp.py). ✅ Cobertura 100% garantida com pytest-cov.