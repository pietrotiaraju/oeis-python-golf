# A000463

> n followed by n^2.
> — [OEIS A000463](https://oeis.org/A000463)

Offset 1: 1, 1, 2, 4, 3, 9, 4, 16, 5, 25, …

### Python 3 — 35 bytes

```python
n=1
while[print(n),print(n*n)]:n+=1
```

**How it works**

- For n=1,2,3,…, emit the pair n,n². Thus at sequence positions
  2n−1 and 2n the terms are n and n² respectively; the initial
  pair is 1,1 rather than just one occurrence of 1.
- Python evaluates list entries from left to right. Both print calls
  in `[print(n),print(n*n)]` therefore run in the specified order,
  each writing one integer and one newline.
- The resulting list is `[None,None]`, which is nonempty and true.
  Its entries' false values do not matter. The body increments n
  only after both members of the current pair have printed.

**Notes**

- Exact integer multiplication and a single counter; no stored list
  of sequence values or parity test on the output index is needed.
- A single `print(n,n*n)` would put the pair on one line by default,
  violating the one-term-per-line rule. The two print calls also
  provide the loop's always-true condition.
- This interleaves entire integers. It does not split their digits:
  at n=10 the two emitted terms are 10 and 100.
- The b-file has 10000 terms (indices 1 through 10000). The bar is the
  whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 35 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000463), CC BY-SA 4.0.
