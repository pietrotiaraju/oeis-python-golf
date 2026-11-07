# A000757

> Number of cyclic permutations of [n] with no i -> i+1 (mod n).
> — [OEIS A000757](https://oeis.org/A000757)

Offset 0: 1, 0, 0, 1, 1, 8, 36, 229, 1625, 13208, 120288, 1214673, 13469897, 162744944, …

### Python 3 — 43 bytes

```python
d=1;a=n=0
while[print(a:=d-a)]:d=d*n^1;n+=1
```

**How it works**

- From the e.g.f. (1 − log(1−x))·e^(−x): A + A′ = e^(−x)/(1−x), the e.g.f.
  of the derangement numbers D(n) ([A000166](../A000166/)). So
  a(n) + a(n+1) = D(n) (an OEIS formula), i.e. a(n+1) = D(n) − a(n).
- When a(n) is printed, `d` holds D(n−1); the start d = 1, a = 0 plays
  D(−1) and a(−1), so the first print is 1 = a(0).
- D(n) = n·D(n−1) + (−1)ⁿ, and n·D(n−1) is even exactly when n is even
  (D(m) is odd for even m), so adding (−1)ⁿ is `^1`: `d=d*n^1`. At n = 0
  it gives 0^1 = 1 = D(0).

**Notes**

- Exact integer arithmetic, one multiplication per term.
- Moving the D update into the print (`a:=(d:=d*n^1)-a`, starting at
  n = −1) is 45 bytes.
- The whole b-file (201 terms) prints at once; it is the bar.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 43 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000757), CC BY-SA 4.0.
