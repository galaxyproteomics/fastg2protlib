from fastg2protlib import fastg2protlib
import os


def test_peptides_for_fastg(shared_datadir, tmpdir):
    contents = (shared_datadir / 'two.fastg').read_text()
    sub = tmpdir.mkdir("sub")
    p = sub.join("fastg_input")
    p.write(contents)
    
    fastg2protlib.peptides_for_fastg(
        os.path.join(sub, "fastg_input"), 
        min_protein_length=40, 
        db_name=os.path.join(sub, "test.db"),
        peptide_file_name=os.path.join(sub, "peptide.fasta"))
    with open(os.path.join(sub, "peptide.fasta")) as f:
        peps = f.readlines()
    assert len(peps) == 68