# A001651

> Numbers not divisible by 3.
> — [OEIS A001651](https://oeis.org/A001651)

Offset 1: 1, 2, 4, 5, 7, 8, 10, 11, 13, 14, 16, 17, 19, 20, 22, 23, 25, 26, …

### Python 3 — 26 bytes

```python
n=1
while[print(n)]:n+=n%3
```

**How it works**

- From n ≡ 1 (mod 3), `n+=n%3` adds 1 and reaches n ≡ 2; from there it
  adds 2, jumping over the multiple of 3 to the next n ≡ 1. Starting at 1
  this lists exactly the numbers not divisible by 3, in order.

**Notes**

- The closed form (3n − 1)//2 as a stride, `n=2` / `print(n//2)` /
  `n+=3`, is 27 bytes; the filter `n%3and print(n)` is 31.
- The b-file has 10000 terms; the bar is the whole b-file, printed in under
  a second. Correct for every n.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-13 | Python 3 | 26 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001651), CC BY-SA 4.0.
