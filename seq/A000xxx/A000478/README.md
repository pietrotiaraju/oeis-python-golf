# A000478

> Number of ways of placing n labeled balls into 3 indistinguishable boxes with at least 2 balls in each box.
> — [OEIS A000478](https://oeis.org/A000478)

Offset 6: 15, 105, 490, 1918, 6825, 22935, 74316, 235092, 731731, 2252341, …

### Python 3 — 61 bytes

```python
n=6
while 1:print((6*(1+n+n*n)-3*(n+2)*2**n+2*3**n)//12);n+=1
```

**How it works**

- One block of at least two labeled elements has e.g.f.
  exp(x)−1−x: remove the empty set and singleton. Three unlabeled
  blocks therefore have e.g.f. (exp(x)−1−x)³/3!.
- Expand the cube as
  exp(3x)−3(1+x)exp(2x)+3(1+x)²exp(x)−(1+x)³.
  For n≥6 the final polynomial has no n-th coefficient. Taking
  n-th derivatives at zero and dividing by 6 gives

  a(n)=3ⁿ/6−(n+2)2ⁿ/4+(n²+n+1)/2.

- Put the expression over the common denominator 12 before computing
  it. `6*(1+n+n*n)-3*(n+2)*2**n+2*3**n` is the numerator
  in the program; the complete numerator is divisible by 12.
- The smallest possible n is 6. Then all boxes contain two elements,
  so a(6)=6!/(2!³3!)=15, explaining both the offset and first term.

**Notes**

- Exact integer arithmetic; no floating-point exponentials or fractions
  are evaluated. Cancellation occurs in the integer numerator before
  the final division.
- Compare [A000453](../A000453/) and [A000481](../A000481/),
  which require nonempty blocks but allow singletons. Here subtracting
  x from the one-block e.g.f. enforces the stronger size condition.
- The expression needs only a constant number of integer temporaries.
  Exponential growth eventually reaches Python 3.11+'s default
  4300-digit conversion limit, an interpreter limit.
- The b-file has 195 terms (indices 6 through 200). The bar is the
  whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 61 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000478), CC BY-SA 4.0.
