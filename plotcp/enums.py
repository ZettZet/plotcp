from enum import Flag, auto


class Faxis(Flag):
    ORIG = auto()
    TRANSFORM = auto()
    BOTH = ORIG | TRANSFORM


class Reim(Flag):
    RE = auto()
    IM = auto()
    BOTH = RE | IM


class Inits(Flag):
    ORIG = auto()
    TRANSFORM = auto()
    BOTH = ORIG | TRANSFORM
