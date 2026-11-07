# A000460

> Eulerian numbers (Euler's triangle: column k=3 of A008292, column k=2 of A173018).
> — [OEIS A000460](https://oeis.org/A000460)

Offset 3: 1, 11, 66, 302, 1191, 4293, 14608, 47840, 152637, 478271, …

a(n) is the number of permutations of n elements with exactly 2 descents
(positions i with π(i) > π(i+1)).

### Python 3 — 44 bytes

```python
n=3
while[print(3**n-~n*(n-(2<<n))//2)]:n+=1
```

**How it works**

- **The formula.** The Eulerian number with r descents is
  A(n, r) = Σ_{j=0}^{r} (−1)^j·C(n+1, j)·(r+1−j)ⁿ (the classical explicit
  formula, Graham–Knuth–Patashnik, Concrete Mathematics, eq. (6.38)). For
  r = 2 this is a(n) = 3ⁿ − (n+1)·2ⁿ + C(n+1, 2).
- **Grouping the (n+1)s.** −(n+1)·2ⁿ + n(n+1)/2 = −(n+1)(2^(n+1) − n)/2.
  In the code `3**n-~n*(n-(2<<n))//2` the `-` is binary and `~n` is
  −(n+1), so it reads 3ⁿ − ((~n)·(n − 2^(n+1)))//2 with
  (~n)·(n − 2^(n+1)) = (n+1)(2^(n+1) − n); `*` and `//` bind tighter than
  `-` and group to the left. `2<<n` is 2^(n+1).
- **Exactness.** (n+1)(2^(n+1) − n) = (n+1)·2^(n+1) − n(n+1) is even (both
  parts are), so the `//2` is exact.

**Notes**

- Other versions that print the same terms:
  `3**n+~n*2**n+n*-~n//2` and `3**n+(~n<<n)+n*-~n//2` in the same loop:
  also 44 bytes; the original
  `while 1:print(3**n-(n+1)*2**n+n*(n+1)//2);n+=1`: 50 bytes.
- Exact integer arithmetic, so the program is right for every n.
- The b-file's 998 terms print in 0.1 s here. The b-file has 998 terms (up
  to a(1000)); the bar is the whole b-file in 60 s.
- a(n) is close to 3ⁿ, so a(9013) is the first term with more than 4300
  digits and printing stops there (after about 2 s).
- [A000498](../A000498/) is the next column (3 descents).

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 50 | first entry |
| 2026-11-07 | Python 3 | 44 | (n+1)(n − 2^(n+1))/2 in one product |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000460), CC BY-SA 4.0.
