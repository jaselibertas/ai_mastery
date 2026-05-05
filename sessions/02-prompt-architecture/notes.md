python sessions/02-prompt-architecture/demo.py 
=== BASIC (no system prompt) ===
# Code Review

## Overall Assessment
This is a simple, functional addition function, but it lacks robustness for production use.

## Issues & Recommendations

### 1. **Missing Type Hints** ⚠️
```python
# Current
def add(a, b):
    return a + b

# Better
def add(a: int | float, b: int | float) -> int | float:
    return a + b
```

### 2. **Missing Documentation** ⚠️
```python
def add(a: int | float, b: int | float) -> int | float:
    """
    Add two numbers together.
    
    Args:
        a: First number
        b: Second number
        
    Returns:
        Sum of a and b
    """
    return a + b
```

### 3. **No Input Validation** ⚠️
The function will accept any types that support the `+` operator (strings, lists, etc.), which may not be intended:
```python
add("hello", "world")  # Returns "helloworld"
add([1], [2])          # Returns [1, 2]
```

### 4. **No Error Handling**
Consider whether you need to handle edge cases like `None` values or incompatible types.

## Improved Version

```python
def add(a: int | float, b: int | float) -> int | float:
    """
    Add two numbers together.
    
    Args:
        a: First number (int or float)
        b: Second number (int or float)
        
    Returns:
        Sum of a and b
        
    Raises:
        TypeError: If inputs are not numeric types
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both arguments must be int or float")
    return a + b
```

## Verdict
✅ **Functional** for basic use cases  
⚠️ **Not production-ready** without improvements

Tokens — in: 22 out: 482

=== ENGINEERED (system prompt + XML) ===
# Code Review

## Issues and Improvements

1. **[Line 1] MINOR - Style**: Function lacks proper formatting according to PEP 8 standards. Single-line function definitions should be reserved for very simple lambdas or used sparingly. This should be reformatted to multi-line for better readability.

2. **[Line 1] MINOR - Style**: Missing spaces after commas in parameter list. Should be `add(a, b)` instead of `add(a,b)`.

3. **[Line 1] MEDIUM - Documentation**: Missing docstring. All functions should include a docstring describing purpose, parameters, and return value.

4. **[Line 1] MEDIUM - Type Safety**: Missing type hints. Modern Python code should include type annotations for better code clarity and IDE support.

5. **[Line 1] LOW - Robustness**: No input validation. While Python's duck typing allows flexible inputs, consider whether you want to restrict types or handle edge cases.

## Recommended Refactored Version

```python
def add(a: int | float, b: int | float) -> int | float:
    """
    Add two numbers together.
    
    Args:
        a: First number to add
        b: Second number to add
        
    Returns:
        The sum of a and b
        
    Examples:
        >>> add(2, 3)
        5
        >>> add(2.5, 3.5)
        6.0
    """
    return a + b
```

## Summary
- **Critical Issues**: 0
- **Medium Issues**: 2 (documentation, type hints)
- **Minor Issues**: 2 (formatting, spacing)

The function is functionally correct but lacks professional Python code standards for production use.

Tokens — in: 84 out: 411