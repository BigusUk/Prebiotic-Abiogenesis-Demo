#!/usr/bin/env python3
import numpy as np
from rdkit import Chem
from rdkit.Chem import AllChem, Descriptors
from Bio.SeqUtils.ProtParam import ProteinAnalysis

np.random.seed(42)

def generate_random_polyglycine(min_len=4, max_len=20):
    length = np.random.randint(min_len, max_len + 1)
    seq = 'G' * length
    # Build SMILES for polyglycine (NCC(=O)) repeated
    smiles = 'NCC(=O)' + 'NCC(=O)' * (length - 1)
    smiles = smiles.rstrip('O') + 'N'  # Rough correction for proper peptide
    return seq, smiles

def is_stable_molecule(mol):
    if mol is None:
        return False
    mw = Descriptors.MolWt(mol)
    logp = Descriptors.MolLogP(mol)
    # Simple prebiotic stability proxy: reasonable size and hydrophilicity
    return 200 < mw < 2000 and -3 < logp < 1

def simulate_trial():
    temp = np.random.uniform(30, 50)    # °C, hydrothermal-like
    pH = np.random.uniform(6, 8)
    conc = np.random.uniform(0.5, 1.5)   # Arbitrary concentration units

    # Narrow viable window (realistic for vents)
    if 35 < temp < 45 and 6.5 < pH < 7.5 and conc > 0.8:
        seq, smiles = generate_random_polyglycine()
        mol = Chem.MolFromSmiles(smiles)
        if mol and is_stable_molecule(mol):
            AllChem.Compute2DCoords(mol)  # For potential visualization
            analysis = ProteinAnalysis(seq)
            mw = analysis.molecular_weight()
            pI = analysis.isoelectric_point()
            print(f'Success: Polyglycine length {len(seq)}, MW = {mw:.1f}, pI = {pI:.2f}')
            return True
    return False

trials = 20000  # Balanced for speed/precision
successes = sum(simulate_trial() for _ in range(trials))
prob = (successes / trials) * 100

print(f'\nAbiogenesis success rate after {trials:,} trials: {prob:.3f}%')
print('Note: This is a toy model illustrating narrow viable windows and basic chemical filtering.')
