# OEIS Python Golf

Shortest known Python programs that generate sequences from the
[OEIS](https://oeis.org/). Every record is run and checked against the
sequence's OEIS b-file, locally and in CI.

## Records

Size in bytes, shortest in bold. The last column is how many terms every
program for that sequence must reproduce within its time limit. Click a
sequence for the code and how it works.

<!-- records:start -->

**117 sequences**, 11579 bytes in all.

| Folder | Sequences |
|---|---|
| [A000000 to A000999](seq/A000xxx/) | 110 |
| [A276000 to A276999](seq/A276xxx/) | 1 |
| [A300000 to A300999](seq/A300xxx/) | 3 |
| [A334000 to A334999](seq/A334xxx/) | 1 |
| [A384000 to A384999](seq/A384xxx/) | 1 |
| [A386000 to A386999](seq/A386xxx/) | 1 |

Latest 20 records:

| Date | Sequence | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | [A000024](seq/A000xxx/A000024/) | 92 | range named in the while condition |
| 2026-11-05 | [A000021](seq/A000xxx/A000021/) | 92 | range named in the while condition |
| 2026-11-05 | [A000018](seq/A000xxx/A000018/) | 92 | range named in the while condition |
| 2026-11-05 | [A000080](seq/A000xxx/A000080/) | 339 | value named in the while condition |
| 2026-11-05 | [A000013](seq/A000xxx/A000013/) | 96 | `1<<g-n//g%2` instead of `1<<g>>n//g%2` (from A000116) |
| 2026-11-05 | [A000003](seq/A000xxx/A000003/) | 146 | `import math` instead of `from math import*` |
| 2026-11-05 | [A000001](seq/A000xxx/A000001/) | 255 | value named in the while condition |
| 2026-11-05 | [A300000](seq/A300xxx/A300000/) | 65 | `while[print(...)]:` loop |
| 2026-11-05 | [A000099](seq/A000xxx/A000099/) | 177 | value named in the while condition |
| 2026-11-05 | [A000092](seq/A000xxx/A000092/) | 284 | value named in the while condition |
| 2026-11-05 | [A000091](seq/A000xxx/A000091/) | 88 | value named in the while condition |
| 2026-11-05 | [A000072](seq/A000xxx/A000072/) | 91 | value named in the while condition |
| 2026-11-05 | [A000067](seq/A000xxx/A000067/) | 89 | range named in the while condition |
| 2026-11-05 | [A000059](seq/A000xxx/A000059/) | 63 | ~d gives negative divisors, so the range starts at 0 (-1) |
| 2026-11-05 | [A000050](seq/A000xxx/A000050/) | 87 | range named in the while condition |
| 2026-11-05 | [A000049](seq/A000xxx/A000049/) | 93 | range named in the while condition |
| 2026-11-05 | [A000025](seq/A000xxx/A000025/) | 118 | value named in the while condition |
| 2026-11-05 | [A000019](seq/A000xxx/A000019/) | 468 | value named in the while condition |
| 2026-11-05 | [A000016](seq/A000xxx/A000016/) | 96 | `import math` instead of `from math import*` |
| 2026-11-05 | [A000015](seq/A000xxx/A000015/) | 82 | `import math` instead of `from math import*` |

<!-- records:end -->

## Rules in short

- Print the sequence from its OEIS offset, one term per line, forever.
- CPython 3.12, no flags, no input. Size = file bytes, trailing newline free.
- Plain Python 3 and each "Python 3 + library" are separate categories.
- Correct for every n, with exact arithmetic; hard-coding only with a proof on
  the page.

Full rules and how to send a record: [CONTRIBUTING.md](CONTRIBUTING.md).

## Verify locally

```bash
pip install -r requirements.txt
python tools/verify.py
```

## Why "shortest known"

No record here is proved minimal, and in general none can be:

- A function that returns the length of the shortest program for any output
  cannot exist (the Berry paradox argument behind Kolmogorov complexity).
- Even deciding whether a given program prints a given infinite sequence is
  undecidable (Rice's theorem): a program that prints the sequence but switches
  to 0 once some machine halts prints it exactly when that machine never halts.
- For one specific record of, say, 66 bytes, ruling out every shorter program
  means about 96⁶⁵ ≈ 10¹²⁸ candidates, each needing a proof about its infinite
  output.

So a record stands until someone finds a shorter program.

## Related

- [LODA](https://loda-lang.org/) mines programs for OEIS sequences in its own
  assembly-like language, at a much larger scale and without byte golfing.
- The `%o` lines of each OEIS entry hold readable reference programs.

## License

Programs and tools: [MIT](LICENSE). Sequence names, b-files and other data
come from [The On-Line Encyclopedia of Integer Sequences](https://oeis.org/)
under [CC BY-SA 4.0](https://oeis.org/LICENSE); the pages that quote them are
under CC BY-SA 4.0 too.
