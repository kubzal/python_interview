# Valid Parentheses

In programming and mathematical expressions, **valid parentheses** refer to a sequence of parentheses that are correctly balanced and properly nested. This is a common problem encountered in coding challenges and interviews.

## Problem Statement

Given a string containing just the characters `(`, `)`, `{`, `}`, `[` and `]`, determine if the input string is valid.

An input string is valid if:

1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.

### Example

```python
Input: "()"
Output: True
```

```python
Input: "()[]{}"
Output: True
```

```python
Input: "(]"
Output: False
```

```python
Input: "([)]"
Output: False
```

```python
Input: "{[]}"
Output: True
```
