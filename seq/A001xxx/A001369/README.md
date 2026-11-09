# A001369

> Blocks of increasing length using 1,2,3,...,9,10; omit leading 0's.
> — [OEIS A001369](https://oeis.org/A001369)

Offset 1: 1, 23, 456, 7891, 1234, 567891, 123456, 78910123, 456789101, …

### Python 3 — 62 bytes

```python
n=t=0
while 1:n+=1;print(int(('12345678910'*n*n)[t:t+n]));t+=n
```

**How it works**

- **The digit string.** Writing 1, 2, …, 9, 10 over and over gives the
  periodic string 12345678910 12345678910 …, period 11 (this is how the
  entry's PARI program and the data read the title: after 10 the count
  starts again at 1). a(n) is its n-th block, of n digits, read as a
  number, so a leading 0 drops out (a(5) = 01234 → 1234).
- **The block.** The first n − 1 blocks use t = n(n − 1)/2 digits, so
  block n is the slice `[t:t+n]`. The string is repeated n² times, 11n²
  digits, which is more than t + n = n(n + 1)/2 for every n ≥ 1.
- `int(…)` drops leading zeros; `t+=n` moves to the next block.
- The literal `'12345678910'` is the definition itself, the numbers 1 to 10
  written one after another; its first ten digits are also a(1) to a(4),
  which is why the program went through a review. Building the string
  instead, as `'%d'*10%(*range(1,11),)`, costs 10 bytes.

**Notes**

- Exact for every n. a(n) has n digits, so from n = 4301 on `print` hits
  Python's 4300-digit int-to-str limit (`ValueError`), an interpreter
  limit; the b-file ends at n = 200.
- The bar is the whole b-file (200 terms) in 60 s, which takes a fraction
  of a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 62 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001369), CC BY-SA 4.0.
