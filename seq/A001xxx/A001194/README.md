# A001194

> a(n) = A059366(n,n-2) = A059366(n,2) for n >= 2, where the triangle A059366 arises in the expansion of a trigonometric integral.
> — [OEIS A001194](https://oeis.org/A001194)

Offset 2: 3, 9, 54, 450, 4725, 59535, 873180, 14594580, 273648375, 5685805125, 129636356850, 3217338674550, 86331921100425, 2490343877896875, 76844896803675000, 2525635608280785000, …

### Python 3 — 48 bytes

```python
d=1;n=2
while[print(3*n*~-n//2*d)]:d*=2*n-3;n+=1
```

**How it works**

- V. Kotesovec's closed form a(n) = 3n(n−1)·(2n−4)!/(2ⁿ⁻¹·(n−2)!) is
  3·C(n,2)·(2n−5)!!, since (2n−4)!/(2ⁿ⁻²·(n−2)!) = (2n−5)!!.
- `d` is the double factorial, starting at (−1)!! = 1 for n = 2, and
  `3*n*~-n//2` is 3·C(n,2).

**Notes**

- The whole b-file prints at once.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 48 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001194), CC BY-SA 4.0.
