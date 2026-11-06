# A000566

> Heptagonal numbers (or 7-gonal numbers): n*(5*n-3)/2.
> — [OEIS A000566](https://oeis.org/A000566)

Offset 0: 0, 1, 7, 18, 34, 55, 81, 112, 148, 189, …

### Python 3 — 35 bytes

```python
n=0
while[print(n*(5*n-3)//2)]:n+=1
```

**How it works**

- Evaluate the heptagonal-number formula n(5n−3)/2 from n=0.
  If n is even the first factor is even; if n is odd, 5n−3 is even.
  Thus the division by 2 is always exact.
- Printing inside a nonempty list keeps the loop running, since the
  list is true even though `print` itself returns `None`. Incrementing
  n then visits each successive polygonal layer.

**Notes**

- All operations are on integers, and every stated division is exact.
- Python 3.11+ can eventually reach its integer-to-string conversion limit.
- The reference file contains 10001 terms from the OEIS b-file; the verification
  bar is 10001 terms in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 35 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000566), CC BY-SA 4.0.
