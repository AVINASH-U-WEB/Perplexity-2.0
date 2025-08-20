from langchain.tools import tool
from datetime import datetime
from zoneinfo import ZoneInfo
import ast
import operator as op

# Allowed operations for calculator
_ALLOWED_OPS = {
    ast.Add: op.add, ast.Sub: op.sub, ast.Mult: op.mul,
    ast.Div: op.truediv, ast.Pow: op.pow, ast.Mod: op.mod,
    ast.USub: op.neg
}

def _eval_expr(node):
    if isinstance(node, ast.Constant):
        return node.value
    elif isinstance(node, ast.BinOp):
        if type(node.op) in _ALLOWED_OPS:
            return _ALLOWED_OPS[type(node.op)](_eval_expr(node.left), _eval_expr(node.right))
    elif isinstance(node, ast.UnaryOp):
        if type(node.op) in _ALLOWED_OPS:
            return _ALLOWED_OPS[type(node.op)](_eval_expr(node.operand))
    raise TypeError(f"Unsupported expression type: {type(node)}")

@tool
def calculator(expression: str) -> str:
    """
    Evaluates a mathematical expression safely and returns the result as a string.
    Only supports basic arithmetic operations.
    """
    try:
        tree = ast.parse(expression, mode='eval')
        result = _eval_expr(tree.body)
        return str(result)
    except (TypeError, SyntaxError, ValueError, ZeroDivisionError) as e:
        return f"Error: Invalid expression. {e}"

@tool
def now_ist() -> str:
    """Returns the current date and time in IST (India Standard Time)."""
    dt_now = datetime.now(ZoneInfo("Asia/Kolkata"))
    return dt_now.strftime("%A, %Y-%m-%d %H:%M:%S %Z")