# A000340

> a(0)=1, a(n) = 3*a(n-1) + n + 1.
> — [OEIS A000340](https://oeis.org/A000340)

Offset 0: 1, 5, 18, 58, 179, 543, 1636, 4916, 14757, 44281, 132854, …

### Python 3 — 34 bytes

```python
a=n=1
while[print(a)]:n+=1;a=3*a+n
```

**How it works**

- The recurrence as it is written, with `n` kept one ahead of the index: when
  `a` = a(k) is printed, `n` = k + 1, so after `n+=1` the step `a=3*a+n` is
  3·a(k) + (k + 1) + 1 = a(k + 1).
- Starting both at 1 sets a(0) = 1 and the counter in one assignment.

**Notes**

- Starting one step early is also 34 bytes: the recurrence gives a(−1) = 0,
  so `a=n=0` + `while[print(a:=3*a-~n)]:n+=1` works, with `-~n` = n + 1.
- Keeping the difference d(k) = a(k) − a(k−1) = (3^(k+1) − 1)/2, which obeys
  d → 3d + 1, gives `a=d=1` + `while[print(a)]:d=3*d+1;a+=d`, 34 bytes again.
  The closed form a(n) = (3^(n+2) − 2n − 5)/4 needs a counter and a power and
  is longer.
- Exact integers, so every term is right. a(9012) is the first term with more
  than 4300 digits, so Python 3.11+ stops there with a `ValueError` from the
  int-to-str limit, which is not counted as a failure.
- The b-file has 1001 terms (n = 0 to 1000) and prints at once; the bar is the
  whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 34 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000340), CC BY-SA 4.0.
