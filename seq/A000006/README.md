# A000006

> Integer part of square root of n-th prime.
> — [OEIS A000006](https://oeis.org/A000006)

Offset 1: 1, 1, 2, 2, 3, 3, 4, 4, 4, 5, 5, 6, 6, 6, 6, 7, 7, 7, 8, …

### Python 3 — 57 bytes

```python
k=P=s=1
while 1:P%k and print(s);P*=k*k;k+=1;s+=s*(s+2)<k
```

**How it works**

- Primes come from the code-golf classic based on Wilson's theorem: `P` is
  ((k−1)!)², and P mod k is 1 when k is prime and 0 otherwise. Squaring
  handles k = 4, where 3! = 6 is not a multiple of 4 but 36 is; for k = 1,
  1 mod 1 = 0.
- `s` stays equal to ⌊√k⌋ with exact integers: k grows by 1 per step, so s
  grows by at most 1, exactly when (s+1)² ≤ k, that is s(s+2) < k.
- `P%k and print(s)` prints only at primes.

**Notes**

- `int(k**.5)` instead of tracking `s` is 51 bytes, but the float square root
  is wrong for large k (just below a big square it rounds up, and past 10³⁰⁸
  it overflows), so it breaks the exact-arithmetic rule.
- `math.isqrt(k)` is exact but costs 67 bytes with the import.
- `P` grows like (k!)², so the program slows down: about 8300 terms a minute.
  The bar for this sequence is 5000 terms in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 57 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000006), CC BY-SA 4.0.
