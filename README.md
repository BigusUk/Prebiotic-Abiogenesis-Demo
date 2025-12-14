# Chemical Abiogenesis Probability Toy Model

> "AI and Humanity: Collaborating to Build a Better Future for the Universe."

A Monte Carlo simulation exploring the emergence of simple peptide-like structures under prebiotic conditions. Uses RDKit for realistic molecule generation/validation and Biopython for protein property analysis.

This is a **highly simplified educational toy model**—not a quantitative prediction of life's origin.

## Features
- Random polyglycine peptide generation (4–20 units)
- Chemistry-inspired stability criteria (molecular weight, logP)
- Narrow environmental windows (hydrothermal vent-inspired)
- Biopython analysis on successful assemblies

Minor Technical Issue Noted:

The SMILES generation ('NCC(=O)' + 'NCC(=O)' * (length - 1) then rstrip('O') + 'N') is approximate and often produces invalid SMILES for longer chains (RDKit returns None frequently). This contributes to very low success rates—realistic for illustrating rarity but could be improved with a proper peptide builder (e.g., using RDKit's Chem.MolFromSequence or a loop for bonds).

## Requirements
- Python 3.8+
- `numpy`
- `rdkit`
- `biopython`

##Install:
```bash
pip install numpy rdkit biopython

##How to Run
Bashpython abiogenesis_simulation.py
Scientific Background & References

RNA World Hypothesis: Gilbert, W. (1986). "Origin of life: The RNA world." Nature 319:618.
Alkaline hydrothermal vent hypothesis: Martin, W., et al. (2008). "Hydrothermal vents and the origin of life." Nature Reviews Microbiology 6:805–814.
Prebiotic peptide formation: Reviews in Huber et al. (2003), Danger et al. (2012).

Customization Ideas

Add other amino acids (modify generate function)
Implement real prebiotic reaction networks
Add RNA nucleotide polymerization
Visualize successful molecules (RDKit 2D coords ready)
