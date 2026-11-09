# A001414

> Integer log of n: sum of primes dividing n (with repetition). Also called sopfr(n).
> — [OEIS A001414](https://oeis.org/A001414)

Offset 1: 0, 2, 3, 4, 5, 5, 7, 6, 6, 7, 11, 7, 13, 9, 8, 8, 17, 8, 19, 9, 10, …

### Python 3 — 71 bytes

```python
l=[n:=1,0]
while[print(l[n])]:
 n+=1;d=2
 while n%d:d+=1
 l+=l[n//d]+d,
```

**How it works**

- sopfr is completely additive: if d is a prime dividing n, then
  sopfr(n) = sopfr(n/d) + d. The smallest d ≥ 2 that divides n is always
  prime, and for a prime n it is n itself, with sopfr(1) = 0.
- `l` stores sopfr(k) at index k (index 0 holds a dummy 1 that is never
  read, so the start `l=[n:=1,0]` also sets n = 1). Each pass prints
  l[n] = a(n), moves to n + 1, finds its least divisor d ≥ 2 with
  `while n%d:d+=1`, and appends `l[n//d]+d`.
- Exact integer arithmetic, so the program is right for every n.

**Notes**

- The search costs about p steps for a prime p, so the running time grows
  like n²/log n. The b-file has 100000 terms; the bar is the first 50000
  in 60 s. Stopping the search at √n would be faster but costs about 11
  bytes.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 71 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001414), CC BY-SA 4.0.
