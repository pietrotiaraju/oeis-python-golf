# A000461

> Concatenate n n times.
> — [OEIS A000461](https://oeis.org/A000461)

Offset 1: 1, 22, 333, 4444, 55555, 666666, 7777777, 88888888, 999999999, 10101010101010101010, …

### Python 3 — 32 bytes

```python
n=0
while 1:n+=1;print(str(n)*n)
```

**How it works**

Multiplying the decimal string of n by n concatenates exactly n
copies. Start at n=1; strings preserve every digit without requiring
conversion of the growing output to a Python integer.

**Notes**

- The program uses exact integer arithmetic and the standard library only.
- The verification bar is 333 terms in 60 s; the official b-file contains 333 terms.


## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 32 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000461), CC BY-SA 4.0.
