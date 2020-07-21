from collections import defaultdict

import matplotlib.pyplot as plt
import numpy as np

from Bio.SeqUtils import GC


def _sequence_histogram(seq_lengths, title, file_name):
    plt.hist(seq_lengths, 20, facecolor="blue", alpha=0.5)
    plt.xlabel("Length")
    plt.ylabel("Count")
    plt.title(title)
    plt.savefig(file_name)
    plt.clf()


def _gc_plot(sequences, title, file_name):
    gc_values = sorted(GC(seq) for seq in sequences)
    plt.plot(gc_values)
    plt.title(title)
    plt.xlabel("ORFs")
    plt.ylabel("GC%")
    plt.savefig(file_name)
    plt.clf()


def _aa_barchart(prot_sequences):
    aa_count = defaultdict(int)
    for sequence in prot_sequences:
        for aa in sequence:
            aa_count[aa] += 1

    objects = [*aa_count]
    objects.sort()
    y_pos = np.arange(len(objects))
    performance = []
    for aa in objects:
        performance.append(aa_count[aa])

    plt.bar(y_pos, performance, align="center", facecolor="blue", alpha=0.5)
    plt.xticks(y_pos, objects)
    plt.ylabel("Count")
    plt.title("Amino Acid Count for Translated Proteins")
    plt.savefig("aa_count_chart.png")
    plt.clf()


def generate_diagnostic_plots(db_manager):
    dna_results = db_manager.exec_query("select dna_sequence from walk")

    dna_lengths = map(lambda x: len(x[0]), dna_results)
    _sequence_histogram(
        list(dna_lengths), "DNA Sequence Lengths from FASTG", "fastg_seq_lengths.png"
    )

    protein_results = db_manager.exec_query("select sequence from protein")
    protein_lengths = map(lambda x: len(x[0]), protein_results)
    _sequence_histogram(
        list(protein_lengths), "Protein Sequence Lengths", "protein_seq_lengths.png"
    )

    _gc_plot(
        list(map(lambda x: x[0], dna_results)),
        "GC Pct. - Translated FASTG",
        "gc_pct.png",
    )

    # bar chart of all translated protein amino acids
    _aa_barchart(list(map(lambda x: x[0], protein_results)))
