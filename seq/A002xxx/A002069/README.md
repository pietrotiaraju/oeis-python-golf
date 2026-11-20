# A002069

> Palindromic pentagonal numbers.
> — [OEIS A002069](https://oeis.org/A002069)

Offset 1: 0, 1, 5, 22, 1001, 2882, 15251, 720027, 7081807, 7451547, 26811862, 54177145, …

### Python 3 — 55 bytes

```python
p=j=0
while 1:s=str(p);j+=3;p+=j-2;s==s[::-1]==print(s)
```

**How it works**

- The pentagonal numbers are k(3k−1)/2 for k = 0, 1, 2, …: 0, 1, 5, 12, …,
  with differences 1, 4, 7, …: `j+=3;p+=j-2` adds 3k + 1 to go from the
  k-th to the (k+1)-th.
- `s==s[::-1]==print(s)` is a chained comparison: `print(s)` runs only when
  the decimal string reads the same backwards. Every pentagonal number is
  visited in increasing order, so the palindromic ones come out in order
  and none is missed.

**Notes**

- Exact integer arithmetic, so the program is right for every n; it is a
  plain search over the pentagonal numbers, about √N steps to reach N.
- The b-file has 58 terms, up to about 1.6·10³⁹, found by smarter
  digit-by-digit searches. Here the 21st term, 264571020175462
  (k ≈ 1.3·10⁷), comes after about 10 s; the 22nd, 5292834004382925, needs
  about 4.6·10⁷ more steps. The bar is 21 terms in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-20 | Python 3 | 55 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A002069), CC BY-SA 4.0.
