# A000198

> Largest order of automorphism group of a tournament with n nodes.
> — [OEIS A000198](https://oeis.org/A000198)

Offset 1: 1, 1, 3, 3, 5, 9, 21, 21, 81, 81, 81, 243, 243, 441, 1215, 1701, 1701, 6561, …

### Python 3 — 84 bytes

```python
L=[0]*6+[n:=1]
while[print(m:=max(3**(n//3)*L[n//3-n],5*L[-5],21*L[-7]))]:L+=m,;n+=1
```

**How it works**

- The recurrence is a(n) = max(3^⌊n/3⌋·a(⌊n/3⌋), 5·a(n−5), 21·a(n−7)),
  with a(0) = 1 and a(k) = 0 for k < 0.
- Every term is a lower bound. Putting all arcs from one tournament to
  another keeps both automorphism groups, so a(n) ≥ a(i)·a(n−i), and
  a(5) = 5 (rotational tournament) and a(7) = 21 (the Paley tournament on
  7 points). Blowing up each vertex of a tournament on r points into a
  3-cycle gives a(3r) ≥ 3^r·a(r); since a is nondecreasing,
  3^⌊n/3⌋·a(⌊n/3⌋) ≤ a(3⌊n/3⌋) ≤ a(n).
- It is also exact, by Theorem 5 of Alspach and Berggren (1973) as quoted on
  the OEIS page: a(3r) = 3^r·a(r); a(n) = a(n−1) for n ≡ 1, 2, 4 (mod 9);
  a(9k+5) = max(a(9k+3), 5a(9k), 21a(9k−2)); a(9k+7) = 21a(9k);
  a(9k+8) = max(a(9k+7), 5a(9k+3)). Case by case:
  - n ≡ 0 (mod 3): the first term.
  - n ≡ 1, 4 (mod 9): a(n) = a(n−1) = a(3⌊n/3⌋), the first term again.
  - n ≡ 2 (mod 9): a(n) = a(n−1) = a(n−2) = a(3⌊n/3⌋).
  - n ≡ 5 (mod 9): a(9k+3) is the first term, the other two are 5·a(n−5)
    and 21·a(n−7).
  - n ≡ 7 (mod 9): 21·a(n−7).
  - n ≡ 8 (mod 9): a(9k+7) = 21·a(9k) = 21·a(9k+1) = 21·a(n−7), and
    5·a(9k+3) = 5·a(n−5).

  So no a(n−1) term is needed. For n ≤ 8 the seeds give 1, 1, 3, 3, 5, 9,
  21, 21 directly. The recurrence also agrees, up to n = 4000, with
  Theorem 4 of the same paper (closed forms at 3^k, 5·3^k, 7·3^k, maximum
  of a(i)·a(n−i) elsewhere).
- Six leading zeros stand for a(−6), …, a(−1), so `L[-5]` and `L[-7]` exist
  from the first pass. Since `L` always ends at a(n−1), a(k) is `L[k-n]`.
- A search over sets of terms c·a(n−k) with c ≤ a(k), k ≤ 9, found
  {5·a(n−5), 21·a(n−7)} as the only shortest one that reproduces the b-file.
  The straight Theorem 4 version (maximum over all splits, plus a short
  `24%n*7%23` that is 5 at n = 5 and 21 at n = 7) came out at 100 bytes.

**Notes**

- Exact integer arithmetic; correct for every n given the Alspach–Berggren
  theorem. The whole b-file (1000 terms) prints at once; the program stops
  after a(18032), when the next term passes the 4300-digit int-to-str limit
  of Python 3.11+. The bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 84 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000198), CC BY-SA 4.0.
