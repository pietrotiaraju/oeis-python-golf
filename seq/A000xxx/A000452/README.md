# A000452

> The greedy sequence of integers which avoids 3-term geometric progressions.
> — [OEIS A000452](https://oeis.org/A000452)

Offset 1: 1, 2, 3, 5, 6, 7, 8, 10, 11, 13, …

### Python 3 — 156 bytes

```python
def f(n):
 p=2
 while p*p<=n:
  e=0
  while n%p<1:n//=p;e+=1
  while e:
   if e%3==2:return 0
   e//=3
  p+=1
 return 1
n=1
while 1:
 if f(n):print(n)
 n+=1
```

**How it works**

Rankin's characterization of the greedy progression-free set is:
every exponent in the prime factorization has only 0 and 1 in base 3.
These exponents form the greedy three-term-arithmetic-progression-free
set. If an exponent has digits 2, subtract once and twice the sum
of their place values: both earlier exponents then have only digits
0 and 1, giving the two earlier terms of a forbidden progression.
Conversely the 0/1 ternary set has no nonconstant three-term
arithmetic progression, so no accepted integer can close a geometric
progression. Trial division extracts the exponents; any remaining
prime has exponent 1 and is automatically allowed.

**Notes**

- The program uses exact integer arithmetic and the standard library only.
- The verification bar is 10000 terms in 60 s; the official b-file contains 10000 terms.


## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 156 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000452), CC BY-SA 4.0.
