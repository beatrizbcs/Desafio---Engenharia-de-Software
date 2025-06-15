from typing import Protocol, List
from .tarefa import Tarefa

class TarefaRepository(Protocol):
    def salvar(self, tarefa: Tarefa) -> None: ...
    def buscar_por_titulo(self, titulo: str) -> Tarefa | None: ...
    def listar(self) -> List[Tarefa]: ...

class InMemoryTarefaRepo:
    def __init__(self) -> None:
        self._tarefas: List[Tarefa] = []

    def salvar(self, tarefa: Tarefa) -> None:
        self._tarefas.append(tarefa)

    def buscar_por_titulo(self, titulo: str) -> Tarefa | None:
        return next((t for t in self._tarefas if t.titulo == titulo), None)

    def listar(self) -> List[Tarefa]:
        return list(self._tarefas)