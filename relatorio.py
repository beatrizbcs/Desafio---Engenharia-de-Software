from abc import ABC, abstractmethod
from typing import List


class RelatorioGerador(ABC):
    """Contrato (ISP) para qualquer gerador de relatório de projeto."""

    @abstractmethod
    def gerar(self, projeto) -> str:  # noqa: ANN001  (projeto é “qualquer”)
        """Recebe um objeto Projeto e devolve o relatório como string."""


class TextoRelatorioGerador(RelatorioGerador):
    """Implementação padrão: devolve o relatório em texto simples."""

    def gerar(self, projeto) -> str: 
        linhas: List[str] = [
            f"Projeto: {projeto.nome}",
            f"Prazo: {projeto.prazo:%d/%m/%Y}",
            f"Descrição: {projeto.descricao}",
            "Membros:",
            *[f" - {m.nome} ({m.funcao})" for m in projeto._membros], 
            "Tarefas:",
            *[
                f" - {t.titulo} [{t.status}] - Resp.: {t.responsavel.nome}"
                for t in projeto.listar_tarefas()
            ],
        ]
        return "\n".join(linhas)