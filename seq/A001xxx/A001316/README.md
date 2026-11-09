# A001316

> Gould's sequence: a(n) = Sum_{k=0..n} (binomial(n,k) mod 2); number of odd entries in row n of Pascal's triangle (A007318); a(n) = 2^A000120(n).
> — [OEIS A001316](https://oeis.org/A001316)

Offset 0: 1, 2, 2, 4, 2, 4, 4, 8, 2, 4, 4, 8, 4, 8, 8, 16, 2, …

### Python 3 — 39 bytes

```python
n=0
while[print(2**n.bit_count())]:n+=1
```

**How it works**

- By Lucas's theorem, C(n,k) is odd exactly when every binary digit of k
  is at most the matching digit of n. So k may have each 1-bit of n set or
  not, and nothing else: row n has 2^s odd entries, where s is the number
  of 1's in the binary expansion of n ([A000120](../../A000xxx/A000120/)).
- `int.bit_count()` (Python 3.10+) counts those 1's, as in the A000120
  record, and `2**` turns the count into a(n).
- `print(…)` runs in the loop condition: it returns `None`, and `[None]` is
  a non-empty list, so the loop never ends.

**Notes**

- `1<<n.bit_count()` is the same length. The entry's recurrence
  a(n) = 2·a(n−1)/(n & −n), with n & −n the largest power of 2 dividing n
  (A006519), is 40 bytes: `a=n=1` / `while[print(a)]:a=a*2//(n&-n);n+=1`.
  Zumkeller's self-similar list (a(2n) = a(n), a(2n+1) = 2a(n)) as a list
  that grows while it is read, `a=[2]` / `for x in a:print(x);a+=x,x*2`,
  needs a(0) printed apart and is 43 bytes.
- The b-file has 50001 terms (n = 0 to 50000); the bar is the whole
  b-file in 60 s, which takes under a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 39 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001316), CC BY-SA 4.0.
