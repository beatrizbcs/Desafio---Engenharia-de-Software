from datetime import date
import pytest
from src import (
    Projeto,
    Membro,
    Tarefa,
    TarefaUrgente,
    TarefaNaoEncontrada,
    InMemoryTarefaRepo,
)

def fabrica():
    repo = InMemoryTarefaRepo()
    p = Projeto("App", date(2025, 12, 1), "Demo DIP", repo)
    dev = Membro("Leo", "Dev")
    p.adicionar_membro(dev)
    p.adicionar_tarefa(Tarefa("Normal", "Doc", dev))
    p.adicionar_tarefa(
        TarefaUrgente("Bug crítico", "Corrigir falha grave", dev, nivel=3)
    )
    return p, repo

def test_ocp_subclasse_funciona():
    projeto, _ = fabrica()
    urgentes = [t for t in projeto.listar_tarefas() if isinstance(t, TarefaUrgente)]
    assert len(urgentes) == 1 and urgentes[0].nivel == 3

def test_dip_repositorio_injetado():
    projeto, repo = fabrica()
    assert len(repo.listar()) == 2
    projeto.concluir_tarefa("Normal")
    tarefa = repo.buscar_por_titulo("Normal")
    assert tarefa and tarefa.status == Tarefa.CONCLUIDA

def test_excecao_ainda_funciona():
    projeto, _ = fabrica()
    with pytest.raises(TarefaNaoEncontrada):
        projeto.concluir_tarefa("Nada")

def test_repr_tarefa_urgente():
    urgente = TarefaUrgente(
        "Bug crítico", "Corrigir falha grave", Membro("Dev", "Engenheiro"), nivel=3
    )
    esperado = "<TarefaUrgente Bug crítico n3 [pendente]>"
    assert repr(urgente) == esperado  

def test_repr_tarefa():
    tarefa = Tarefa("Doc", "Escrever docs", Membro("Ana", "Tech Writer"))
    esperado = "<Tarefa Doc [pendente]>"
    assert repr(tarefa) == esperado 

def test_tarefa_inicia_com_status_pendente():
    tarefa = Tarefa("Teste", "Descrição", Membro("Bob", "Analista"))
    assert tarefa.status == Tarefa.PENDENTE