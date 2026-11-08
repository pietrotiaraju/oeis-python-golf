# A001096

> a(n) = n + n*(n-1)*(n-2)*(n-3)*(n-4)*(n-5).
> — [OEIS A001096](https://oeis.org/A001096)

Offset 0: 0, 1, 2, 3, 4, 5, 726, 5047, 20168, 60489, …

### Python 3 — 49 bytes

```python
n=0
while[print((s:=n*n-5*n)*(s+4)*(s+6)+n)]:n+=1
```

**How it works**

- With s = n(n − 5) = n² − 5n, the six factors pair from the outside in:
  n(n−5) = s, (n−1)(n−4) = s + 4 and (n−2)(n−3) = s + 6, so
  a(n) = s(s + 4)(s + 6) + n.
- The walrus `(s:=n*n-5*n)` stores s inside the print, so the quadratic is
  written once.

**Notes**

- The definition as written is 56 bytes; `from math import*` with
  `n+perm(n,6)` is 52; the [A001095](../A001095/) square,
  `n*((n-5)*(n*n-5*n+5)**2-n+6)`, and a quintic in m = n − 3 both make
  51-byte programs.
- Exact integer arithmetic, so the program is right for every n.
- The b-file has 1001 terms (up to a(1000)); the bar is the whole b-file in
  60 s.
- Siblings with four and five factors: [A001094](../A001094/) and
  [A001095](../A001095/).

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-08 | Python 3 | 49 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001096), CC BY-SA 4.0.
