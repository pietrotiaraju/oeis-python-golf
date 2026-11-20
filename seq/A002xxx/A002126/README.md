# A002126

> Number of solutions to n=p+q where p and q are primes or zero.
> — [OEIS A002126](https://oeis.org/A002126)

Offset 0: 1, 0, 2, 2, 1, 4, 1, 4, 2, 2, 3, 2, …

### Python 3 — 69 bytes

```python
z=[1];P=n=1
while[print(sum(map(min,z,z[::-1])))]:z+=P%n,;P*=n*n;n+=1
```

**How it works**

- The g.f. is (1 + Σ_p x^p)², so a(n) = Σ_{k=0..n} z(k)·z(n−k) with
  z(0) = 1, z(k) = 1 for prime k and 0 otherwise: ordered pairs (p, q),
  each a prime or 0, with p + q = n.
- `z` holds z(0), …, z(n), and `P` is ((n−1)!)² before the append; by
  Wilson's theorem `P%n` is 1 when n is prime and 0 when it is not (n = 1
  gives 1 % 1 = 0; n = 4 gives 36 % 4 = 0), so `z+=P%n,` appends z(n).
- The values are 0 and 1, so the product z(k)·z(n−k) is their minimum:
  `sum(map(min,z,z[::-1]))` pairs z(k) with z(n−k) in C.
- `while[print(…)]:` prints a(n) from the list z(0…n) before z(n+1) is
  appended; a one-element list is always true.

**Notes**

- Exact integer arithmetic, so the program is right for every n.
- O(n) per term in C; the b-file has 10001 terms (n = 0…10000) and the
  bar is all of them in 60 s, about 9 s here.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-20 | Python 3 | 69 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A002126), CC BY-SA 4.0.
