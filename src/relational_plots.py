import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

FIGURES_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "figures")

def plot_relational_trajectories(df: pd.DataFrame) -> str:
    """
    Generates relational scatter plots with regression trendlines and confidence bands.
    """
    os.makedirs(FIGURES_DIR, exist_ok=True)
    sns.set_theme(style="whitegrid")
    plt.rcParams.update({"figure.dpi": 300})

    fig, axes = plt.subplots(1, 2, figsize=(15, 6.5))

    # 1. Experience vs. Salary by Company Size with Regplot
    sns.scatterplot(
        data=df,
        x="years_experience",
        y="salary_in_usd",
        hue="company_size",
        palette="viridis",
        alpha=0.65,
        s=45,
        ax=axes[0]
    )
    sns.regplot(
        data=df,
        x="years_experience",
        y="salary_in_usd",
        scatter=False,
        color="#0f172a",
        line_kws={"linewidth": 2.5, "label": "Market Trend (95% CI)"},
        ax=axes[0]
    )
    axes[0].yaxis.set_major_formatter(lambda x, pos: f"${int(x/1000)}k")
    axes[0].set_title("A. Experience vs. Base Salary by Company Scale", fontsize=12, fontweight="bold", pad=10)
    axes[0].set_xlabel("Years of Industry Experience", fontsize=10, fontweight="bold")
    axes[0].set_ylabel("Annual Base Salary (USD)", fontsize=10, fontweight="bold")
    axes[0].legend(title="Company Size", frameon=True, loc="upper left")

    # 2. Total Comp vs Equity Trajectory by Role
    top_roles = ["AI Research Scientist", "ML Engineer", "Cloud Architect", "Software Engineer"]
    df_top = df[df["job_title"].isin(top_roles)]

    sns.lineplot(
        data=df_top,
        x="years_experience",
        y="total_compensation",
        hue="job_title",
        palette="tab10",
        linewidth=2.5,
        errorbar=("ci", 95),
        ax=axes[1]
    )
    axes[1].yaxis.set_major_formatter(lambda x, pos: f"${int(x/1000)}k")
    axes[1].set_title("B. Total Compensation Growth Curves (95% Bootstrap CI)", fontsize=12, fontweight="bold", pad=10)
    axes[1].set_xlabel("Years of Industry Experience", fontsize=10, fontweight="bold")
    axes[1].set_ylabel("Total Annual Compensation (USD)", fontsize=10, fontweight="bold")
    axes[1].legend(title="Specialization", frameon=True, loc="upper left")

    plt.tight_layout()
    output_path = os.path.join(FIGURES_DIR, "03_experience_vs_comp_regplot.png")
    plt.savefig(output_path, dpi=300)
    plt.close()
    print(f"[OK] Saved Relational Regression Plot to: {output_path}")
    return output_path
