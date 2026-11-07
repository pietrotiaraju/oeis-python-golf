# A000498

> Eulerian numbers (Euler's triangle: column k=4 of A008292, column k=3 of A173018).
> — [OEIS A000498](https://oeis.org/A000498)

Offset 4: 1, 26, 302, 2416, 15619, 88234, 455192, 2203488, 10187685, 45533450, …

a(n) is the number of permutations of n elements with exactly 3 descents
(positions i with p(i) > p(i+1)).

### Python 3 — 57 bytes

```python
n=4
while[print(4**n+~n*3**n+n*-~n*(3*2**n-n+1)//6)]:n+=1
```

**How it works**

- The Eulerian number with r descents is
  A(n, r) = Σ_{j=0}^{r+1} (−1)^j·C(n+1, j)·(r+1−j)ⁿ (the standard
  inclusion–exclusion formula; Comtet 1974). For r = 3 and n ≥ 1 the j = 4
  term is 0ⁿ = 0, so
  a(n) = 4ⁿ − (n+1)·3ⁿ + C(n+1, 2)·2ⁿ − C(n+1, 3), Mike Zabrocki's formula
  in the entry.
- The last two terms share n(n+1)/6:
  C(n+1, 2)·2ⁿ − C(n+1, 3) = n(n+1)(3·2ⁿ − n + 1)/6. That product is 6 times
  an integer, so `n*-~n*(3*2**n-n+1)//6` is exact, and `//` takes only the
  product because `*` and `//` group left to right above `+`.
- `~n*3**n` is −(n+1)·3ⁿ (`~n` = −n − 1) and `-~n` is n + 1.

**Notes**

- Other versions: the same formula with the 2-power term as a shift,
  `4**n+~n*3**n+(n*-~n<<n-1)-(n**3-n)//6`, 60 bytes; Zabrocki's formula
  written out with `while 1:`, 73 bytes. [A000460](../A000460/) (2 descents)
  and [A000295](../A000295/) (1 descent) are the neighbouring columns.
- Exact integer arithmetic, so the program is right for every n.
- The b-file has 197 terms (up to a(200)); the bar is the whole b-file in
  60 s. All of it prints in 0.1 s here.
- a(7143) is the first term with more than 4300 digits, so Python's
  int-to-str limit stops the printing there, after about 2 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 73 | first entry |
| 2026-11-07 | Python 3 | 57 | merge the last two terms over n(n+1)/6 |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000498), CC BY-SA 4.0.
