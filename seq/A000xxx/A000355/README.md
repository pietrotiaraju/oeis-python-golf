# A000355

> Primes p == 3, 9, 11 (mod 20) such that 2p+1 is also prime.
> — [OEIS A000355](https://oeis.org/A000355)

Offset 1: 3, 11, 23, 29, 83, 89, 131, 191, 251, 431, 443, 491, 509, …

### Python 3 — 77 bytes

```python
P=k=1;s={0}
while 1:s|={P%k*k};{k,k//2,k*7%40>20}<=s==print(k//2);P*=k*k;k+=1
```

**How it works**

- p ≡ 3, 9, 11 (mod 20) exactly when 2p + 1 ≡ 7, 19, 23 (mod 40), so the
  terms are (k − 1)/2 for the terms k of [A000353](../A000353/), in the
  same order. The program is that one, printing `k//2` instead of k.
- Wilson's theorem: with P = ((k − 1)!)², P mod k is 1 for prime k and 0
  otherwise, so `s|={P%k*k}` keeps in `s` the primes up to k, plus 0 and
  never 1.
- `{k,k//2,k*7%40>20}<=s` holds when k = 2p + 1 and p = k//2 are prime and
  the residue test is `False` (0). [A000353](../A000353/) shows that, for
  such pairs, 7k mod 40 is at most 20 exactly when k ≡ 7, 19, 23 (mod 40)
  (the pairs p = 2, 3, 5 included), and the chained `==print(k//2)` prints
  p only then.

**Notes**

- Exact integers; correctness for every n rests on Wilson's theorem.
- Naming p with an unparenthesized walrus in the set,
  `{k,q:=k//2,…}` and `print(q)`, is also 77 bytes. Testing p first would
  need the primality of 2p + 1 ahead of the loop, that is a second
  factorial.
- The program prints about 304 terms (up to 45569) in 60 s. The bar is
  230 terms (up to 33023); the b-file has 1000 terms (up to 195131).

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 77 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000355), CC BY-SA 4.0.
