from modulos.confirm import Confirm
from modulos.print import PrintContacts

def teste_localiza_e_foca_pesquisa() -> None:
    PrintContacts().localiza_e_foca_pesquisa()

def teste_print() -> None:
    PrintContacts().print("teste")
    
def teste_confirm() -> None:
    c = Confirm("Teste")
    assert c.status == "continue" or "abort"

if __name__ == "__main__":
    # teste_print()
    teste_confirm()
    ...