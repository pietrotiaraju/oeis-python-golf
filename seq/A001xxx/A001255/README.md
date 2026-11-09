# A001255

> Squares of partition numbers.
> — [OEIS A001255](https://oeis.org/A001255)

Offset 0: 1, 1, 4, 9, 25, 49, 121, 225, 484, 900, 1764, 3136, 5929, 10201, 18225, 30976, 53361, 88209, 148225, 240100, …

### Python 3 — 82 bytes

```python
*a,n=1,0
while[print(a[-1]**2)]:n-=1;a+=sum(d*sum(a[d::d])for d in range(n,0))//n,
```

**How it works**

- The program is the [A000041](../../A000xxx/A000041/) record with its
  term squared. That record uses n·p(n) = Σ_{k≥1} σ(k)·p(n−k), written as
  Σ_d d·Σ_j p(n − j·d). `sum(a[d::d])` reads every d-th earlier value,
  counting back from the end (d < 0).

**Notes**

- The whole b-file (1001 terms) prints in well under a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 82 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001255), CC BY-SA 4.0.
