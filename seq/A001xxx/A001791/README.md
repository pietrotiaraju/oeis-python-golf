# A001791

> a(n) = binomial coefficient C(2n, n-1).
> — [OEIS A001791](https://oeis.org/A001791)

Offset 0: 0, 1, 4, 15, 56, 210, 792, 3003, 11440, 43758, …

### Python 3 — 43 bytes

```python
c=n=1
while[print(~-n*c)]:n+=1;c=4*c-6*c//n
```

**How it works**

- C(2k, k−1) = C(2k, k)·k/(k+1) = k·C(k), with C(k) the Catalan numbers.
- The loop is the Catalan loop of [A000108](../../A000xxx/A000108/): after
  `n+=1;c=4*c-6*c//n`, c = C(n−1) (C(n−1) = C(n−2)·(4n−6)/n, and 6c/n is
  an integer because 4c − 6c/n is). So `~-n*c` = (n−1)·C(n−1) = a(n−1), and
  `c=n=1` prints a(0) = 0 first.

**Notes**

- Exact integer arithmetic, correct for every n. a(7146) is the first term
  over 4300 digits, where Python's int-to-str limit stops the program.
- `import math` / `n=0` / `while[print(math.comb(2*n,n+1))]:n+=1` (using
  C(2n, n−1) = C(2n, n+1), which is 0 at n = 0) is 53 bytes; keeping
  C(2n, n) and printing `c*n//-~n` is 50.
- The b-file has 1201 terms (a(0) to a(1200)); the bar is the whole b-file
  in 60 s, which takes a fraction of a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-16 | Python 3 | 43 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001791), CC BY-SA 4.0.
