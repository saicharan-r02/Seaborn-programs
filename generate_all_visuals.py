import os
from src.data_manager import load_salary_data
from src.distribution_plots import plot_salary_distributions
from src.categorical_plots import plot_categorical_insights
from src.relational_plots import plot_relational_trajectories
from src.matrix_plots import plot_matrix_and_clustermaps
from src.multi_grid_plots import plot_multi_grid_visuals
from src.html_storyboard import generate_visual_storyboard_html

def main():
    print("\n" + "="*70)
    print(" [VisualPulse] Seaborn Tech Workforce & Compensation Insights Suite")
    print("="*70)

    # 1. Load Data
    print("\n[Step 1/6] Ingesting global tech compensation dataset...")
    df = load_salary_data()
    print(f"[OK] Ingested {len(df):,} tech professional profiles.")

    # 2. Distribution Plots (KDE + Boxen)
    print("\n[Step 2/6] Rendering KDE probability densities and Boxen plots...")
    p1 = plot_salary_distributions(df)

    # 3. Categorical Equity Plots (Violin + Bar)
    print("\n[Step 3/6] Generating remote work pay equity violin charts...")
    p2 = plot_categorical_insights(df)

    # 4. Relational & Regression Trajectories
    print("\n[Step 4/6] Plotting experience vs compensation regression trajectories...")
    p3 = plot_relational_trajectories(df)

    # 5. Matrix & Clustermaps
    print("\n[Step 5/6] Generating hierarchical clustermaps & correlation matrices...")
    p4, p5 = plot_matrix_and_clustermaps(df)

    # 6. Multi-Grid FacetGrid & JointGrid
    print("\n[Step 6/6] Rendering FacetGrids, JointPlots & Interactive Storyboard...")
    p6, p7 = plot_multi_grid_visuals(df)
    storyboard_path = generate_visual_storyboard_html(df)

    print("\n" + "="*70)
    print(" [OK] VisualPulse Visualization Suite Generated Successfully!")
    print(f" [INFO] Open the interactive storyboard at: {storyboard_path}")
    print("="*70 + "\n")

if __name__ == "__main__":
    main()
