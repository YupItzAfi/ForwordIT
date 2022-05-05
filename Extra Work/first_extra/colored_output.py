from colorama import Fore
text = input(f"{Fore.CYAN}Your Text{Fore.RED}: {Fore.CYAN}")
color = input(f"{Fore.CYAN}Your Color{Fore.RED}: {Fore.CYAN}")


class Using_Colorama():
    text = ""

    def __init__(self, text="") -> None:
        self.text = text

    def print(self, text=text, color="BLACK"):
        try:
            print(getattr(Fore, color.upper()), text)
            return self
        except AttributeError:
            print(f"The Color \"{color}\" does not exist")


colored_text = Using_Colorama("BOOOYAYA")
colored_text.print(text, color)
