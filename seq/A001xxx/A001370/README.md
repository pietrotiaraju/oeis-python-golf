# A001370

> Sum of digits of 2^n.
> — [OEIS A001370](https://oeis.org/A001370)

Offset 0: 1, 2, 4, 8, 7, 5, 10, 11, 13, 8, 7, 14, 19, 20, 22, 26, 25, 14, …

### Python 3 — 43 bytes

```python
n=1
while[print(sum(map(int,str(n))))]:n*=2
```

**How it works**

n runs through the powers of 2, and `sum(map(int,str(n)))` adds the
decimal digits of n. `while[print(…)]:` prints the term and is always
true, since the list is never empty; the body doubles n.

**Notes**

- Exact for every n, but 2^n has more than 4300 digits from n = 14285 on,
  where `str` raises Python's int-to-str limit (`ValueError`), an
  interpreter limit; the b-file ends at n = 10000 (3011 digits).
- `eval('+'.join(str(n)))` is 2 bytes longer than the `sum(map(…))`.
- The bar is the whole b-file (10001 terms) in 60 s, which takes a few
  seconds.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 43 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001370), CC BY-SA 4.0.
