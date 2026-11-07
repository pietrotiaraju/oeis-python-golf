# A000775

> a(n) = n! * (n + 1 + 2*Sum_{k=1...n} 1/k).
> — [OEIS A000775](https://oeis.org/A000775)

Offset 0: 1, 4, 12, 46, 220, 1268, 8568, 66456, 582048, 5681952, 61174080, 720089280, …

### Python 3 — 46 bytes

```python
a=f=n=1
while[print(a)]:a=a*n-~n*f+f;f*=n;n+=1
```

**How it works**

- With H_n = 1 + 1/2 + ··· + 1/n, a(n) = (n+1)! + 2·n!·H_n. From
  (n+1)! = n·n! + n! and n!·H_n = n·(n−1)!·H_{n−1} + (n−1)!:
  a(n) = n·a(n−1) + n! + 2·(n−1)! = n·a(n−1) + (n+2)·(n−1)!,
  valid from n = 1 (the OEIS entry gives it as a(n+1) = (n+1)·a(n) +
  (n+3)·n! for n > 0, but it also holds at n = 0).
- At the top of each round `a` = a(n−1) and `f` = (n−1)!; then `f*=n` and
  `n+=1` move the factorial and the counter on, as in
  [A000254](../A000254/).
- The update `a*n-~n*f+f` is a·n + (n+2)·f in 10 characters: `~n*f` is
  (−n−1)·f, so subtracting it adds (n+1)·f, and `+f` adds the last f.
  `a*n+f*(n+2)` and `(a+f)*n+2*f` are 11; `a*n-~-~n*f` is another 10.

**Notes**

- Starting from A000254's variables and printing `f*n+2*b` is 49 bytes.
  Subtracting n·n! from a(n) leaves n!·(1 + 2H_n) =
  [A000776](../A000776/), whose step only adds 2·(n−1)!, but printing the
  n·n! back costs more than the step saves.
- Exact integer arithmetic, correct for every n.
- The b-file has 101 terms (up to a(100)); the bar is the whole b-file in
  60 s. It prints them at once.
- a(n) first has more than 4300 digits at n = 1558, so printing stops
  there with a ValueError.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 46 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000775), CC BY-SA 4.0.
