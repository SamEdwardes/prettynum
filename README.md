# prettynum

Simple number formatting for python inspired by the [scales](https://scales.r-lib.org/index.html) package in R.

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