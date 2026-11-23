# A002203

> Companion Pell numbers: a(n) = 2*a(n-1) + a(n-2), a(0) = a(1) = 2.
> — [OEIS A002203](https://oeis.org/A002203)

Offset 0: 2, 2, 6, 14, 34, 82, 198, 478, 1154, 2786, 6726, 16238, 39202, 94642, …

### Python 3 — 33 bytes

```python
a=b=2
while[print(a)]:a,b=b,a+2*b
```

**How it works**

- The definition itself: the pair (a, b) holds two consecutive terms,
  `a=b=2` sets both seeds at once, and `a,b=b,a+2*b` moves the pair one
  place. These are (1 + √2)ⁿ + (1 − √2)ⁿ, twice the Pell–Lucas numbers of
  [A001333](../../A001xxx/A001333/), whose program is the same with
  seeds 1.
- `print` returns `None` and `[None]` is a non-empty list, so the loop
  never ends. Exact integers, so it is right for every n.

**Notes**

- `a,b=b,a+b+b` and the walrus step `b+=a+(a:=b)` are also 33 bytes.
- a(n) grows like (1 + √2)ⁿ, so the terms pass the 4300-digit
  int-to-str limit of Python 3.11+ at n = 11234, where the program stops
  with a `ValueError`.
- The b-file has 1001 terms (n = 0 to 1000); the bar is the whole b-file
  in 60 s, which takes a fraction of a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-23 | Python 3 | 33 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A002203), CC BY-SA 4.0.
