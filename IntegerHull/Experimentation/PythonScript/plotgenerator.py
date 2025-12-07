import matplotlib.pyplot as plt
import numpy as np
import re

# ============================================================
# USER METADATA (indexed by filename)
# ============================================================
# (dim, vertices, volume, BF_new_calls, BF_new_percent, BF_old_calls, BF_old_percent)
metadata = {

    # ===================== 2D TESTS =====================

    "redcheck.ext": (2, 4, 4, 1, 0, 1, 1.72),
    "InhomIneqIH.in": (2, 3, float("inf"), 2, 3.12, 2, 5.04),
    "ThierryApproximate.in": (2, 6, 3652932004, 1, 0, 1, 1.49),

    "T41": (2, 50, 106437.5, 1, 0.001, 2, 0.49),
    "T44": (2, 50, 139514, 1, 0.01, 2, 0.71),
    "T47": (2, 50, 54768, 1, 0.01, 2, 0.70),
    "T50": (2, 50, 114163, 1, 0.02, 2, 0.72),
    "T53": (2, 75, 29666.5, 1, 0.01, 2, 0.91),
    "T56": (2, 75, 24893, 1, 0.01, 2, 1.17),

    # ===================== 3D TESTS =====================

    "dodecahedron-v.IntHull.ref.1": (3, 6, 1.34, 1, 0, 2, 23.99),
    "dodecahedron-v.IntHull.ref.2": (3, 6, 1.34, 1, 1.45, 1, 4.22),
    "cube_3.in": (3, 6, 1, 1, 1.75, 1, 2.27),
    "isIC.in": (3, 5, 2.5, 3, 29.05, 2, 20.59),
    "Kwak10Codim.in": (3, 21, 5536, 1, 0, 2, 99.92),
    "project1res.ine": (3, 24, 62.7, 1, 0.29, 1, 99.95),

    "cyclic10-4.ext": (3, 10, 2772, 1, 0, 2, 8.82),
    "cubocta.ine": (3, 12, 6.7, 1, 0.34, 2, 19.65),
    "hexocta.ine": (3, 26, 2.4, 1, 0.03, 1, 5.41),
    "irbox20-4.ext": (3, 14, 273550.5, 1, 0.02, 2, 2.09),
    "e0.in": (3, 3, 0, 1, 45, 1, 46.51),
    "pugh": (3, 3, float("inf"), 2, 0.04, 2, 99.98),

    "T61": (3, 25, 35600, 1, 0.01, 2, 5.141),
    "T62": (3, 25, 400500, 1, 0.05, 2, 4.15),
    "T63": (3, 25, 694200, 1, 0.01, 2, 4.10),

    # ===================== 4D TESTS =====================

    "big_empty_deg1.in": (4, 4, 16666666.67, 2, 21.83, 2, 22.46),
    "truncated_dodecahefron_dual": (4, 18, 0.125, 2, 6.25, 3, 10.79),
    "strange.in": (4, 5, 0.5, 2, 20.53, 3, 32.62),
    "samplelp1.ine": (4, 6, 1.34, 2, 13.75, 3, 23.26),
}

# ============================================================
# EXTRACT NEW + OLD TIMES FROM FILES
# ============================================================

def extract(path, regex_pattern):
    names = []
    times = []
    patt = re.compile(regex_pattern)

    with open(path, "r") as f:
        for line in f:
            m = patt.search(line)
            if m:
                names.append(m.group(1))
                times.append(float(m.group(2)))

    return names, times


new_names, new_times = extract(
    "../BENCHMARKING_results_newmethod.output",
    r'"newmethod time for",\s*"Input/([^"]+)",\s*"is",\s*([\d\.Ee+-]+)'
)

old_names, old_times = extract(
    "../BENCHMARKING_results_oldmethod.output",
    r'"oldmethod time for",\s*"Input/([^"]+)",\s*"is",\s*([\d\.Ee+-]+)'
)

