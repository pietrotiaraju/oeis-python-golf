# A001269

> Table T(n,k) in which n-th row lists prime factors of 2^n + 1 (n >= 0), with repetition.
> — [OEIS A001269](https://oeis.org/A001269)

Offset 0: 2, 3, 5, 3, 3, 17, 3, 11, 5, 13, 3, 43, 257, 3, 3, 3, 19, 5, 5, 41, 3, 683, 17, 241, …

Row n (n ≥ 0) lists the prime factors of 2^n + 1 in increasing order, each
as often as it divides, and the rows are read one after another:
2 | 3 | 5 | 3, 3 | 17 | 3, 11 | 5, 13 | …

### Python 3 — 82 bytes

```python
d=M=m=2
while 1:
 if d*d>m:print(m);m=M=M+M-1;d=2
 d+=m%d>0 or print(d)is(m:=m//d)
```

**How it works**

- `M` is the current 2^n + 1, and `m` is what is left of it after the
  factors printed so far. `M+M-1` = 2M − 1 turns 2^n + 1 into
  2^(n+1) + 1.
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
  no √m check; 2^n + 1 is odd for n ≥ 1, so it only moves d to 3.
- d never goes down within a row and the final prime m is at least d, so
  each row comes out in increasing order. The start `d=M=m=2` has
  d² = 4 > 2 and prints row 0 (just 2) at once. Exact integers
  throughout, so every row is right for every n.

**Notes**

- Trial division costs about max(√p₁, p₂) steps per row, p₁ ≥ p₂ the two
  largest prime factors. Rows 0 to 57 (190 entries, the largest step count
  about 5·10⁶ at 2^53 + 1 = 3 · 107 · 28059810762433) print in about
  2 reference seconds. Row 58 = 5 · 107367629 · 536903681 then needs about
  10⁸ steps, and row 61 = 3 · 768614336404564651 (a prime) about 9·10⁸.
- Pollard's rho with a Miller–Rabin test gets further, but its primality
  decisions must be exact: Miller–Rabin with the first 13 primes as bases
  is proven only below 3.3·10²⁴ (Sorenson and Webster, 2015), and
  2^92 + 1 = 17 · 291280009243618888211558641 has a 27-digit prime
  factor. An ungolfed program of that kind reaches 361 entries (rows 0
  to 91) at several times the length.
- Without the √m stop the program is 11 bytes shorter but much slower
  (below). [A001265](../A001265/) is the same program for 2^n − 1.
- The b-file has 10121 entries (rows 0 to 1122), from factorizations far
  beyond trial division; the bar is the 190 entries of rows 0 to 57 in
  60 s.

## First 81 terms

A [separate record](../../../CONTRIBUTING.md#short-bar-records): the same
rules, but only the first 81 entries (rows 0 to 30) have to arrive in time.

### Python 3, 81 terms — 71 bytes

```python
d=M=m=2
while 1:
 if m<2:m=M=M+M-1;d=2
 d+=m%d>0 or print(d)is(m:=m//d)
```

**How it works**

- The same division step without the √m stop: d climbs to the largest
  prime factor, which is printed and divided out like the others, and the
  row ends when m reaches 1. No prime below d divides m, so every printed
  d is prime, and d never goes down, so the row is in increasing order.
- `if m<2` then starts the next row, m = M = 2M − 1 with d = 2. The start
  `d=M=m=2` divides row 0 (2) at once.

**Limits**

- A row costs as many steps as its largest prime factor: the slowest of
  rows 0 to 30 (81 entries) is 2^28 + 1 = 17 · 15790321, and row 31 =
  3 · 715827883 needs about 7·10⁸ steps.

## History

**Python 3**

| Date | Bytes | Note |
|---|---|---|
| 2026-11-09 | 82 | first entry |

**Python 3, 81 terms**

| Date | Bytes | Note |
|---|---|---|
| 2026-11-09 | 71 | first entry: no √m stop |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001269), CC BY-SA 4.0.
