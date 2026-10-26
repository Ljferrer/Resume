# Lukas José Ferrer - Resume

[Read the current resume](LukasFerrer_Resume.pdf) · Updated October 26, 2026

The two-page resume features Work Audit Refine (WAR), the migration of clinical
Activation workloads to self-hosted Qwen, and recent production ML engineering.
It includes clickable links and QR codes for [WAR](https://github.com/Ljferrer/WorkAuditRefine),
the [video demo](https://youtu.be/6LXrfWtKSlg?si=guy4gEUdLSzJRNSj), and
[LinkedIn](https://www.linkedin.com/in/lukasferrer/).

- [Dated October 2026 PDF](output/pdf/LukasJoseFerrer_Resume_October2026.pdf)
- [Original April 2026 PDF](archive/LukasJoseFerrer_Resume_April2026.pdf), preserved unchanged
- [Research and claim provenance](docs/resume-research-april-october-2026.md)
- [Editable content and PDF generator](generate_resume.py)

## Rebuild

With Python 3 and ReportLab installed:

```sh
python3 -m pip install reportlab
python3 generate_resume.py
```

The generator uses ReportLab's bundled fonts, draws vector QR codes, and writes
the dated PDF plus the identical current resume at the repository root. Text is
selectable, and all main sections use a single-column reading order.

`src.tex` is retained as the historical resume source; it does not generate the
current version.

