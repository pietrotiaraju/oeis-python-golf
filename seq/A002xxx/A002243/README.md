# A002243

> Numbers that are not the sum of 3 distinct triangular numbers.
> — [OEIS A002243](https://oeis.org/A002243)

Offset 1, finite (all 12 terms): 1, 2, 3, 5, 6, 8, 12, 15, 20, 23, 33, 78.

### Python 3 — 88 bytes

```python
T={n:=0}
while 1:n+=1;T|={n*-~n//2};any(a<b<n-a-b in T for a in T for b in T)or print(n)
```

**How it works**

- **The definition, checked for each n.** Triangular numbers here
  include 0 = T(0), as in the data (4 = 0 + 1 + 3). Before n is tested,
  `T` holds T(0), T(1), …, T(n), and every triangular number ≤ n is
  among them (T(k) ≤ n forces k ≤ n). n is a sum of three distinct ones
  exactly when two of them, a < b, leave a third c = n − a − b that is
  triangular and larger than b; the chained comparison
  `a<b<n-a-b in T` tests a < b, b < c and c ∈ T at once. If no pair
  works, n is printed.
- `T={n:=0}` starts the set with 0 and sets n = 0; `n*-~n//2` is
  n(n+1)/2.

**Notes**

- The program follows the definition for every n and uses no theorem.
  The entry marks the list as complete (keywords fini, full) but cites no
  proof; the program does not rely on it: after 78 it keeps checking
  79, 80, … forever and prints nothing more, which is right exactly when
  the list is complete (if a larger exception existed, it would print
  it).
- All 12 terms come at once; the check of each n takes O(n²) steps.
  The bar is the whole sequence in 10 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-23 | Python 3 | 88 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A002243), CC BY-SA 4.0.
