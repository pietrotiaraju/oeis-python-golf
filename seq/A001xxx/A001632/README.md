# A001632

> Smallest prime p such that there is a gap of 2n between p and previous prime.
> — [OEIS A001632](https://oeis.org/A001632)

Offset 1: 5, 11, 29, 97, 149, 211, 127, 1847, 541, 907, …

a(n) is the prime that ends the first gap of exactly 2n between consecutive
primes, so a(n) = [A000230](../A000230/)(n) + 2n: the gap 3 → 5 gives
a(1) = 5, the gap 113 → 127 gives a(7) = 127. The terms are not increasing,
so each one needs its own search.

### Python 3 — 72 bytes

```python
m=0
while m:=m+2:
 P=k=p=1
 while(g:=p*P%k)-m:p+=g;P*=k;k+=1
 print(p+m)
```

**How it works**

- m = 2n is the gap being looked for (2, 4, 6, …, from `while m:=m+2`).
- Each search restarts at k = 1 with P = (k−1)! and p = the last prime below
  k (p = 1 stands in before 2). Wilson's theorem gives P ≡ −1 (mod k) for a
  prime k, so `p*P%k` is −p mod k = k − p, the gap from the previous prime.
  For a composite k > 4, k divides (k−1)!, so it is 0. `p+=g` then moves p
  to k exactly when k is prime, with no prime test of its own.
- The one exception is k = 4: 3!·3 = 18 ≡ 2 (mod 4), so the gap 3 → 5 is
  reported one step early (at k = 4 instead of 5), p jumps to 5, and at
  k = 5 the value is 5·4! ≡ 0. The gaps still come out once each and in
  order, each with the right previous prime p.
- The sentinel gives a fake gap 1 at k = 2, and 2 → 3 is the real gap 1; m
  is even, so neither can stop the search. The first k with g = m ends it:
  p is then the smallest prime followed by a gap of exactly m, and the
  printed p + m is the prime that ends it (5 for m = 2, even though k is
  still 4 there). That is the same search as A000230, printing the other
  end of the gap.

**Golf notes**

- Printing k, the prime where the search stops, would be 2 bytes shorter
  but wrong for n = 1, where the early report at k = 4 stops the search;
  p + m is right every time.
- A000230's `while[print(p)]` trick needs a term to print before the first
  search; with offset 1 there is none, so the print goes after the search.

**Notes**

- The rule is the definition itself: primality comes from Wilson's theorem,
  exact for every k, and the scan visits every number in order, so the
  first gap of size m found is the first one there is.
- If some even number were never a gap between consecutive primes, a(n)
  would not exist and the program would search forever at that n; whether
  every even number occurs as a gap is open (de Polignac's conjecture says
  infinitely often). All 595 terms in the b-file exist.
- Every term restarts the scan, and (k−1)! grows to hundreds of thousands
  of digits, so the time goes with the largest a(n) so far: a(22) = 15727
  comes after about 13 s here, a(23) = 81509 after about 56 s, and the next
  few small terms right after it.
- The b-file has 595 terms (a(1) to a(595), from Nicely's tables); the bar
  is 22 terms (up to a(22)) in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-13 | Python 3 | 72 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001632), CC BY-SA 4.0.
