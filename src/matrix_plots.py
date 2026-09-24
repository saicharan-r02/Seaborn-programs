import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

FIGURES_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "figures")

def plot_matrix_and_clustermaps(df: pd.DataFrame) -> tuple[str, str]:
    """
    Generates Hierarchical Clustermaps and Correlation Heatmaps.
    """
    os.makedirs(FIGURES_DIR, exist_ok=True)
    sns.set_theme(style="white")
    plt.rcParams.update({"figure.dpi": 300})

    # 1. Clustermap: Median Salary by Role vs Primary Skill
    pivot_matrix = df.pivot_table(
        index="job_title",
        columns="primary_skill",
        values="salary_in_usd",
        aggfunc="median"
    ).fillna(df["salary_in_usd"].median()) / 1000

    cluster_grid = sns.clustermap(
        pivot_matrix,
        cmap="mako",
        annot=True,
        fmt=".0f",
        linewidths=0.7,
        cbar_kws={"label": "Median Salary ($k USD)"},
        figsize=(11, 9),
        dendrogram_ratio=(0.15, 0.15),
        cbar_pos=(0.02, 0.8, 0.03, 0.15)
    )
    cluster_grid.fig.suptitle("Hierarchical Clustering of Tech Roles & Skill Premiums ($k USD)",
                              fontsize=13, fontweight="bold", y=0.98)
    
    path_cluster = os.path.join(FIGURES_DIR, "04_skills_compensation_clustermap.png")
    cluster_grid.savefig(path_cluster, dpi=300)
    plt.close()
    print(f"[OK] Saved Clustermap to: {path_cluster}")

    # 2. Correlation Matrix Heatmap
    num_cols = ["years_experience", "salary_in_usd", "equity_grant_usd", "total_compensation",
                "work_life_balance_rating", "career_growth_rating"]
    corr_matrix = df[num_cols].corr()

    # Pretty labels
    pretty_labels = ["Experience (Yrs)", "Base Salary", "Equity Grant", "Total Comp", "WLB Rating", "Growth Rating"]

    plt.figure(figsize=(8.5, 7))
    sns.heatmap(
        corr_matrix,
        annot=True,
        fmt=".2f",
        cmap="coolwarm",
        vmin=-0.2,
        vmax=1.0,
        xticklabels=pretty_labels,
        yticklabels=pretty_labels,
        linewidths=1.0,
        cbar_kws={"label": "Pearson Correlation (r)"}
    )
    plt.title("Correlation Matrix of Compensation & Career Satisfaction Metrics", fontsize=12, fontweight="bold", pad=12)
    plt.tight_layout()

    path_corr = os.path.join(FIGURES_DIR, "05_correlation_heatmap.png")
    plt.savefig(path_corr, dpi=300)
    plt.close()
    print(f"[OK] Saved Correlation Heatmap to: {path_corr}")

    return path_cluster, path_corr
