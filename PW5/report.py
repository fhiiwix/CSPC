import pandas as pd

df = pd.read_csv("results/events.csv")

lines = ["SEISMIC EVENT ANALYSIS SUMMARY", "=" * 35, ""]
for _, row in df.iterrows():
    lines.append(
        f"Record: {row['event']}\n"
        f"  P-wave arrival (t_P): {row['t_P']:.2f} s\n"
        f"  S-wave arrival (t_S): {row['t_S']:.2f} s\n"
        f"  Epicentral distance (R): {row['R_km']:.2f} km\n"
        f"  Peak Ground Velocity (PGV): {row['PGV_cm_s']:.4f} cm/s\n"
        f"  Estimated Magnitude (M): {row['M']:.2f}\n"
    )

closer = df.loc[df["R_km"].idxmin(), "event"]
stronger = df.loc[df["M"].idxmax(), "event"]

lines.append("-" * 35)
lines.append(f"Closer earthquake: {closer}")
lines.append(f"Stronger earthquake: {stronger}")

report_text = "\n".join(lines)
with open("results/report.txt", "w") as f:
    f.write(report_text)

print(report_text)