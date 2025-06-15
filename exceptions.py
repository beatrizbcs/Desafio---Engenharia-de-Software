class TarefaNaoEncontrada(Exception):
    """Exceção lançada quando uma tarefa não é encontrada no repositório."""

    def __init__(self, titulo):
        """Inicializa a exceção com o título da tarefa não encontrada."""
        super().__init__(f"Tarefa '{titulo}' não encontrada.")