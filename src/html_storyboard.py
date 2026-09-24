import os
import pandas as pd
import datetime

FIGURES_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "figures")

def generate_visual_storyboard_html(df: pd.DataFrame) -> str:
    """
    Builds a standalone, responsive HTML visual storytelling dashboard.
    """
    os.makedirs(FIGURES_DIR, exist_ok=True)
    report_file = os.path.join(FIGURES_DIR, "visual_storyboard.html")

    median_sal = df["salary_in_usd"].median()
    median_tc = df["total_compensation"].median()
    top_role = df.groupby("job_title")["total_compensation"].median().idxmax()
    top_role_tc = df.groupby("job_title")["total_compensation"].median().max()
    remote_wlb = df[df["work_setting"] == "Fully Remote"]["work_life_balance_rating"].mean()
    office_wlb = df[df["work_setting"] == "In-Office"]["work_life_balance_rating"].mean()

    # Role breakdown table
    role_stats = df.groupby("job_title").agg(
        Count=("employee_id", "count"),
        Median_Base=("salary_in_usd", "median"),
        Median_TC=("total_compensation", "median"),
        Avg_Exp=("years_experience", "mean"),
        Avg_WLB=("work_life_balance_rating", "mean")
    ).sort_values("Median_TC", ascending=False).reset_index()

    table_rows = ""
    for _, row in role_stats.iterrows():
        table_rows += f"""
        <tr>
            <td><strong>{row['job_title']}</strong></td>
            <td>{row['Count']:,}</td>
            <td>${row['Median_Base']:,.0f}</td>
            <td><strong>${row['Median_TC']:,.0f}</strong></td>
            <td>{row['Avg_Exp']:.1f} yrs</td>
            <td>{row['Avg_WLB']:.2f} / 5.0</td>
        </tr>
        """

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>VisualPulse — Global Tech Salaries & Workforce Trends Storyboard</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
    <style>
        :root {{
            --bg-body: #07090e;
            --bg-card: rgba(15, 23, 42, 0.85);
            --border-card: rgba(51, 65, 85, 0.4);
            --accent-cyan: #38bdf8;
            --accent-purple: #a855f7;
            --text-main: #f8fafc;
            --text-sub: #94a3b8;
        }}
        * {{ margin: 0; padding: 0; box-sizing: border-box; font-family: 'Inter', sans-serif; }}
        body {{
            background: radial-gradient(circle at top center, #0f172a 0%, #030712 100%);
            color: var(--text-main);
            padding: 35px 20px;
            min-height: 100vh;
        }}
        .container {{ max-width: 1320px; margin: 0 auto; }}
        header {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding-bottom: 25px;
            border-bottom: 1px solid var(--border-card);
            margin-bottom: 35px;
            flex-wrap: wrap;
            gap: 15px;
        }}
        h1 {{
            font-size: 28px;
            font-weight: 800;
            background: linear-gradient(135deg, #38bdf8, #a855f7);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }}
        .badge {{
            background: rgba(168, 85, 247, 0.15);
            border: 1px solid rgba(168, 85, 247, 0.3);
            color: #d8b4fe;
            padding: 6px 14px;
            border-radius: 20px;
            font-size: 13px;
            font-weight: 600;
        }}
        .kpi-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(230px, 1fr));
            gap: 20px;
            margin-bottom: 35px;
        }}
        .kpi-card {{
            background: var(--bg-card);
            border: 1px solid var(--border-card);
            border-radius: 16px;
            padding: 22px;
            backdrop-filter: blur(12px);
        }}
        .kpi-title {{ font-size: 12px; font-weight: 600; color: var(--text-sub); text-transform: uppercase; }}
        .kpi-value {{ font-size: 30px; font-weight: 800; margin: 8px 0; color: #fff; }}
        .kpi-sub {{ font-size: 12px; color: #34d399; font-weight: 500; }}
        
        .gallery-section {{
            margin-bottom: 40px;
        }}
        .section-title {{
            font-size: 20px;
            font-weight: 700;
            margin-bottom: 20px;
            color: #f1f5f9;
        }}
        .grid-2col {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(580px, 1fr));
            gap: 26px;
            margin-bottom: 30px;
        }}
        .grid-1col {{
            margin-bottom: 30px;
        }}
        .visual-card {{
            background: var(--bg-card);
            border: 1px solid var(--border-card);
            border-radius: 16px;
            padding: 22px;
            backdrop-filter: blur(12px);
            transition: transform 0.2s ease;
        }}
        .visual-card:hover {{ transform: translateY(-2px); }}
        .visual-card h3 {{
            font-size: 15px;
            font-weight: 700;
            color: #bae6fd;
            margin-bottom: 6px;
        }}
        .visual-card p {{
            font-size: 13px;
            color: var(--text-sub);
            margin-bottom: 15px;
        }}
        .visual-card img {{
            width: 100%;
            height: auto;
            border-radius: 10px;
            border: 1px solid rgba(255, 255, 255, 0.05);
        }}
        table {{
            width: 100%;
            border-collapse: collapse;
            font-size: 13.5px;
            text-align: left;
        }}
        th {{
            background: rgba(30, 41, 59, 0.7);
            color: var(--text-sub);
            padding: 12px 14px;
            font-weight: 600;
        }}
        td {{
            padding: 12px 14px;
            border-bottom: 1px solid rgba(255, 255, 255, 0.05);
            color: #cbd5e1;
        }}
        footer {{
            text-align: center;
            color: var(--text-sub);
            font-size: 13px;
            margin-top: 40px;
            padding-top: 20px;
            border-top: 1px solid var(--border-card);
        }}
    </style>
</head>
<body>
    <div class="container">
        <header>
            <div>
                <h1>VisualPulse — Statistical Tech Workforce & Compensation Insights</h1>
                <p style="color: var(--text-sub); font-size: 14px; margin-top: 5px;">Publication-Ready Seaborn Statistical Storytelling Suite</p>
            </div>
            <div class="badge">Seaborn 0.13+ Visual Engine</div>
        </header>

        <!-- KPI Metrics -->
        <div class="kpi-grid">
            <div class="kpi-card">
                <div class="kpi-title">Global Median Base Salary</div>
                <div class="kpi-value">${median_sal:,.0f}</div>
                <div class="kpi-sub">Across 8 Tech Markets</div>
            </div>
            <div class="kpi-card">
                <div class="kpi-title">Median Total Comp (TC)</div>
                <div class="kpi-value">${median_tc:,.0f}</div>
                <div class="kpi-sub">Base Salary + Annual Equity Grants</div>
            </div>
            <div class="kpi-card">
                <div class="kpi-title">Highest Compensated Role</div>
                <div class="kpi-value" style="font-size: 22px;">{top_role}</div>
                <div class="kpi-sub">${top_role_tc:,.0f} Median Total Comp</div>
            </div>
            <div class="kpi-card">
                <div class="kpi-title">Remote Work-Life Balance</div>
                <div class="kpi-value">{remote_wlb:.1f} / 5.0</div>
                <div class="kpi-sub">vs. {office_wlb:.1f} / 5.0 for In-Office</div>
            </div>
        </div>

        <!-- Visual Storyboard Gallery -->
        <div class="gallery-section">
            <div class="section-title">📊 Statistical Visualization Gallery</div>
            
            <div class="grid-2col">
                <div class="visual-card">
                    <h3>1. Salary Probability Density (KDE) & Role Boxen Spreads</h3>
                    <p>Evaluates right-skewness and multimodality across experience tiers and role archetypes.</p>
                    <img src="01_salary_distribution_kde.png" alt="Salary KDE Distribution">
                </div>
                <div class="visual-card">
                    <h3>2. Remote Work Pay Equity & Employee Satisfaction</h3>
                    <p>Split-violin distributions demonstrating parity between remote and in-office compensation.</p>
                    <img src="02_remote_work_pay_equity_violin.png" alt="Categorical Equity Violin">
                </div>
            </div>

            <div class="grid-2col">
                <div class="visual-card">
                    <h3>3. Career Experience vs Compensation Trajectories</h3>
                    <p>Linear and polynomial trendlines with 95% bootstrap confidence interval bands.</p>
                    <img src="03_experience_vs_comp_regplot.png" alt="Relational Regplot">
                </div>
                <div class="visual-card">
                    <h3>4. Hierarchical Skill & Specialization Clustermap</h3>
                    <p>Unsupervised hierarchical dendrogram grouping skill domains by salary premiums.</p>
                    <img src="04_skills_compensation_clustermap.png" alt="Hierarchical Clustermap">
                </div>
            </div>

            <div class="grid-2col">
                <div class="visual-card">
                    <h3>5. Compensation & Satisfaction Correlation Heatmap</h3>
                    <p>Pearson correlation coefficients identifying the drivers of career growth satisfaction.</p>
                    <img src="05_correlation_heatmap.png" alt="Correlation Heatmap">
                </div>
                <div class="visual-card">
                    <h3>6. Multi-Faceted Company Scale Analysis (FacetGrid)</h3>
                    <p>Cross-tabulated subplots showing how startup vs enterprise scales affect senior pay.</p>
                    <img src="06_facet_grid_company_size.png" alt="FacetGrid">
                </div>
            </div>

            <div class="grid-1col">
                <div class="visual-card">
                    <h3>7. Joint Bivariate Density & Marginal Distributions (JointGrid)</h3>
                    <p>Comprehensive bivariate scatter distribution with marginal histograms.</p>
                    <img src="07_joint_distribution_marginal.png" alt="JointPlot Marginal">
                </div>
            </div>
        </div>

        <!-- Role Compensation Benchmark Table -->
        <div class="visual-card" style="margin-bottom: 30px;">
            <h3 style="margin-bottom: 16px;">💼 Specialized Role Benchmark Matrix</h3>
            <table>
                <thead>
                    <tr>
                        <th>Job Title</th>
                        <th>Sample Size</th>
                        <th>Median Base Salary</th>
                        <th>Median Total Comp</th>
                        <th>Avg Experience</th>
                        <th>Work-Life Balance</th>
                    </tr>
                </thead>
                <tbody>
                    {table_rows}
                </tbody>
            </table>
        </div>

        <footer>
            VisualPulse Statistical Storytelling Suite • Powered by Seaborn & Matplotlib • Production Ready
        </footer>
    </div>
</body>
</html>
"""
    with open(report_file, "w", encoding="utf-8") as f:
        f.write(html)

    print(f"[OK] Visual Storyboard HTML compiled at: {report_file}")
    return report_file
