# A000914

> Stirling numbers of the first kind: s(n+2, n).
> — [OEIS A000914](https://oeis.org/A000914)

Offset 0: 0, 2, 11, 35, 85, 175, 322, 546, 870, 1320, 1925, 2717, 3731, 5005, …

### Python 3 — 40 bytes

```python
a=n=0
while[print(a)]:n+=1;a+=n*~n*~n//2
```

**How it works**

- The Stirling recurrence [n+2, n] = (n+1)·[n+1, n] + [n+1, n−1] with
  [n+1, n] = C(n+1, 2) gives a(n) = a(n−1) + n(n+1)²/2 (Walsh's formula on
  the OEIS page), starting from a(0) = 0.
- `~n` is −(n+1), so `n*~n*~n` is n(n+1)²; n(n+1) is even, so `//2` is
  exact. The partial sums beat the closed form
  n(n+1)(n+2)(3n+5)/24 by 7 bytes.
- Putting the update inside the print (`print(a:=a+n*~n*~n//2)`, which adds
  0 for n = 0) is also 40 bytes.

**Notes**

- Exact integer arithmetic, correct for every n.
- The b-file has 1001 terms (up to a(1000)); the bar is the whole b-file in
  60 s. It prints them at once.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 40 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000914), CC BY-SA 4.0.
