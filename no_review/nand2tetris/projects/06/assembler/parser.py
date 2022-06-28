from enum import Enum
import re
from typing import List, Tuple


class CommandType(Enum):
    A = 'A'
    C = 'C'
    LABEL = 'LABEL'
    VARIABLE = 'VARIABLE'
    UNKNOWN = 'UNKNOWN'


symbols_table = {
    'R0': 0,
    'R1': 1,
    'R2': 2,
    'R3': 3,
    'R4': 4,
    'R5': 5,
    'R6': 6,
    'R7': 7,
    'R8': 8,
    'R9': 9,
    'R10': 10,
    'R11': 11,
    'R12': 12,
    'R13': 13,
    'R14': 14,
    'R15': 15,
    'SCREEN': 16384,
    'KBD': 24576,
    'SP': 0,
    'LCL': 1,
    'ARG': 2,
    'THIS': 3,
    'THAT': 4,
}


class Reader:
    def __init__(self, file_path):
        self.file_path = file_path
        self.commands: List[Tuple[str, CommandType]] = []

    def _sanitize(self, lines: List[str]):
        lines_sanitized = []
        for line in lines:
            if line in ['\n', '\r', '\r\n'] or line.startswith('//'):
                continue
            lines_sanitized.append(''.join(line.strip().split()))
        return lines_sanitized

    def read_file(self):
        lines = None
        with open(self.file_path) as f:
            lines = f.readlines()
        return self._sanitize(lines)


class Parser:
    def __init__(self, line: str):
        self.line = line

    def _get_command_type(self):
        if self.line.startswith('@'):
            text = self.line[1::]
            if text.isdecimal():
                return CommandType.A
            if text in symbols_table:
                return CommandType.VARIABLE
        elif self.line.startswith('(') and self.line.endswith(')'):
            text = self.line[1:-1]
            if text:
                return CommandType.LABEL
        elif self.line.startswith('D='):
            text = self.line[2::]
            if text:
                return CommandType.C

        return CommandType.UNKNOWN

    def get_parser(self):
        type = self._get_command_type()
        if type == CommandType.A:
            return AParser(self.line)
        elif type == CommandType.VARIABLE:
            return VParser(self.line)
        elif type == CommandType.LABEL:
            return LParser(self.line)
        elif type == CommandType.C:
            return CParser(self.line)


class AtParser:
    def __init__(self, line: str):
        self.line = line

    def val(self):
        return self.line[1::]


class AParser(AtParser):
    pass


class VParser(AtParser):
    pass


class LParser:
    def __init__(self, line: str):
        self.line = line

    def val(self):
        return self.line[1:-1]


class CParser:
    def __init__(self, line: str):
        self.line = line

    def comp(self):
        return re.search('(?<=\D=).*', self.line)

    def dest():
        pass

    def jmp():
        pass


class Translator:
    def __init__(self, command):
        self.command = command

    def comp():
        pass

    def dest():
        pass

    def jmp():
        pass
