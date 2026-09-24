import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

FIGURES_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "figures")

def plot_multi_grid_visuals(df: pd.DataFrame) -> tuple[str, str]:
    """
    Generates FacetGrid and JointGrid multi-panel statistical layouts.
    """
    os.makedirs(FIGURES_DIR, exist_ok=True)
    sns.set_theme(style="ticks")
    plt.rcParams.update({"figure.dpi": 300})

    # 1. FacetGrid across Company Size
    g = sns.FacetGrid(
        df,
        col="company_size",
        hue="work_setting",
        palette="Set2",
        height=4.2,
        aspect=1.1,
        col_order=["Small (<50)", "Medium (50-250)", "Large (250+)"]
    )
    g.map_dataframe(
        sns.scatterplot,
        x="years_experience",
        y="salary_in_usd",
        alpha=0.6,
        s=35
    )
    g.set_axis_labels("Years of Experience", "Base Salary ($ USD)")
    for ax in g.axes.flat:
        ax.yaxis.set_major_formatter(lambda x, pos: f"${int(x/1000)}k")
    g.add_legend(title="Work Setting", loc="upper right")
    g.fig.subplots_adjust(top=0.82)
    g.fig.suptitle("Multi-Faceted Analysis: Experience vs Salary Across Company Tiers (FacetGrid)",
                   fontsize=12, fontweight="bold")
    
    path_facet = os.path.join(FIGURES_DIR, "06_facet_grid_company_size.png")
    g.savefig(path_facet, dpi=300)
    plt.close()
    print(f"[OK] Saved FacetGrid Plot to: {path_facet}")

    # 2. JointPlot with Marginal Histograms & KDE Overlay
    jp = sns.jointplot(
        data=df,
        x="years_experience",
        y="salary_in_usd",
        hue="work_setting",
        palette="viridis",
        kind="scatter",
        alpha=0.6,
        marginal_kws=dict(fill=True, common_norm=False),
        height=7.5
    )
    jp.ax_joint.yaxis.set_major_formatter(lambda x, pos: f"${int(x/1000)}k")
    jp.ax_joint.set_xlabel("Years of Industry Experience", fontsize=10, fontweight="bold")
    jp.ax_joint.set_ylabel("Annual Base Salary ($ USD)", fontsize=10, fontweight="bold")
    jp.fig.subplots_adjust(top=0.92)
    jp.fig.suptitle("Joint Distribution & Marginal Density: Experience vs Base Salary (JointGrid)",
                    fontsize=12, fontweight="bold")

    path_joint = os.path.join(FIGURES_DIR, "07_joint_distribution_marginal.png")
    jp.savefig(path_joint, dpi=300)
    plt.close()
    print(f"[OK] Saved JointPlot to: {path_joint}")

    return path_facet, path_joint
