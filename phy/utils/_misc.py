# -*- coding: utf-8 -*-

"""Utility functions."""


#------------------------------------------------------------------------------
# Imports
#------------------------------------------------------------------------------

import os.path as op
from inspect import getargspec


#------------------------------------------------------------------------------
# Various Python utility functions
#------------------------------------------------------------------------------

def _as_dict(x):
    """Convert a list of tuples to a dict."""
    if isinstance(x, list):
        return dict(x)
    else:
        return x


def _fun_arg_count(f):
    """Return the number of arguments of a function.

    WARNING: with methods, only works if the first argument is named 'self'.

    """
    args = getargspec(f).args
    if args and args[0] == 'self':
        args = args[1:]
    return len(args)


#------------------------------------------------------------------------------
# Config
#------------------------------------------------------------------------------

_PHY_USER_DIR_NAME = '.phy'

def _phy_user_dir(sub_dir=None):
    """Return the absolute path to the phy user directory."""
    home = op.expanduser("~")
    path = op.realpath(op.join(home, _PHY_USER_DIR_NAME))
    if sub_dir is not None:
        path = op.join(path, sub_dir)
    return path


def _ensure_phy_user_dir_exists():
    """Create the phy user directory if it does not exist."""
    path = _phy_user_dir
    if not os.exists(path):
        os.mkdir(path)
