# prettynum

Simple number formatting for python inspired by the [scales](https://scales.r-lib.org/index.html) package in R. `prettynum` is lightweight and has not third party library dependencies.

- GitHub: [https://github.com/SamEdwardes/prettynum](https://github.com/SamEdwardes/prettynum)
- PyPi:  [https://pypi.org/project/prettynum/](https://pypi.org/project/prettynum/)

## Installation

```bash
pip install prettynum
```

## Usage

```python
>>> from prettynum import comma, dollar
>>> comma(1000)
'1,000'
>>> comma(1000, 3)
'1,000.000'
>>> comma(1000.89, 1)
'1,000.9'
>>> dollar(1000)
'$1,000'
>>> dollar(1000, 3)
'$1,000.000'
>>> dollar(1000.89, 1)
'$1,000.9'
```
