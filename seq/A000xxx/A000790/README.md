# A000790

> Primary pretenders: least composite c such that n^c == n (mod c).
> — [OEIS A000790](https://oeis.org/A000790)

Offset 0: 4, 4, 341, 6, 4, 4, 6, 6, 4, 4, 6, 10, 4, 4, 14, 6, 4, 4, 6, 6, …

### Python 3 — 66 bytes

```python
n=0
while 1:
 c=4;P=12
 while(n**c-n+P)%c:P*=c;c+=1
 print(c);n+=1
```

**How it works**

- For each n the inner loop walks c = 4, 5, 6, … and stops at the first c
  with c | nᶜ − n + P, where `P` = 2·(c−1)! (it starts at 12 = 2·3! and
  `P*=c` keeps it up to date).
- That single test does both jobs. For composite c, c | 2·(c−1)!: c = 4
  divides 12, and a composite c ≥ 6 divides (c−1)! (if c = ab with
  1 < a < b both factors are below c; if c = a² with a ≥ 3, so are a and
  2a). So P drops out and the test is c | nᶜ − n, the definition. For a
  prime c ≥ 5, Fermat gives nᶜ ≡ n and Wilson gives 2·(c−1)! ≡ −2, so
  the sum is ≡ −2 ≢ 0 and primes are always skipped, with no primality
  test.
- The search always ends by c = 561: 561 = 3·11·17 is a Carmichael number
  (squarefree, and 2, 10 and 16 all divide 560), so n⁵⁶¹ ≡ n (mod 561)
  for every n.

**Notes**

- Exact integer arithmetic; the facts used are Fermat's little theorem,
  Wilson's theorem and Korselt's criterion (only for termination).
- The whole b-file (10001 terms) takes well under a second; the bar is
  the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 66 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000790), CC BY-SA 4.0.
