# A000005

> d(n) (also called tau(n) or sigma_0(n)), the number of divisors of n.
> — [OEIS A000005](https://oeis.org/A000005)

Offset 1: 1, 2, 2, 3, 2, 4, 2, 4, 3, 4, 2, 6, 2, 4, 4, 5, …

### Python 3 — 52 bytes

```python
n=1
while[print(sum(n%-~k<1for k in range(n)))]:n+=1
```

**How it works**

- Counts the k from 1 to n that divide n.
- `-~k` is k+1, so `range(n)` runs the divisor candidate over 1…n and saves
  the 2 bytes of `range(1,n+1)`.
- `n%-~k<1` is a bool, and `sum` counts the `True`s.
- `while[print(...)]:` prints in the loop condition: `[None]` is a non-empty
  list, so it is true, and it saves a byte over `while 1:print(...);`
  (`n+=1` moves into the loop body).

**Notes**

- `1for` makes Python 3.12 print a `SyntaxWarning` on stderr, which the rules
  ignore; a space would cost a byte.
- Each term costs n steps: about 18 000 terms a minute. The bar for this
  sequence is 10 000 terms in 60 s.
- Other shapes tried: `range(1,n+1)` with `n%k<1` (54 bytes); negative
  divisors, `n%k>-1for k in range(-n,0)` (54).

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 53 | first entry |
| 2026-11-05 | Python 3 | 52 | `while[print(...)]:` loop |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000005), CC BY-SA 4.0.
