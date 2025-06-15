class Tarefa:
    """
    Representa uma tarefa dentro de um projeto.

    Atributos:
        titulo (str): Nome da tarefa.
        descricao (str): Detalhes sobre a tarefa.
        responsavel (Membro): Pessoa responsável pela tarefa.
        status (str): Estado atual da tarefa ('pendente' ou 'concluída').
    """

    PENDENTE = "pendente"
    CONCLUIDA = "concluida"

    def __init__(self, titulo, descricao, responsavel):
        """Inicializa uma nova tarefa."""
        self.titulo = titulo
        self.descricao = descricao
        self.responsavel = responsavel
        self.status = Tarefa.PENDENTE

    def concluir(self):
        """Marca a tarefa como concluída."""
        self.status = Tarefa.CONCLUIDA

    def __repr__(self):
        """Retorna uma representação em string da tarefa."""
        return f"<Tarefa {self.titulo} [{self.status}]>"


class TarefaUrgente(Tarefa):
    """
    Representa uma tarefa urgente dentro de um projeto.

    Atributos:
        nivel (int): Nível de urgência (quanto maior, mais crítico).
    """

    def __init__(self, titulo, descricao, responsavel, nivel=1):
        """Inicializa uma tarefa urgente."""
        super().__init__(titulo, descricao, responsavel)
        self.nivel = nivel

    def __repr__(self):
        """Retorna uma representação em string da tarefa urgente."""
        return f"<TarefaUrgente {self.titulo} n{self.nivel} [{self.status}]>"