# 📊 VisualPulse — Global Tech Salaries & Workforce Trends Statistical Visualization Suite

[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![Seaborn](https://img.shields.io/badge/Seaborn-0.13%2B-cyan.svg)](https://seaborn.pydata.org/)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-3.8%2B-blue.svg)](https://matplotlib.org/)
[![Status](https://img.shields.io/badge/Status-Production%20Ready-emerald.svg)]()

A publication-grade statistical data visualization and storytelling suite built with **Seaborn** and **Matplotlib**. It explores global technology workforce dynamics, compensation distributions, remote work pay equity, experience trajectories, skill premiums, and employee satisfaction using advanced statistical plotting techniques.

---

## 📌 Project Highlights

- **Comprehensive Seaborn Spectrum**: Showcases KDE probability densities, Boxen plots, split-violin categorical plots, regression trendlines with 95% bootstrap confidence intervals, hierarchical clustermaps, Pearson correlation heatmaps, FacetGrids, and JointGrids.
- **Publication-Ready Figures**: All charts rendered at 300 DPI with custom palettes (`mako`, `viridis`, `crest`), curated typography, and statistical annotations.
- **Interactive Visual Storyboard**: An aesthetic, self-contained HTML storytelling dashboard presenting full visual galleries and economic conclusions.
- **Archived Practice Library**: Historical daily exercises and exploratory scripts preserved in [`practice_exercises/`](practice_exercises/).

---

## 🏗️ System Architecture

```
Seaborn/
├── practice_exercises/          <- Historical daily Seaborn exercises & scripts
├── data/
│   └── global_tech_salaries.csv <- 2,500+ records across 8 global tech hubs
├── src/
│   ├── data_manager.py          <- Tech compensation dataset synthesis & loader
│   ├── distribution_plots.py    <- KDE & Boxen distribution visualizer
│   ├── categorical_plots.py     <- Violin, Strip & Bar remote equity plots
│   ├── relational_plots.py      <- Regression & confidence interval trajectories
│   ├── matrix_plots.py          <- Hierarchical Clustermap & Correlation Heatmap
│   ├── multi_grid_plots.py      <- FacetGrid & JointPlot marginal densities
│   └── html_storyboard.py       <- Interactive visual gallery & report compiler
├── figures/
│   ├── 01_salary_distribution_kde.png
│   ├── 02_remote_work_pay_equity_violin.png
│   ├── 03_experience_vs_comp_regplot.png
│   ├── 04_skills_compensation_clustermap.png
│   ├── 05_correlation_heatmap.png
│   ├── 06_facet_grid_company_size.png
│   ├── 07_joint_distribution_marginal.png
│   └── visual_storyboard.html
├── generate_all_visuals.py      <- Main one-click visual generator
└── README.md
```

---

## 🚀 Quick Start

### 1. Generate All Figures & Storyboard
```bash
python generate_all_visuals.py
```

### 2. View the Visual Storyboard
Open `figures/visual_storyboard.html` in your web browser.

---

## 🎨 Visualization Catalog

| Output Figure | Chart Types | Key Insight Highlighted |
| :--- | :--- | :--- |
| `01_salary_distribution_kde.png` | Multi-tier KDE & Boxen Plot | Right-skewness & compensation spread across experience tiers and AI/ML roles. |
| `02_remote_work_pay_equity_violin.png` | Split Violin & Bar with CI | Remote vs. On-Site pay equity and work-life balance satisfaction differential. |
| `03_experience_vs_comp_regplot.png` | Scatter with Regplot (95% CI) | Non-linear compensation scaling across enterprise vs startup environments. |
| `04_skills_compensation_clustermap.png` | Hierarchical Clustermap | Unsupervised dendrogram grouping high-value skills (PyTorch, AWS, Kubernetes). |
| `05_correlation_heatmap.png` | Pearson Correlation Heatmap | Quantifying the relationship between equity grants, experience, and satisfaction. |
| `06_facet_grid_company_size.png` | Multi-faceted FacetGrid | Comparative multi-subplot analysis of experience vs salary by company size. |
| `07_joint_distribution_marginal.png` | JointGrid + Marginal Histograms | Bivariate distribution with marginal kernel density estimates. |
