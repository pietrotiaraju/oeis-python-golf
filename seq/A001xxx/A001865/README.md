# A001865

> Number of connected functions on n labeled nodes.
> — [OEIS A001865](https://oeis.org/A001865)

Offset 1: 1, 3, 17, 142, 1569, 21576, 355081, 6805296, 148869153, 3660215680, …

### Python 3 — 58 bytes

```python
n=0
while 1:n+=1;s=i=0;exec('s=s*i+n**i;i+=1;'*n);print(s)
```

**How it works**

- **Connected functions.** The functional graph of f: [n] → [n] (an arrow
  x → f(x)) is connected exactly when it has a single cycle. With a cycle of
  length k: choose and arrange its nodes in n!/((n − k)!·k) ways, then hang
  the other n − k nodes as a forest of trees rooted on the k cycle nodes, in
  k·nⁿ⁻ᵏ⁻¹ ways. So a(n) = Σₖ n!·nⁿ⁻ᵏ⁻¹/(n − k)!, the first formula on the
  OEIS page, which with j = n − k is
  a(n) = Σⱼ₌₀..ₙ₋₁ (n − 1)!/j!·nʲ.
- **Horner.** s₀ = 1 and sᵢ = i·sᵢ₋₁ + nⁱ give sᵢ = Σⱼ₌₀..ᵢ i!/j!·nʲ, so
  a(n) = sₙ₋₁.
- **The program.** `exec` runs the string `s=s*i+n**i;i+=1;` n times; with
  s = i = 0 the first pass gives s₀ = 1. That is 3 bytes under a
  `s=0;[s:=s*i+n**i for i in range(n)]` comprehension and 4 under an
  indented `for` loop.

**Notes**

- Exact integer arithmetic, so the program is right for every n; a(n)
  passes the 4300-digit int-to-str limit near n = 1372.
- The b-file has 380 terms (n = 1 to 380); the bar is the whole b-file in
  60 s, which takes a second or two.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-16 | Python 3 | 58 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001865), CC BY-SA 4.0.
