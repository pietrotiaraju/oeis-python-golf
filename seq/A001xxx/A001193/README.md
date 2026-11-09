# A001193

> a(n) = (n+1)*(2*n)!/(2^n*n!) = (n+1)*(2n-1)!!.
> — [OEIS A001193](https://oeis.org/A001193)

Offset 0: 1, 2, 9, 60, 525, 5670, 72765, 1081080, 18243225, 344594250, 7202019825, 164991726900, 4111043861925, 110681950128750, 3201870700153125, 99044533658070000, …

### Python 3 — 37 bytes

```python
d=n=1
while[print(n*d)]:d*=2*n-1;n+=1
```

**How it works**

- `d` is (2n−1)!! and `n` runs one ahead of the index, so the term is
  `n*d`; the next double factorial multiplies in 2n − 1 before `n` steps
  on. `d=n=1` covers (−1)!! = 1.

**Notes**

- The whole b-file prints at once.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 37 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001193), CC BY-SA 4.0.
