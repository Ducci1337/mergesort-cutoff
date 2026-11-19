import pandas as pd
import matplotlib.pyplot as plt
import os

# đọc dữ liệu
df = pd.read_csv("results/raw_results.csv")

# tính trung bình thời gian theo cutoff, loại mảng, kích thước
avg = df.groupby(["cutoff", "array_type", "array_size"])["time_ms"].mean().reset_index()
avg.columns = ["cutoff", "array_type", "array_size", "avg_time_ms"]

os.makedirs("results/charts", exist_ok=True)

TYPES = ["random", "sorted", "reverse", "nearly_sorted"]
TYPE_LABELS = {
    "random": "Mảng ngẫu nhiên",
    "sorted": "Mảng đã sắp xếp",
    "reverse": "Mảng ngược",
    "nearly_sorted": "Mảng gần như đã sắp xếp"
}
SIZES = sorted(avg["array_size"].unique())
COLORS = plt.cm.tab10.colors

# --- Đồ thị 1: với mỗi loại mảng, vẽ time vs cutoff cho từng kích thước n ---
for arr_type in TYPES:
    fig, ax = plt.subplots(figsize=(10, 6))
    subset = avg[avg["array_type"] == arr_type]
    for i, n in enumerate(SIZES):
        data = subset[subset["array_size"] == n].sort_values("cutoff")
        ax.plot(data["cutoff"], data["avg_time_ms"],
                marker="o", label=f"n = {n:,}", color=COLORS[i])

    ax.axvline(x=7,  color="gray",   linestyle="--", linewidth=1, label="CUTOFF = 7 (Java 6)")
    ax.axvline(x=10, color="orange", linestyle="--", linewidth=1, label="CUTOFF = 10 (giáo trình)")

    ax.set_title(f"Thời gian chạy theo CUTOFF — {TYPE_LABELS[arr_type]}")
    ax.set_xlabel("Giá trị CUTOFF")
    ax.set_ylabel("Thời gian trung bình (ms)")
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(f"results/charts/chart_{arr_type}.png", dpi=150)
    plt.close()
    print(f"Đã lưu: results/charts/chart_{arr_type}.png")

# --- Đồ thị 2: so sánh tổng hợp tất cả loại mảng, n lớn nhất ---
n_max = max(SIZES)
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
axes = axes.flatten()

for i, arr_type in enumerate(TYPES):
    ax = axes[i]
    data = avg[(avg["array_type"] == arr_type) & (avg["array_size"] == n_max)].sort_values("cutoff")
    ax.plot(data["cutoff"], data["avg_time_ms"], marker="o", color=COLORS[i])
    ax.axvline(x=7,  color="gray",   linestyle="--", linewidth=1)
    ax.axvline(x=10, color="orange", linestyle="--", linewidth=1)

    best_cutoff = data.loc[data["avg_time_ms"].idxmin(), "cutoff"]
    ax.axvline(x=best_cutoff, color="red", linestyle="-", linewidth=1.5, label=f"Tốt nhất: {best_cutoff}")

    ax.set_title(TYPE_LABELS[arr_type])
    ax.set_xlabel("CUTOFF")
    ax.set_ylabel("Thời gian (ms)")
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)

fig.suptitle(f"So sánh CUTOFF — n = {n_max:,}", fontsize=14, fontweight="bold")
plt.tight_layout()
plt.savefig("results/charts/chart_summary.png", dpi=150)
plt.close()
print("Đã lưu: results/charts/chart_summary.png")

# --- In bảng tóm tắt: CUTOFF tốt nhất cho từng loại mảng và kích thước ---
print("\n=== CUTOFF tốt nhất ===")
for arr_type in TYPES:
    for n in SIZES:
        subset = avg[(avg["array_type"] == arr_type) & (avg["array_size"] == n)]
        if subset.empty:
            continue
        best = subset.loc[subset["avg_time_ms"].idxmin()]
        print(f"{arr_type:15s} | n={n:>9,} | CUTOFF={int(best['cutoff']):2d} | {best['avg_time_ms']:.4f} ms")
