# A000537

> Sum of first n cubes; or n-th triangular number squared.
> — [OEIS A000537](https://oeis.org/A000537)

Offset 0: 0, 1, 9, 36, 100, 225, 441, 784, 1296, 2025, …

### Python 3 — 33 bytes

```python
t=n=0
while[print(t*t)]:n+=1;t+=n
```

**How it works**

- Nicomachus's identity: 1³ + 2³ + … + n³ = T(n)², with T(n) = n(n+1)/2 the
  n-th triangular number ([A000217](../A000217/)). By induction:
  T(n) + T(n−1) = n(n+1)/2 + n(n−1)/2 = n², so
  T(n)² − T(n−1)² = (T(n) − T(n−1))·(T(n) + T(n−1)) = n·n² = n³.
- `t` is T(n): each pass adds the new n to it, so the program keeps a
  running triangular number and prints its square; no cube is formed.
- `print` sits in the loop condition: it returns `None`, and `[None]` is a
  non-empty list, so the loop never ends (the [A000007](../A000007/) loop).
  The first pass prints a(0) = 0 before anything is added.

**Notes**

- Other versions that print the same terms:
  - the running sum of cubes used for the higher powers
    ([A000538](../A000538/)–[A000542](../A000542/)),
    `n=a=0` / `while[print(a)]:n+=1;a+=n**3`: 34 bytes, and with the
    walrus in the print, `a=n=0` / `while[print(a:=a+n**3)]:n+=1`: also 34;
  - `t-=~n;n+=1` in place of `n+=1;t+=n`: 34 bytes;
  - the closed form, `n=0` / `while[print((n*n+n>>1)**2)]:n+=1`: 36 bytes.
- Exact integer arithmetic, so the program is right for every n.
- About 5.2 million terms in 60 s here. The b-file has 1001 terms
  (up to a(1000)); the bar is the whole b-file in 60 s, and it prints in
  well under a second.
- a(n) < n⁴ for n ≥ 2, so a term with more than 4300 digits (Python's
  int-to-str limit) needs n > 10^1075: out of reach.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 34 | first entry |
| 2026-11-07 | Python 3 | 33 | square of a running triangular number |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000537), CC BY-SA 4.0.
