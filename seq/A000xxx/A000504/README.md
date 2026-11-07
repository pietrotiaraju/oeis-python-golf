# A000504

> S2(j,2j+3) where S2(n,k) is a 2-associated Stirling number of the second kind.
> — [OEIS A000504](https://oeis.org/A000504)

Offset 1: 1, 56, 1918, 56980, 1636635, 47507460, 1422280860, 44346982680, 1446733012725, 49473074851200, …

a(n) is the number of ways to split 2n + 3 labelled elements into n blocks,
every block of size at least 2: the entry T(2n+3, n) of the triangle A008299.

### Python 3 — 60 bytes

```python
j=f=2
while[print(f*~-j*j*(10*j*j-5*j-3)//108)]:j+=1;f*=j-~j
```

**How it works**

- n blocks of size ≥ 2 on 2n + 3 elements leave three elements beyond n
  pairs, so there is one block of 5 and n − 1 pairs, or blocks of 4 and 3
  and n − 2 pairs, or three blocks of 3 and n − 3 pairs. These types give
  (2n+3)!/(5!·2^(n−1)·(n−1)!), (2n+3)!/(4!·3!·2^(n−2)·(n−2)!) and
  (2n+3)!/(3!⁴·2^(n−3)·(n−3)!) partitions (the fourth 3! is the number of
  orders of the three blocks of size 3). Their sum is

  a(n) = (2n+3)!/(2ⁿ·n!) · n·(1/60 + (n−1)/36 + (n−1)(n−2)/162)
       = (2n+3)!/(2ⁿ·n!) · n(10n² + 15n + 2)/1620.

- (2n+3)!/(2ⁿ·n!) = 2(n+1)·(2n+3)!!, so a(n) = n(n+1)(10n² + 15n + 2)·(2n+3)!!/810.
  This is the formula van Hoeij found by fitting ("it appears" in the OEIS
  entry); the count above proves it.
- The program runs j = n + 1, where n(n+1) = (j−1)·j and
  10n² + 15n + 2 = 10j² − 5j − 3, and keeps f = 2·(2j+1)!!/15: f = 2 at
  j = 2, and each step multiplies it by 2j + 1 = `j-~j` (`~j` is −j−1).
  Then a(n) = f·(j−1)·j·(10j² − 5j − 3)/108, and `//108` is exact because
  the quotient is the integer a(n). `~-j` is j − 1.
- `j=f=2` sets both seeds at once, and `while[print(…)]:` prints before each
  step (a one-element list is always true).

**Notes**

- The same closed form in n, with f = (2n+3)!!/15, is 61 bytes:
  `n=f=1` / `while[print(f*n*-~n*(10*n*n+15*n+2)//54)]:n+=1;f*=2*n+3`. In
  m = 2n + 3 with f = m!!/3 it is 62 bytes. Mathar's first-order recurrence
  a(n)·(n−1)(10n² − 5n − 3) = a(n−1)·(2n+3)(n+1)(10n² + 15n + 2) is 84 bytes.
- Exact integer arithmetic, so the program is right for every n.
- The b-file has 17 terms (up to a(17)); the bar is the whole b-file in
  60 s.
- Python's 4300-digit int-to-str limit stops the printing after a(1418)
  (4298 digits; a(1419) has 4302), which the program reaches in under a
  second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 84 | first entry |
| 2026-11-07 | Python 3 | 60 | closed form with a running double factorial |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000504), CC BY-SA 4.0.
