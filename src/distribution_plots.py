import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

FIGURES_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "figures")

def plot_salary_distributions(df: pd.DataFrame) -> str:
    """
    Generates KDE density distributions and Boxen plots for salary analysis.
    """
    os.makedirs(FIGURES_DIR, exist_ok=True)
    sns.set_theme(style="whitegrid", font="sans-serif")
    plt.rcParams.update({"figure.dpi": 300})

    fig, axes = plt.subplots(2, 1, figsize=(13, 11), gridspec_kw={"height_ratios": [1, 1.2]})

    # 1. KDE Density Plot by Experience Level
    exp_order = ["Entry-Level", "Mid-Level", "Senior", "Lead / Principal", "Executive"]
    palette_exp = sns.color_palette("mako", n_colors=len(exp_order))

    for idx, exp in enumerate(exp_order):
        subset = df[df["experience_level"] == exp]
        sns.kdeplot(
            data=subset["salary_in_usd"] / 1000,
            ax=axes[0],
            fill=True,
            alpha=0.35,
            linewidth=2,
            label=f"{exp} (Median: ${subset['salary_in_usd'].median()/1000:.0f}k)",
            color=palette_exp[idx]
        )

    axes[0].set_title("A. Kernel Density Estimation (KDE) of Tech Salaries Across Experience Tiers", fontsize=13, fontweight="bold", pad=10)
    axes[0].set_xlabel("Annual Base Salary ($ in Thousands USD)", fontsize=11, fontweight="bold")
    axes[0].set_ylabel("Probability Density", fontsize=11, fontweight="bold")
    axes[0].legend(title="Experience Tier", frameon=True, facecolor="white", framealpha=0.9, loc="upper right")
    axes[0].set_xlim(30, 380)

    # 2. Boxen Plot of Total Compensation Across Job Roles
    role_order = df.groupby("job_title")["total_compensation"].median().sort_values(ascending=False).index

    sns.boxenplot(
        data=df,
        x="total_compensation",
        y="job_title",
        order=role_order,
        palette="viridis",
        hue="job_title",
        legend=False,
        ax=axes[1]
    )

    # Format x-axis as $k
    axes[1].xaxis.set_major_formatter(lambda x, pos: f"${int(x/1000)}k")
    axes[1].set_title("B. Total Compensation Distribution (Base + Equity) by Specialized Tech Role", fontsize=13, fontweight="bold", pad=10)
    axes[1].set_xlabel("Total Annual Compensation (USD)", fontsize=11, fontweight="bold")
    axes[1].set_ylabel("Specialized Job Role", fontsize=11, fontweight="bold")

    plt.tight_layout()
    output_path = os.path.join(FIGURES_DIR, "01_salary_distribution_kde.png")
    plt.savefig(output_path, dpi=300)
    plt.close()
    print(f"[OK] Saved Distribution Plot to: {output_path}")
    return output_path
