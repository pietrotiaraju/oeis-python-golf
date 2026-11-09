# A001318

> Generalized pentagonal numbers: m*(3*m - 1)/2, m = 0, +-1, +-2, +-3, ....
> — [OEIS A001318](https://oeis.org/A001318)

Offset 0: 0, 1, 2, 5, 7, 12, 15, 22, 26, 35, 40, 51, 57, 70, 77, 92, 100, …

### Python 3 — 34 bytes

```python
k=1
while[print(k*k//24)]:k+=4*k%6
```

**How it works**

- m(3m − 1)/2 = ((6m − 1)² − 1)/24. As m runs through 0, 1, −1, 2, −2, …,
  6m − 1 runs through −1, 5, −7, 11, −13, …, so j = |6m − 1| runs through
  1, 5, 7, 11, 13, …: every positive integer prime to 6, once each and in
  increasing order (6i − 1 comes from m = i, 6i + 1 from m = −i). The terms
  (j² − 1)/24 then increase too, which is the order of the entry.
- For j prime to 6, j² ≡ 1 (mod 24) (j² ≡ 1 mod 8 for odd j, and mod 3 for
  j not divisible by 3), so `k*k//24` is exactly (j² − 1)/24.
- The step `k+=4*k%6` walks the numbers prime to 6: if k ≡ 1 (mod 6), then
  4k ≡ 4 and k + 4 ≡ 5; if k ≡ 5 (mod 6), then 4k ≡ 2 and k + 2 ≡ 1. Both
  times it lands on the next number prime to 6, so from k = 1 it visits
  1, 5, 7, 11, 13, … with none skipped.
- `print` returns `None` and `[None]` is a non-empty list, so the loop never
  ends.

**Notes**

- The same frame as the pentagonal numbers [A000326](../../A000xxx/A000326/)
  (`m*m//24` with `m-=6`). A search over steps `k+=E`, `k-=E`, `k^=E`,
  `k|=E`, `k*=E` and `k=E`, with E up to 5 characters of digits, `k`,
  brackets and `+ - * % ^ | & ~ < >`, and starts from −12 to 12, found only
  `4*k%6` and `k*4%6` from k = 1, plus 35-byte forms from k = −1 such as
  `k-=k%3*2`.
- Also 35 bytes: `k=1` + `while[print((k|1)**2//24)]:k+=3` (the n-th number
  prime to 6 is (3n + 1) | 1), and the steps `k+=-k%3*2` and `k+=8>>k%3`.
  Following m itself, `m=0` + `while[print(3*m*m-m>>1)]:m=(m<1)-m`, is 38;
  the differences n (n odd) and n/2 (n even) from the entry,
  `a=n=0` + `while[print(a)]:n+=1;a+=n>>1-n%2`, are 38; filtering with
  `k*k%24==1==print(k*k//24)` is 42.
- The b-file has 1001 terms (n = 0 to 1000); the bar is the whole b-file in
  60 s, which takes a fraction of a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 34 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001318), CC BY-SA 4.0.
