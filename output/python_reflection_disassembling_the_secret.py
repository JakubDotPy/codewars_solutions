"""Kata - Python Reflection: Disassembling the secret

completed at: 2024-07-28 20:27:31
by: Jakub Červinka

There is a string of 32 alphanumeric characters hidden inside a dynamically generated function, which will then be passed into your function.

Your task is to recover this string and return it.
"""

import dis

def find_the_secret(f):
    for instr in dis.get_instructions(f):
        if (
            instr.opname == 'LOAD_CONST'
            and len(instr.argval) == 32
        ):
            return instr.argval
