import re
from dataclasses import dataclass


@dataclass
class CategoriaCID10:
    codigo: str
    letra: str | None = None
    numero: int | None = None

    def __post_init__(self):
        PATTERN = r"([A-Za-z])(\d{2})"

        match = re.match(PATTERN, self.codigo)

        if not match:
            print(self.codigo)
            raise ValueError()

        self.letra = match.group(1)
        self.numero = int(match.group(2))

    def __eq__(self, other):
        if not isinstance(other, CategoriaCID10):
            raise NotImplementedError()

        return self.letra == other.letra and self.numero == other.numero

    def __ne__(self, other):
        return not self.__eq__(other)

    def __gt__(self, other):
        if not isinstance(other, CategoriaCID10):
            raise NotImplementedError()

        if (self.letra > other.letra) or (
            self.letra == other.letra and self.numero > other.numero
        ):
            return True

        return False

    def __lt__(self, other):
        if not isinstance(other, CategoriaCID10):
            raise NotImplementedError()

        if (self.letra < other.letra) or (
            self.letra == other.letra and self.numero < other.numero
        ):
            return True

        return False

    def __ge__(self, other):
        return self.__gt__(other) or self.__eq__(other)

    def __le__(self, other):
        return self.__lt__(other) or self.__eq__(other)
