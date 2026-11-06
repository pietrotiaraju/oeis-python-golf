# A000353

> Primes p == 7, 19, 23 (mod 40) such that (p-1)/2 is also prime.
> — [OEIS A000353](https://oeis.org/A000353)

Offset 1: 7, 23, 47, 59, 167, 179, 263, 383, 503, 863, 887, 983, 1019, …

### Python 3 — 74 bytes

```python
P=k=1;s={0}
while 1:s|={P%k*k};{k,k//2,k*7%40>20}<=s==print(k);P*=k*k;k+=1
```

**How it works**

- Wilson's theorem, as in [A000006](../A000006/): with P = ((k − 1)!)²,
  P mod k is 1 when k is prime and 0 otherwise, so `s|={P%k*k}` adds k to
  the set `s` exactly when k is prime (and adds 0 otherwise). So at step k,
  `s` is 0 together with the primes up to k, and never contains 1.
- The test is one subset check, `{k,k//2,k*7%40>20}<=s`: k is prime,
  k//2 = (k − 1)/2 is prime, and the residue test is `False` (0, which is
  in `s`) rather than `True` (1, which is not). The chained `==print(k)`
  prints only when the subset test holds.
- Why `k*7%40>20` is false exactly on 7, 19, 23 (mod 40) here: if q = (p − 1)/2
  and p are both prime with q > 5, then q is odd and prime to 5, so
  p = 2q + 1 is 3, 7, 15, 19, 23, 27, 35 or 39 (mod 40), and 15 and 35
  would make p a multiple of 5. On the six residues left, 7r mod 40 is
  9, 13, 1 for r = 7, 19, 23 and 21, 29, 33 for r = 3, 27, 39. The small
  cases q = 2, 3, 5 give p = 5, 7, 11, with 7p mod 40 = 35, 9, 37: only 7
  passes, as it should.

**Notes**

- Exact integers; correctness for every n rests on Wilson's theorem.
- A search over k·M mod A compared with a constant, and over k mod A, k·M
  mod A combined with +, −, ^, //, % or a shift as the third element of
  the set, found nothing shorter than the 9 characters of `k*7%40>20`
  (`k*9%40//3` ties).
- The same in a `while[…]` condition with `s:=s|{…}` is 75 bytes;
  multiplying the subset test by the residue test,
  `({k,k//2}<=s)*k*27%40>19`, is 77.
- The factorial makes each step cost time proportional to k log k, so the
  program prints about 305 terms (up to 91943) in 60 s. The bar is 230
  terms (up to 66047); the b-file has 1000 terms (up to 390263).

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 74 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000353), CC BY-SA 4.0.
