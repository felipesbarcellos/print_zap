from modulos.print import PrintContacts
from modulos.gemini import run
from modulos.confirm import Confirm

if __name__ == "__main__":
    PrintContacts().print()
    status = Confirm("Print Contatos").status
    if status == "continue":
        run()