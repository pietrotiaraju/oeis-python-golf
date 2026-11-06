# A000439

> Powers of rooted tree enumerator.
> — [OEIS A000439](https://oeis.org/A000439)

Offset 1: 9, 30, 69, 133, 230, 369, 560, 814, 1143, 1560, …

### Python 3 — 51 bytes

```python
n=1
while 1:print(n*(n*(n*(n+18)+83)+114)//24);n+=1
```

**How it works**

Evaluate the quartic formula given by the OEIS,
a(n)=(n⁴+18n³+83n²+114n)/24, using Horner's rule.
The numerator is divisible by 24 for every positive integer n.

**Notes**

- The program uses exact integer arithmetic and the standard library only.
- The verification bar is 43 terms in 60 s; the official b-file contains 43 terms.


## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 51 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000439), CC BY-SA 4.0.
