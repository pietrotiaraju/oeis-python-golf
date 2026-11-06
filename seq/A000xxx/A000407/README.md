# A000407

> a(n) = (2*n+1)! / n!.
> — [OEIS A000407](https://oeis.org/A000407)

Offset 0: 1, 6, 60, 840, 15120, 332640, 8648640, 259459200, 8821612800, 335221286400, …

### Python 3 — 33 bytes

```python
a=1;k=6
while[print(a)]:a*=k;k+=4
```

**How it works**

The factorial ratio a(n) = (2n+1)!/n! satisfies a(0) = 1 and
a(n+1) = (4n+6)a(n). The state `k` visits 6, 10, 14, … and
`a` is multiplied by the next factor after each print.
`[print(a)]` is a nonempty list, so the loop continues indefinitely.

**Notes**

- The program uses exact integer arithmetic and the standard library only.
- The verification bar is 101 terms in 60 s; the official b-file contains 101 terms.
- Python 3.11+ eventually stops at its default 4300-digit integer-to-string limit; this interpreter limit is not counted as a correctness failure.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 33 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000407), CC BY-SA 4.0.
