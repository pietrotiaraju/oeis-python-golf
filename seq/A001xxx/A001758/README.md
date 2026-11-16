# A001758

> Number of quasi-alternating permutations of length n.
> — [OEIS A001758](https://oeis.org/A001758)

Offset 2: 0, 2, 12, 58, 300, 1682, 10332, 69298, 505500, 3990362, 33925452, 309248938, …

### Python 3 — 68 bytes

```python
r=[0,2,2]
while 1:s=0;r=[s:=s+x for x in[0]+r[::-1]];print(s-2*r[1])
```

**How it works**

- **Runs.** A "sequence" here is an alternating run: a maximal increasing or
  decreasing stretch of the permutation, so 3 1 2 5 4 has the runs 3 1,
  1 2 5 and 5 4. Let R(n, k) count the permutations of [n] with k runs. A
  permutation of [n] has at most n − 1 runs, so R(n, n) = 0, and a
  quasi-alternating permutation has n − 2 runs: a(n) = R(n, n − 2).
- **André's recurrence.** Inserting n into a permutation of [n − 1] gives
  R(n, k) = k·R(n − 1, k) + 2·R(n − 1, k − 1) + (n − k)·R(n − 1, k − 2)
  (D. André, 1884; F. N. David and D. E. Barton, *Combinatorial Chance*,
  1962). Take n + 1 for n and k = n: since R(n, n) = 0,
  R(n + 1, n) = 2·R(n, n − 1) + R(n, n − 2), so
  a(n) = R(n + 1, n) − 2·R(n, n − 1).
- **Alternating permutations.** n − 1 runs means every run has length 2,
  i.e. the permutation alternates up and down. There are 2Eₙ of them for
  n ≥ 2, Eₙ the Euler zigzag numbers ([A000111](../../A000xxx/A000111/)), so
  a(n) = 2Eₙ₊₁ − 4Eₙ for n ≥ 2, the formula [A001250](../A001250/)(n + 1) − 2·A001250(n) on
  the OEIS page.
- **Seidel's boustrophedon.** Each row is the running sum of a 0 followed by
  the previous row reversed: `s=0;r=[s:=s+x for x in[0]+r[::-1]]`. Row n
  holds the Entringer numbers E(n, 0…n) and ends in Eₙ, so after the step
  `s` is the new Eₙ₊₁ and `r[1]`, the old last entry, is Eₙ. The triangle is
  linear, so the program starts from row 2 doubled, `[0,2,2]`, and prints
  `s-2*r[1]` = 2Eₙ₊₁ − 4Eₙ, beginning with a(2) = 0.

**Notes**

- Running André's recurrence over the whole triangle and reading
  R(n, n − 2) is 95 bytes:
  `r=[0,n:=2,0,0]` / `while[print(r[-4])]:n+=1;r=[k*r[k]+2*r[k-1]+(n-k)*r[k-2]for k in range(n)]+[0,0]`
  (two trailing zeros let `r[k-1]` and `r[k-2]` wrap round to 0 at k = 0, 1).
  That is the template of [A001759](../A001759/) and [A001760](../A001760/),
  where the reduction to zigzag numbers keeps a factor n.
- Exact integer arithmetic, so the program is right for every n.
- The b-file has 99 terms (n = 2 to 100); the bar is the whole b-file in
  60 s, which takes well under a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-16 | Python 3 | 68 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001758), CC BY-SA 4.0.
