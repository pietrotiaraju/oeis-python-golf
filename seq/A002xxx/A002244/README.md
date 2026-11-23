# A002244

> Numbers that are not the sum of 3 distinct nonzero triangular numbers.
> — [OEIS A002244](https://oeis.org/A002244)

Offset 1, finite (all 28 terms): 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 15, 16, 18, 20, 21, 23, 27, 29, 33, 36, 38, 48, 51, 78, 111, 183.

### Python 3 — 89 bytes

```python
T={1};n=0
while 1:n+=1;T|={n*-~n//2};any(a<b<n-a-b in T for a in T for b in T)or print(n)
```

**How it works**

- **The definition, checked for each n.** Before n is tested, `T` holds
  the nonzero triangular numbers T(1), …, T(n), and every nonzero
  triangular number ≤ n is among them (T(k) ≤ n forces k ≤ n). n is a
  sum of three distinct ones exactly when two of them, a < b, leave a
  third c = n − a − b that is triangular and larger than b; the chained
  comparison `a<b<n-a-b in T` tests a < b, b < c and c ∈ T at once. If
  no pair works, n is printed.
- `T={1}` leaves 0 out of the set (compare [A002243](../A002243/),
  where 0 counts); `n*-~n//2` is n(n+1)/2.

**Notes**

- The program follows the definition for every n and uses no theorem.
  The entry marks the list as complete (keywords fini, full) but cites no
  proof; the program does not rely on it: after 183 it keeps checking
  184, 185, … forever and prints nothing more, which is right exactly
  when the list is complete (if a larger exception existed, it would
  print it).
- All 28 terms come at once; the check of each n takes O(n²) steps.
  The bar is the whole sequence in 10 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-23 | Python 3 | 89 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A002244), CC BY-SA 4.0.
