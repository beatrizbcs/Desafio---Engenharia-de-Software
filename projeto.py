from datetime import date
from typing import List

from .tarefa import Tarefa
from .membro import Membro
from .exceptions import TarefaNaoEncontrada
from .repository import TarefaRepository, InMemoryTarefaRepo
from .relatorio import RelatorioGerador, TextoRelatorioGerador


class Projeto:
    """
    Representa um projeto que possui membros e tarefas.

    Atributos:
        nome (str): Nome do projeto.
        prazo (date): Data limite.
        descricao (str): Breve descrição.
        _membros (List[Membro]): Participantes.
        _repo (TarefaRepository): Repositório de tarefas.
        _relatorio (RelatorioGerador): Estratégia para gerar relatórios.
    """

    def __init__(
        self,
        nome: str,
        prazo: date,
        descricao: str,
        repo: TarefaRepository | None = None,
        relatorio: RelatorioGerador | None = None,
    ):
        self.nome = nome
        self.prazo = prazo
        self.descricao = descricao
        self._membros: List[Membro] = []
        self._repo: TarefaRepository = repo or InMemoryTarefaRepo()
        # ISP → Projeto depende apenas do contrato RelatorioGerador
        self._relatorio: RelatorioGerador = relatorio or TextoRelatorioGerador()

    # ---------- operações -----------
    def adicionar_membro(self, membro: Membro) -> None:
        self._membros.append(membro)

    def adicionar_tarefa(self, tarefa: Tarefa) -> None:
        self._repo.salvar(tarefa)

    def concluir_tarefa(self, titulo: str) -> None:
        tarefa = self._repo.buscar_por_titulo(titulo)
        if not tarefa:
            raise TarefaNaoEncontrada(titulo)
        tarefa.concluir()

    def listar_tarefas(self) -> List[Tarefa]:
        return self._repo.listar()

    # ---------- relatório -----------
    def gerar_relatorio(self) -> str:
        """Delegação ao objeto que implementa RelatorioGerador (ISP)."""
        return self._relatorio.gerar(self)

    # ---------- representação -----------
    def __repr__(self) -> str:  # pragma: no cover
        return f"<Projeto {self.nome} ({len(self.listar_tarefas())} tarefas)>"