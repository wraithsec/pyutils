#!/usr/bin/env python3 

class Dict(dict):
    """
    Dot notation access to dict attributes.
    Dict({'one':1})
    Dict(one=1)
     
    Will not work in form of 1:'one' as Dict.1 breaks
    """
    __getattr__ = dict.get
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__
