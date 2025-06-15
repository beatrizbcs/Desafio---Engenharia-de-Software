from datetime import date
from src import Projeto, Membro, Tarefa, InMemoryTarefaRepo


def fabrica():
    repo = InMemoryTarefaRepo()
    p = Projeto("App", date(2025, 12, 1), "Demo DIP", repo)
    dev = Membro("Leo", "Dev")
    p.adicionar_membro(dev)
    p.adicionar_tarefa(Tarefa("Normal", "Doc", dev))
    return p


def test_gerar_relatorio_completo():
    projeto = fabrica()
    relatorio = projeto.gerar_relatorio()

    assert "Projeto: App" in relatorio
    assert "Membros:" in relatorio
    assert "Tarefas:" in relatorio