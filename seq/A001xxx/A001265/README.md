# A001265

> Table T(n,k) in which n-th row lists prime factors of 2^n - 1 (n >= 2), with repetition.
> — [OEIS A001265](https://oeis.org/A001265)

Offset 2: 3, 7, 3, 5, 31, 3, 3, 7, 127, 3, 5, 17, 7, 73, 3, 11, 31, 23, 89, 3, 3, 5, 7, 13, 8191, …

Row n (n ≥ 2) lists the prime factors of 2^n − 1 in increasing order, each
as often as it divides, and the rows are read one after another:
3 | 7 | 3, 5 | 31 | 3, 3, 7 | 127 | 3, 5, 17 | …

### Python 3 — 81 bytes

```python
d=M=m=3
while 1:
 if d*d>m:print(m);m=M=M-~M;d=2
 d+=m%d>0 or print(d)is(m:=m//d)
```

**How it works**

- `M` is the current 2^n − 1, and `m` is what is left of it after the
  factors printed so far. `M-~M` = 2M + 1 turns 2^n − 1 into 2^(n+1) − 1.
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
  no √m check; 2^n − 1 is odd, so it only moves d to 3.
- d never goes down within a row and the final prime m is at least d, so
  each row comes out in increasing order. The start `d=M=m=3` has
  d² = 9 > 3 and prints row 2 (just 3) at once. Exact integers throughout,
  so every row is right for every n.

**Notes**

- Trial division costs about max(√p₁, p₂) steps per row, p₁ ≥ p₂ the two
  largest prime factors. 2^61 − 1 is prime, so row 61 needs about
  1.5·10⁹ steps; rows 2 to 60 (250 entries, the largest step count about
  2·10⁶ at 2^49 − 1 = 127 · 4432676798593) print in about 1 reference second, and then
  the program stalls.
- Pollard's rho with a Miller–Rabin test gets further, but its primality
  decisions must be exact: Miller–Rabin with the first 13 primes as bases
  is proven only below 3.3·10²⁴ (Sorenson and Webster, 2015), and
  2^89 − 1 is a 27-digit prime. An ungolfed program of that kind reaches
  417 entries (rows 2 to 88) at several times the length.
- Without the √m stop the program is 13 bytes shorter but much slower
  (below).
- The b-file has 15035 entries (rows 2 to 1206), from factorizations far
  beyond trial division; the bar is the 250 entries of rows 2 to 60 in
  60 s.

## First 91 terms

A [separate record](../../../CONTRIBUTING.md#short-bar-records): the same
rules, but only the first 91 entries (rows 2 to 30) have to arrive in time.

### Python 3, 91 terms — 68 bytes

```python
M=m=1
while 1:
 if m<2:m=M=M-~M;d=2
 d+=m%d>0 or print(d)is(m:=m//d)
```

**How it works**

- The same division step without the √m stop: d climbs to the largest
  prime factor, which is printed and divided out like the others, and the
  row ends when m reaches 1. No prime below d divides m, so every printed
  d is prime, and d never goes down, so the row is in increasing order.
- `if m<2` then starts the next row, m = M = 2M + 1 with d = 2; the start
  `M=m=1` makes the first row M = 3.

**Limits**

- A row costs as many steps as its largest prime factor. 2^31 − 1 =
  2147483647 is prime, so row 31 needs about 2·10⁹ steps; rows 2 to 30
  (91 entries) print in about 0.1 reference seconds.

## History

**Python 3**

| Date | Bytes | Note |
|---|---|---|
| 2026-11-09 | 81 | first entry |

**Python 3, 91 terms**

| Date | Bytes | Note |
|---|---|---|
| 2026-11-09 | 68 | first entry: no √m stop |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001265), CC BY-SA 4.0.
