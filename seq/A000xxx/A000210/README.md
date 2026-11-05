# A000210

> A Beatty sequence: floor(n*(e-1)).
> — [OEIS A000210](https://oeis.org/A000210)

Offset 1: 1, 3, 5, 6, 8, 10, 12, 13, 15, 17, …

### Python 3 — 44 bytes

```python
n=M=F=1
while[print(M//F)]:F*=n;n+=1;M=M*n+1
```

**How it works**

- Let S_K = 1/0! + 1/1! + … + 1/K!. For K ≥ n the truncated series
  already gives the right floor: ⌊n·e⌋ = ⌊n·S_K⌋. Proof: K!·e = K!·S_K + r
  with 0 < r = 1/(K+1) + 1/((K+1)(K+2)) + … < 1/K, so
  n·e = n·S_K + n·r/K!. Since n divides K!, n·S_K is a fraction with
  denominator K!/n, so the next integer above it is at least n/K! away,
  and the step n·r/K! is smaller than that. Nothing in between: the floors
  agree.
- Take K = n and drop the n·1/0! term: a(n) = ⌊n·(S_n − 1)⌋ = M/(n−1)!
  rounded down, where M = n!·(S_n − 1) = n!/1! + n!/2! + … + n!/n! is an
  integer with M(n) = n·M(n−1) + 1.
- The loop keeps M and F = (n−1)! together: `F*=n` runs with the old n,
  `M=M*n+1` with the new one. `while[print(…)]:` is a non-empty list, so
  it is always true, one byte under `while 1:` plus a `print(…);`.

**Notes**

- Integers only, no floats and no `import`, so it is correct for every n.
  The lemma is the same argument as the classical proof that e is
  irrational, and it does not need any bound on how well e can be
  approximated.
- M and F grow like n!, so each term costs time proportional to log n!.
  It prints the whole b-file (1000 terms) at once and about 129000 terms
  in 60 s; the bar is the whole b-file in 60 s.
