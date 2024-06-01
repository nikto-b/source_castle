from __future__ import annotations

import traceback
from dataclasses import dataclass
from typing import Optional

import model.grammar
from model.nterm import Nonterminal
from model.grammar import CFG
from parse import parse_prog, ParseError

"""

    PROG -> BLOCK
    BLOCK -> '{' OPS '}'
    OPS -> EXPR TAIL
    TAIL -> ';' EXPR TAIL | ε
    EXPR -> TERM OP_ASSIGN CALC_EXPR | CALC_EXPR
    CALC_EXPR -> START_EXPR | START_EXPR OP_CMP START_EXPR
    
    # START_EXPR -> TERM | SIGN TERM | START_EXPR OP_SUM TERM
    
    START_EXPR -> TERM START_EXPR` | SIGN TERM START_EXPR` | TERM | SIGN TERM
    START_EXPR` -> OP_SUM TERM START_EXPR` | OP_SUM TERM 
    
    # TERM -> FACTOR | TERM OP_MUL FACTOR
    
    TERM -> FACTOR TERM` | FACTOR
    TERM` -> OP_MUL FACTOR TERM` | OP_MUL FACTOR
    
    FACTOR -> 'I' | 'C' | '(' START_EXPR ')' | 'not' FACTOR
    OP_CMP -> '=' | '<>' | '<' | '<=' | '>' | '>' '='
    SIGN -> '+' | '-'
    OP_SUM -> '+' | '-' | 'or'
    OP_MUL -> '*' | '/' | 'div' | 'mod' | 'and'
    OP_ASSIGN -> ':='
    
"""


def main():
    G1str = """
    PROG -> BLOCK
    BLOCK -> '{' OPS '}'
    OPS -> EXPR TAIL
    TAIL -> ';' EXPR TAIL | ε
    EXPR -> 'C' OP_ASSIGN CALC_EXPR | CALC_EXPR
    CALC_EXPR -> START_EXPR | START_EXPR OP_CMP START_EXPR
        
    START_EXPR -> TERM START_EXPR` | SIGN TERM START_EXPR` | TERM | SIGN TERM
    START_EXPR` -> OP_SUM TERM START_EXPR` | OP_SUM TERM 
        
    TERM -> FACTOR TERM` | FACTOR
    TERM` -> OP_MUL FACTOR TERM` | OP_MUL FACTOR
    
    FACTOR -> 'I' | 'C' | '(' START_EXPR ')' | 'not' FACTOR
    OP_CMP -> '=' | '<>' | '<' | '<=' | '>' | '>='
    SIGN -> '+' | '-'
    OP_SUM -> '+' | '-' | 'or'
    OP_MUL -> '*' | '/' | 'div' | 'mod' | 'and'
    OP_ASSIGN -> ':='
    """

    G1 = CFG.fromstring(G1str)
    print(G1)

    first = {}

    while True:
        txt = input('(?)> ')
        try:
            print(parse_prog(G1, txt))
        except ParseError as e:
            print(e)
            traceback.print_exc()
        # print(G1.get_first(Nonterminal(nterm)))
        # print(G1.get_follow(Nonterminal(nterm)))


if __name__ == '__main__':
    main()