# ============================================================
# ALIGN NEW & OLD RESULTS BY FILENAME
# ============================================================

common = [name for name in new_names if name in old_names]

aligned_new = []
aligned_old = []
dims = []
verts = []
vols = []
BFn = []
BFn_pct = []
BFo = []
BFo_pct = []

for name in common:
    aligned_new.append(new_times[new_names.index(name)])
    aligned_old.append(old_times[old_names.index(name)])

    d, v, vol, bf_n, bf_n_p, bf_o, bf_o_p = metadata[name]
    dims.append(d)
    verts.append(v)
    BFn.append(bf_n)
    BFn_pct.append(bf_n_p)
    BFo.append(bf_o)
    BFo_pct.append(bf_o_p)

    # Replace infinite volumes by 100 for plotting
    if np.isinf(vol):
        vols.append(2e9)
    else:
        vols.append(vol)

aligned_new = np.array(aligned_new)
aligned_old = np.array(aligned_old)
dims = np.array(dims)
verts = np.array(verts)
vols = np.array(vols)
BFn = np.array(BFn)
BFn_pct = np.array(BFn_pct)
BFo = np.array(BFo)
BFo_pct = np.array(BFo_pct)

# ============================================================
# PLOTS
# ============================================================

# 1) Volume vs Time
plt.figure(figsize=(10,6))
plt.scatter(vols, aligned_new, label="New")
plt.scatter(vols, aligned_old, label="Old", marker="x")
plt.xscale("log")   # <<< ADD THIS
plt.xlabel("Volume (∞ → 2e9)")
plt.ylabel("Time (s)")
plt.title("Volume vs Time (Log Scale)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("volume_vs_time.png")
plt.close()

# 2) Vertices vs Time
plt.figure(figsize=(10,6))
plt.scatter(verts, aligned_new, label="New")
plt.scatter(verts, aligned_old, label="Old", marker="x")
plt.xlabel("Vertices")
plt.ylabel("Time (s)")
plt.title("Vertices vs Time")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("vertices_vs_time.png")
plt.close()

# 3) Dimension vs Time
plt.figure(figsize=(10,6))
plt.scatter(dims, aligned_new, label="New")
plt.scatter(dims, aligned_old, label="Old", marker="x")
plt.xlabel("Dimension")
plt.ylabel("Time (s)")
plt.title("Dimension vs Time")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("dimension_vs_time.png")
plt.close()

# 4) Speedup
speedup = aligned_old / aligned_new
plt.figure(figsize=(10,6))
plt.bar(np.arange(len(speedup)), speedup)
plt.xlabel("Test Index")
plt.ylabel("Speedup (Old/New)")
plt.title("Speedup of New Algorithm")
plt.grid(True)
plt.tight_layout()
plt.savefig("speedup_factor.png")
plt.close()

# 5) Brute Force Calls Comparison
plt.figure(figsize=(10,6))
idx = np.arange(len(BFn))
width = 0.35
plt.bar(idx, BFn, width, label="BF New")
plt.bar(idx + width, BFo, width, label="BF Old")
plt.xlabel("Test Index")
plt.ylabel("BF Calls")
plt.title("Brute Force Calls: New vs Old Method")
plt.legend()
plt.tight_layout()
plt.savefig("bf_calls_comparison.png")
plt.close()

# 6) Brute Force Percentage vs Time
plt.figure(figsize=(10,6))
plt.scatter(BFn_pct, aligned_new, label="New BF %")
plt.scatter(BFo_pct, aligned_old, label="Old BF %", marker="x")
plt.xlabel("Brute Force (%)")
plt.ylabel("Time (s)")
plt.title("Brute Force % vs Time")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("bf_percent_vs_time.png")
plt.close()

print("\nSaved:")
print(" volume_vs_time.png")
print(" vertices_vs_time.png")
print(" dimension_vs_time.png")
print(" speedup_factor.png")
print(" bf_calls_comparison.png")
print(" bf_percent_vs_time.png")
