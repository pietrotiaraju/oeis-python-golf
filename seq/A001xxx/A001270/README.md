# A001270

> Table of prime factors of 10^n - 1 (with multiplicity).
> — [OEIS A001270](https://oeis.org/A001270)

Offset 1: 3, 3, 3, 3, 11, 3, 3, 3, 37, 3, 3, 11, 101, 3, 3, 41, 271, 3, 3, 3, 7, 11, 13, 37, …

Row n (n ≥ 1) lists the prime factors of 10^n − 1 in increasing order,
each as often as it divides, and the rows are read one after another:
3, 3 | 3, 3, 11 | 3, 3, 3, 37 | 3, 3, 11, 101 | …

### Python 3 — 85 bytes

```python
M=m=9;d=2
while 1:
 if d*d>m:print(m);m=M=M*10+9;d=2
 d+=m%d>0 or print(d)is(m:=m//d)
```

**How it works**

- `M` is the current 10^n − 1, and `m` is what is left of it after the
  factors printed so far. `M*10+9` turns 10^n − 1 into 10^(n+1) − 1.
- Trial division keeps two facts at the top of the loop: m > 1, and no
  prime below d divides m. So if d² > m, m is prime (a composite m has a
  prime factor at most √m < d): it is printed as the last factor of the row,
  and the next row starts with d = 2.
- Otherwise the second line runs with d² ≤ m. If d does not divide m,
  `m%d>0` is `True` and d goes up by 1. If it does, d is prime (no smaller
  prime divides m), `print(d)` prints it, `(m:=m//d)` divides it out, and
  `None is m` is `False`, so d stays where it is for a repeated factor.
  Since d² ≤ m, m/d ≥ d ≥ 2: m never drops to 1.
- Right after a new row starts, the second line runs once with d = 2 and
  no √m check; 10^n − 1 is odd, so it only moves d to 3.
- d never goes down within a row and the final prime m is at least d, so
  each row comes out in increasing order. Row 1 (9 = 3 · 3) is factored
  from the start `M=m=9;d=2`. Exact integers throughout, so every row is
  right for every n.

**Notes**

- Trial division costs about max(√p₁, p₂) steps per row, p₁ ≥ p₂ the two
  largest prime factors. Rows 1 to 18 (101 entries, the largest step count
  about 2·10⁶ at 10^17 − 1 = 3² · 2071723 · 5363222357) print in under a
  reference second. Row 19 = 3² · 1111111111111111111 (a prime repunit)
  then needs about 10⁹ steps.
- Pollard's rho with a Miller–Rabin test gets further, but its primality
  decisions must be exact: Miller–Rabin with the first 13 primes as bases
  is proven only below 3.3·10²⁴ (Sorenson and Webster, 2015). An
  ungolfed program of that kind reaches 264 entries (rows 1 to 37) at
  several times the length; row 38 holds the 19-digit repunit prime and
  the 18-digit prime 909090909090909091, both too large for rho to split them,
  and row 41 a 30-digit prime.
- Without the √m stop the program is 15 bytes shorter but much slower
  (below). [A001265](../A001265/) is the same program for 2^n − 1.
- The b-file has 4999 entries (rows 1 to 352), from factorizations far
  beyond trial division; the bar is the 101 entries of rows 1 to 18 in
  60 s.

## First 59 terms

A [separate record](../../../CONTRIBUTING.md#short-bar-records): the same
rules, but only the first 59 entries (rows 1 to 12) have to arrive in time.

### Python 3, 59 terms — 70 bytes

```python
M=m=0
while 1:
 if m<2:m=M=M*10+9;d=2
 d+=m%d>0 or print(d)is(m:=m//d)
```

**How it works**

- The same division step without the √m stop: d climbs to the largest
  prime factor, which is printed and divided out like the others, and the
  row ends when m reaches 1. No prime below d divides m, so every printed
  d is prime, and d never goes down, so the row is in increasing order.
- `if m<2` then starts the next row, m = M = 10M + 9 with d = 2; the start
  `M=m=0` makes the first row M = 9.

**Limits**

- A row costs as many steps as its largest prime factor: rows 1 to 12
  (59 entries) need at most 513239 (row 11), while row 13 =
  3² · 53 · 79 · 265371653 needs about 2.7·10⁸.

## History

**Python 3**

| Date | Bytes | Note |
|---|---|---|
| 2026-11-09 | 85 | first entry |

**Python 3, 59 terms**

| Date | Bytes | Note |
|---|---|---|
| 2026-11-09 | 70 | first entry: no √m stop |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001270), CC BY-SA 4.0.
