__version__ = '1.1.1'

from .engine import run
from .utils import export_rule_data

# Appease pyflakes by "using" these exports
assert run
assert export_rule_data
