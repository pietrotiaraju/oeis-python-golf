# A000337

> a(n) = (n-1)*2^n + 1.
> — [OEIS A000337](https://oeis.org/A000337)

Offset 0: 0, 1, 5, 17, 49, 129, 321, 769, 1793, 4097, 9217, 20481, …

### Python 3 — 33 bytes

```python
n=0
while[print((n-1<<n)+1)]:n+=1
```

**How it works**

- The [A000027](../A000027/) counter, printing the closed form.
- `-` binds tighter than `<<`, so `n-1<<n` is (n − 1)·2^n. Python's shifts
  act on the two's-complement value with infinite sign bits, so at n = 0 it is
  −1 << 0 = −1 and the term is 0, as it should be.

**Notes**

- `n-1<<n|1` would save 3 bytes, since (n − 1)·2^n is even for n ≥ 1, but at
  n = 0 it gives −1 | 1 = −1 instead of 0, and no `|` or `^` can turn −1 into
  0. `-~(n-1<<n)` and `1-(1-n<<n)` are also 10 bytes.
- The recurrence a(n) = 2·a(n−1) + 2^n − 1 with q = 2^n − 1 stepped by
  `q-=~q`, `a=q=0` + `while[print(a:=a+a+q)]:q-=~q`, is 34 bytes; summing
  a(n) − a(n−1) = n·2^(n−1) as `a+=n<<n-1` is 36.
- Exact integers, so every term is right. a(14271) is the first term with more
  than 4300 digits, so Python 3.11+ stops there with a `ValueError` from the
  int-to-str limit, which is not counted as a failure.
- The b-file has 1001 terms (n = 0 to 1000) and prints at once; the bar is the
  whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 33 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000337), CC BY-SA 4.0.
