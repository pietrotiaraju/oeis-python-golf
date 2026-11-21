# A002097

> Numbers that are not the sum of 3 nonzero triangular numbers.
> — [OEIS A002097](https://oeis.org/A002097)

Offset 1: 1, 2, 4, 6, 11, 20, 29 (the entry's full list)

### Python 3 — 98 bytes

```python
n=0
while 1:n+=1;R=range(1,n);all(a*~a+b*~b+c*~c+2*n for a in R for b in R for c in R)and print(n)
```

**How it works**

- **Definition.** The nonzero triangular numbers are T_k = k(k + 1)/2 with
  k ≥ 1 (1, 3, 6, 10, …), and a sum may repeat one (3 = 1 + 1 + 1). n is
  listed when no a, b, c ≥ 1 give T_a + T_b + T_c = n.
- **The test.** `a*~a` is −a(a + 1) = −2T_a, so
  `a*~a+b*~b+c*~c+2*n` is 2(n − T_a − T_b − T_c), zero exactly for a
  representation. `R=range(1,n)` holds every useful index: T_a ≤ n − 2 forces
  a < n. `all(…)` is true when every triple misses, and then `and print(n)`
  prints n. So the program prints exactly the numbers that are not such a
  sum, in increasing order, by the definition alone: n = 1 is printed
  because R is empty.
- **Finite, but not assumed.** The entry lists 1, 2, 4, 6, 11, 20, 29 and
  marks the list complete (keywords fini, full). By Gauss's Eureka theorem
  every n is a sum of three triangular numbers when T_0 = 0 is allowed; with
  all three nonzero, the claim is equivalent to 8n + 3 being a sum of three
  odd squares all larger than 1. The program does not rely on any of this:
  after 29 it keeps testing every n and would print any further exception,
  so it computes the sequence for every n whether or not the list is
  complete.

**Notes**

- The triple loop costs about n³ steps for n; the seven terms come in a
  fraction of a second, and the program then keeps searching silently
  until it is stopped. The bar is the whole b-file, 7 terms, in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-20 | Python 3 | 98 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A002097), CC BY-SA 4.0.
