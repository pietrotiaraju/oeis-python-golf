# A001363

> Primes in ternary.
> — [OEIS A001363](https://oeis.org/A001363)

Offset 1: 2, 10, 12, 21, 102, 111, 122, 201, 212, 1002, 1011, 1101, 1112, …

### Python 3 — 75 bytes

```python
f=lambda n:n and n%3+10*f(n//3)
P=k=1
while[-P%k==1==print(f(k))]:P*=k;k+=1
```

**How it works**

- **Primes** by Wilson's theorem, as in [A000040](../../A000xxx/A000040/):
  P = (k − 1)! and k > 1 is prime if and only if (k − 1)! ≡ −1 (mod k),
  that is `-P%k==1` (k = 1 gives 0). The chain `-P%k==1==print(…)` calls
  `print` only when the first comparison holds.
- **Ternary.** `f(n)` writes n in base 3 and reads the digits as a decimal
  number: f(n) = (n mod 3) + 10·f(⌊n/3⌋), f(0) = 0.
- `while[…]:` is always true (a one-element list); the body steps
  P = (k − 1)! to k!.

**Notes**

- Exact, so correct for every n. The factorial grows to about
  k·log₁₀ k digits, so the program slows down roughly quadratically; the
  recursion in `f` goes one level per ternary digit, far below the limit.
- The bar is the whole b-file (847 terms, up to the prime 6553 =
  22222201₃) in 60 s, which takes a fraction of a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 75 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001363), CC BY-SA 4.0.
