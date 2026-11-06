# A000442

> a(n) = (n!)^3.
> — [OEIS A000442](https://oeis.org/A000442)

Offset 0: 1, 1, 8, 216, 13824, 1728000, 373248000, 128024064000, 65548320768000, 47784725839872000, …

### Python 3 — 36 bytes

```python
a=1;n=0
while[print(a)]:n+=1;a*=n**3
```

**How it works**

- Start with a=(0!)³=1 and n=0. After printing, increase n and
  multiply a by n³. Since (n!)³=n³·((n−1)!)³, the invariant
  a=(n!)³ holds at every subsequent print.
- Incrementing before multiplication matters: using the old initial
  n=0 would set a to zero permanently. The actual first update
  multiplies by 1 and supplies the second 1 in the sequence.
- `while[print(a)]` prints in the condition; the one-element list
  remains true after `print` returns `None`.

**Notes**

- Exact integer multiplication, with no factorial recomputation or
  division. Only the current term and its index are stored.
- The first distinct multipliers are 1³, 2³, 3³, …; for example,
  the update from 8 to 216 multiplies by 27.
- Cubing a running factorial would need a separate output expression;
  accumulating the cubed factors directly keeps the stored value
  equal to the term being printed.
- Factorial growth eventually reaches Python 3.11+'s default
  4300-digit integer-to-string limit, an interpreter limit.
- The b-file has 101 terms (indices 0 through 100). The bar is the
  whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 36 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000442), CC BY-SA 4.0.
