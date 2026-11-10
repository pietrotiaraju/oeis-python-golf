# A001466

> Denominators of greedy Egyptian fraction expansion of Pi - 3.
> — [OEIS A001466](https://oeis.org/A001466)

Offset 1: 8, 61, 5020, 128541455, 162924332716605980, 28783052231699298507846309644849796, …

### Python 3 — 98 bytes

```python
q=t=l=y=1
while(y-q)*(c:=t//y+1)<t or[print(c),y:=y*c-t,q:=q*c,t:=t*c]:l+=2;y=y*l-2*q;q*=l//2;t*=l
```

**How it works**

- **The greedy expansion.** With x₀ = π − 3, each step takes the
  smallest d with 1/d ≤ x, that is d = ⌈1/x⌉, prints it and goes on with
  x − 1/d (the entry's PARI program). Since π is irrational, x is never 0
  and 1/x is never a whole number.
- **π from Gibbons' spigot**, the same state as the π digits of
  [A000796](../../A000xxx/A000796/): the series
  π = 2 + 1/3·(2 + 2/5·(2 + 3/7·(2 + …))) is read term by term into an
  increasing map f(X) = (q·X + y − 4q)/t, with x = f(X) for the value X of
  the rest of the series, which lies strictly between 3 and 4. So x is
  strictly between f(3) = (y − q)/t and f(4) = y/t. A new term
  (`l` = 2k + 1, `l//2` = k) turns f into f(2 + k·X/l): q → q·k, t → t·l,
  y → y·l − 2q, and the interval gets more than 2 times narrower. At the
  start q = t = 1 and y = 1 give f(X) = X − 3, so x = π − 3.
- **Deciding a step.** `c` = ⌊t/y⌋ + 1 = ⌊1/f(4)⌋ + 1. As x < f(4),
  1/x > 1/f(4) and so d = ⌈1/x⌉ ≥ c. If also f(3)·c ≥ 1, that is
  `(y-q)*c>=t`, then x > f(3) ≥ 1/c, so 1/x < c and d ≤ c: d = c for sure.
  (y > 0 always, since f(4) > x > 0.) Otherwise the condition is true and
  the body reads another term; once the interval is narrow enough, c is d
  and f(3)·d > 1, since x·d > 1, so every term is eventually printed.
- **Taking the step.** x − 1/c = (c·(q·X + y − 4q) − t)/(c·t): q → q·c,
  t → t·c and y → y·c − t, all exact. The list holding the print is
  non-empty, so the body also runs after a print; one print per term read
  is plenty, since each new d needs about twice as many terms as the
  last.

**Notes**

- Exact integer arithmetic, so it is right for every n. The denominators
  roughly square at each step (a(10) has 553 digits, a(11) 1109), so
  a(13), with some 4400 digits, would hit the 4300-digit int-to-str limit
  of Python 3.11+, an interpreter limit far past the bar. The 10-term
  b-file prints in under a second on a slow PC, a(11)
  takes about 5 s and a(12) about 30 s. The bar is the whole b-file in
  60 s.
- An exact `Fraction` version over π/2 = Σ k!/(2k+1)!!, with π between
  the partial sum and the partial sum plus twice the next term, is 130
  bytes and about twice as slow.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-10 | Python 3 | 98 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001466), CC BY-SA 4.0.
