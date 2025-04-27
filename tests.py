from modulos.print import PrintContacts

def teste_localiza_e_foca_pesquisa() -> None:
    PrintContacts().localiza_e_foca_pesquisa()

def teste_print() -> None:
    PrintContacts().print("teste")

if __name__ == "__main__":
    teste_print()
    ...