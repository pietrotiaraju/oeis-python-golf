# A000720

> pi(n), the number of primes <= n. Sometimes called PrimePi(n) to distinguish it from the number 3.14159...
> — [OEIS A000720](https://oeis.org/A000720)

Offset 1: 0, 1, 2, 2, 3, 3, 4, 4, 4, 4, 5, 5, 6, 6, 6, 6, 7, 7, 8, 8, …

### Python 3 — 44 bytes

```python
s=0;P=k=1
while[print(s)]:P*=k*k;k+=1;s+=P%k
```

**How it works**

- Wilson's theorem: k > 1 is prime exactly when (k−1)! ≡ −1 (mod k). For
  the square, ((k−1)!)² ≡ 1 (mod k) when k is prime, and ≡ 0 when k is
  composite: for composite k other than 4 already k | (k−1)!, and for
  k = 4, 3!² = 36 ≡ 0. So `P%k` is 1 at primes and 0 elsewhere, with no
  "−1" to undo.
- `P` holds ((k−1)!)², updated with `P*=k*k` before `k+=1`, and `s`
  counts the primes seen: s = π(k). The loop prints π(k) before moving
  to k+1, starting from π(1) = 0.
- `while[print(s)]:` loops forever, because a one-element list is truthy
  even though `print` returns None.

**Notes**

- Exact integer arithmetic; the only fact used is Wilson's theorem.
- The product grows to about 2k·log₂k bits, so each step costs O(k log k)
  and n terms cost about n²: 91000 terms in 60 s.
- The b-file has 100000 terms; the bar is 70000 terms in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 44 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000720), CC BY-SA 4.0.
