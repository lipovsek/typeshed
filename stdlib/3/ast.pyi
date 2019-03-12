# Python 3.5 ast

import sys
# Rename typing to _typing, as not to conflict with typing imported
# from _ast below when loaded in an unorthodox way by the Dropbox
# internal Bazel integration.
import typing as _typing
from typing import Any, Iterator, Optional, Union, TypeVar

from _ast import *

class NodeVisitor():
    def visit(self, node: AST) -> Any: ...
    def generic_visit(self, node: AST) -> Any: ...

class NodeTransformer(NodeVisitor):
    def generic_visit(self, node: AST) -> Optional[AST]: ...

_T = TypeVar('_T', bound=AST)

if sys.version_info >= (3, 8):
    def parse(source: Union[str, bytes], filename: Union[str, bytes] = ..., mode: str = ...,
              type_comments: bool = ..., feature_version: int = ...) -> AST: ...
else:
    def parse(source: Union[str, bytes], filename: Union[str, bytes] = ..., mode: str = ...) -> AST: ...

def copy_location(new_node: _T, old_node: AST) -> _T: ...
def dump(node: AST, annotate_fields: bool = ..., include_attributes: bool = ...) -> str: ...
def fix_missing_locations(node: _T) -> _T: ...
def get_docstring(node: AST, clean: bool = ...) -> str: ...
def increment_lineno(node: _T, n: int = ...) -> _T: ...
def iter_child_nodes(node: AST) -> Iterator[AST]: ...
def iter_fields(node: AST) -> Iterator[_typing.Tuple[str, Any]]: ...
def literal_eval(node_or_string: Union[str, AST]) -> Any: ...
def walk(node: AST) -> Iterator[AST]: ...
