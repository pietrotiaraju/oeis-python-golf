# A001348

> Mersenne numbers: 2^p - 1, where p is prime.
> — [OEIS A001348](https://oeis.org/A001348)

Offset 1: 3, 7, 31, 127, 2047, 8191, 131071, 524287, 8388607, 536870911, …

### Python 3 — 45 bytes

```python
P=k=1
while[-P%k==1==print(2**k-1)]:P*=k;k+=1
```

**How it works**

- The prime loop of [A000040](../../A000xxx/A000040/), printing 2ᵏ − 1
  instead of k. Wilson's theorem: k ≥ 2 is prime exactly when
  (k − 1)! ≡ −1 (mod k).
- `P` is kept equal to (k − 1)!: it starts at 0! = 1, and `P*=k;k+=1` turns
  (k − 1)! into k! as k moves on. At k = 1 every number is 0 mod 1, so 1 is
  skipped; at k = 4, 3! = 6 ≡ 2 (mod 4) fails as it should.
- The chained comparison `-P%k==1==print(2**k-1)` means
  `-P%k==1 and 1==print(2**k-1)`, so the print runs only for prime k, in
  increasing order. The list around it is non-empty, so the loop never
  stops. All composite exponents are skipped and all primes are kept, so
  2047 = 23 · 89 (p = 11) is a term, as in the entry.

**Notes**

- Also 45 bytes: `P=k=1` + `while[P%k>0==print(2**k-1)]:P*=k*k;k+=1`
  ((k − 1)!² mod k is 1 for primes, 0 otherwise) and `P=k=1` +
  `while k:=k+1:~P%k or print(2**k-1);P*=k`. Keeping M = 2ᵏ − 1 in a
  variable (`M-=~M`) is 48.
- A test on M alone, `pow(2,M,M)==2`, is wrong: 2 has order k mod M, so it
  holds exactly when k divides 2ᵏ − 2, and the pseudoprime k = 341 passes.
- 2ᵖ − 1 has more than 4300 digits from p = 14293 on (the 1677th term,
  4303 digits), where the int-to-str limit of Python 3.11+ stops the
  program with a `ValueError`.
- The b-file has 100 terms (p up to 541, 163 digits); the bar is the whole
  b-file in 60 s, which takes a fraction of a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 45 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001348), CC BY-SA 4.0.
