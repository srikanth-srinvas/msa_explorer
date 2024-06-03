from Bio import AlignIO

def read_fasta_msa(filepath):
    with open(filepath, "r") as handle:
        alignment = AlignIO.read(handle, "fasta")
    sequences = [str(seq) for seq in alignment]  # Extract sequences as strings
    return sequences
