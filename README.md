# RNA to Protein Translator

This repository contains a simple Python script that translates an RNA sequence into a protein sequence using the standard genetic codon table.

## 🧬 Overview

The script reads an RNA sequence from a text file (`input.txt`), translates the codons into their corresponding amino acids, and outputs the resulting protein string. Translation halts when a stop codon is encountered.

## 📂 Files

- `translate_rna.py` — Main script that handles RNA translation.
- `input.txt` — Sample input file containing the RNA sequence.

## ▶️ How to Use

1. Make sure you have Python 3 installed.

2. Add your RNA sequence to input.txt (must be a continuous string like AUGGCC...).

3. Run the script:
   ```bash
   python translate_rna.py
   ```

## 📋 Example

**Input (********`input.txt`********):**

```
AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA
```

**Output:**

```
Protein String: MAMAPRTEINSTRING
```

## 📜 Notes

- The script uses the standard RNA codon table.
- Translation stops at the first stop codon (`UAA`, `UAG`, or `UGA`).
- Invalid or incomplete codons at the end are ignored.

## 📜 License

This project is licensed under the MIT License.

---

Feel free to modify or extend the script to handle more complex inputs, output formats, or integrate into larger bioinformatics workflows.

