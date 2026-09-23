import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

FIGURES_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "figures")

def plot_categorical_insights(df: pd.DataFrame) -> str:
    """
    Generates Violin, Strip, and Bar plots evaluating remote work equity and satisfaction.
    """
    os.makedirs(FIGURES_DIR, exist_ok=True)
    sns.set_theme(style="ticks", palette="muted")
    plt.rcParams.update({"figure.dpi": 300})

    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    # 1. Violin Plot: Salary by Work Setting & Experience Tier
    exp_filtered = df[df["experience_level"].isin(["Mid-Level", "Senior", "Lead / Principal"])]
    sns.violinplot(
        data=exp_filtered,
        x="work_setting",
        y="salary_in_usd",
        hue="experience_level",
        palette="crest",
        inner="quartile",
        cut=0,
        ax=axes[0]
    )
    axes[0].yaxis.set_major_formatter(lambda x, pos: f"${int(x/1000)}k")
    axes[0].set_title("A. Remote vs On-Site Salary Equity Across Seniority", fontsize=12, fontweight="bold", pad=10)
    axes[0].set_xlabel("Work Setting", fontsize=10, fontweight="bold")
    axes[0].set_ylabel("Annual Base Salary (USD)", fontsize=10, fontweight="bold")
    axes[0].legend(title="Experience", frameon=True, loc="upper right")

    # 2. Grouped Barplot: Satisfaction Ratings
    melted_ratings = df.melt(
        id_vars=["work_setting"],
        value_vars=["work_life_balance_rating", "career_growth_rating"],
        var_name="Satisfaction_Metric",
        value_name="Rating_Score"
    )
    melted_ratings["Satisfaction_Metric"] = melted_ratings["Satisfaction_Metric"].replace({
        "work_life_balance_rating": "Work-Life Balance",
        "career_growth_rating": "Career Growth Satisfaction"
    })

    sns.barplot(
        data=melted_ratings,
        x="work_setting",
        y="Rating_Score",
        hue="Satisfaction_Metric",
        palette="Blues_r",
        capsize=0.08,
        err_kws={"linewidth": 1.5},
        ax=axes[1]
    )
    axes[1].set_ylim(1.0, 5.0)
    axes[1].set_title("B. Employee Satisfaction by Work Model (1-5 Scale)", fontsize=12, fontweight="bold", pad=10)
    axes[1].set_xlabel("Work Setting", fontsize=10, fontweight="bold")
    axes[1].set_ylabel("Average Rating (with 95% CI)", fontsize=10, fontweight="bold")
    axes[1].legend(title="Metric", frameon=True, loc="lower right")

    plt.tight_layout()
    output_path = os.path.join(FIGURES_DIR, "02_remote_work_pay_equity_violin.png")
    plt.savefig(output_path, dpi=300)
    plt.close()
    print(f"[OK] Saved Categorical Equity Plot to: {output_path}")
    return output_path
