# A000040

> The prime numbers.
> — [OEIS A000040](https://oeis.org/A000040)

Offset 1: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, …

### Python 3 — 40 bytes

```python
P=k=1
while[-P%k==1==print(k)]:P*=k;k+=1
```

**How it works**

- Wilson's theorem: k ≥ 2 is prime exactly when (k − 1)! ≡ −1 (mod k). No
  trial division is needed.
- `P` is kept equal to (k − 1)!: it starts at 0! = 1, and `P*=k;k+=1` turns
  (k − 1)! into k! as k moves on.
- `-P%k` is `(-P)%k`, so `-P%k==1` is the theorem's test. For k = 1 every
  number is 0 mod 1, so 1 is skipped with no special case. For k = 4,
  3! = 6 ≡ 2 (mod 4) fails as it should: 4 is the only composite where
  (k − 1)! is not 0 mod k.
- The chained comparison `-P%k==1==print(k)` means
  `-P%k==1 and 1==print(k)`, so `print(k)` runs only for primes. The list
  around it is non-empty, so the loop never stops, as in
  [A000028](../A000028/).

**Notes**

- P has about k log₂ k bits, so each step costs about k log k: around
  15 000 primes a minute. The whole b-file (10 000 terms, up to 104 729)
  prints in 20–30 s; the bar is the whole b-file in 60 s.
- Squaring the factorial also gives 40 bytes: `P=k=1` +
  `while[P%k>0==print(k)]:P*=k*k;k+=1`, since (k − 1)!² mod k is 1 for
  primes and 0 otherwise. The test is 2 bytes shorter, `P*=k*k` takes them
  back, and P is twice as long, so it manages only about 11 000 primes a
  minute.
- Moving the increment into the condition, `P=k=1` +
  `while k:=k+1:~P%k or print(k);P*=k`, is 40 too: k starts at 2, so the
  shorter test `~P%k` (k divides P + 1) is safe there.
- Trial division, `n=1` + `while n:=n+1:all(n%d for d in range(2,n))and
  print(n)`, is 57 bytes. Fermat's test `2**n%n==2` would be shorter but is
  wrong: 341 = 11 · 31 passes it.
- sympy cannot win: `from sympy import*` and its newline already take 19
  bytes, and `n=1` + `while[print(prime(n))]:n+=1` brings it to 50, so there
  is no sympy entry.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 40 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000040), CC BY-SA 4.0.
