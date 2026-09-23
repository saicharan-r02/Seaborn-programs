import os
import numpy as np
import pandas as pd

DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data")
DATA_FILE = os.path.join(DATA_DIR, "global_tech_salaries.csv")

def generate_tech_salary_dataset(n_records: int = 2500, random_state: int = 42) -> pd.DataFrame:
    """
    Generates a realistic global tech compensation and workforce trends dataset.
    """
    np.random.seed(random_state)
    os.makedirs(DATA_DIR, exist_ok=True)

    roles = [
        "AI Research Scientist", "ML Engineer", "Data Scientist",
        "Data Engineer", "Cloud Architect", "Software Engineer",
        "DevOps Engineer", "Product Manager", "BI Analyst"
    ]
    role_weights = [0.10, 0.18, 0.20, 0.15, 0.10, 0.12, 0.06, 0.05, 0.04]
    selected_roles = np.random.choice(roles, size=n_records, p=role_weights)

    experience_levels = ["Entry-Level", "Mid-Level", "Senior", "Lead / Principal", "Executive"]
    exp_weights = [0.18, 0.35, 0.32, 0.12, 0.03]
    selected_exp = np.random.choice(experience_levels, size=n_records, p=exp_weights)

    # Years of experience mapped roughly to tier
    yoe_map = {
        "Entry-Level": (1, 3),
        "Mid-Level": (3, 6),
        "Senior": (6, 11),
        "Lead / Principal": (10, 16),
        "Executive": (14, 22)
    }
    years_exp = np.array([np.random.uniform(*yoe_map[tier]) for tier in selected_exp]).round(1)

    work_settings = ["Fully Remote", "Hybrid", "In-Office"]
    selected_settings = np.random.choice(work_settings, size=n_records, p=[0.42, 0.40, 0.18])

    company_sizes = ["Small (<50)", "Medium (50-250)", "Large (250+)"]
    selected_sizes = np.random.choice(company_sizes, size=n_records, p=[0.22, 0.48, 0.30])

    countries = ["United States", "United Kingdom", "Germany", "Canada", "India", "Australia", "Singapore", "France"]
    country_weights = [0.46, 0.15, 0.10, 0.09, 0.08, 0.05, 0.04, 0.03]
    selected_countries = np.random.choice(countries, size=n_records, p=country_weights)

    country_mult = {
        "United States": 1.0,
        "Canada": 0.82,
        "Australia": 0.84,
        "Singapore": 0.80,
        "United Kingdom": 0.76,
        "Germany": 0.74,
        "France": 0.68,
        "India": 0.42
    }

    role_base = {
        "AI Research Scientist": 165000,
        "ML Engineer": 150000,
        "Cloud Architect": 145000,
        "Data Engineer": 135000,
        "Data Scientist": 130000,
        "Software Engineer": 128000,
        "Product Manager": 132000,
        "DevOps Engineer": 125000,
        "BI Analyst": 95000
    }

    skills = ["PyTorch / TensorFlow", "Python & SQL", "AWS / Cloud", "Kubernetes / Go", "R & Statistics", "Java & Spring"]

    salaries = []
    equities = []
    primary_skills = []
    wlb_ratings = []
    growth_ratings = []

    for i in range(n_records):
        role = selected_roles[i]
        exp = selected_exp[i]
        yoe = years_exp[i]
        country = selected_countries[i]
        setting = selected_settings[i]
        size = selected_sizes[i]

        base = role_base[role]
        yoe_boost = 1.0 + (yoe * 0.045)
        c_factor = country_mult[country]
        size_boost = 1.15 if "Large" in size else (1.05 if "Medium" in size else 0.95)
        remote_boost = 1.02 if setting == "Fully Remote" else 1.0

        raw_salary = base * yoe_boost * c_factor * size_boost * remote_boost + np.random.normal(0, 12000)
        salary_usd = int(np.clip(raw_salary, 42000, 395000))
        salaries.append(salary_usd)

        # Equity grant
        eq_prob = 0.85 if exp in ["Senior", "Lead / Principal", "Executive"] else 0.45
        equity = int(salary_usd * np.random.uniform(0.1, 0.45)) if np.random.rand() < eq_prob else 0
        equities.append(equity)

        # Skill selection
        if role in ["AI Research Scientist", "ML Engineer"]:
            skill = np.random.choice(["PyTorch / TensorFlow", "Python & SQL"], p=[0.75, 0.25])
        elif role in ["Cloud Architect", "DevOps Engineer"]:
            skill = np.random.choice(["AWS / Cloud", "Kubernetes / Go"], p=[0.60, 0.40])
        elif role in ["Data Scientist", "BI Analyst"]:
            skill = np.random.choice(["Python & SQL", "R & Statistics"], p=[0.70, 0.30])
        else:
            skill = np.random.choice(skills)
        primary_skills.append(skill)

        # Ratings
        wlb = np.clip(np.random.normal(3.8 if setting == "Fully Remote" else 3.3, 0.7), 1.0, 5.0).round(1)
        growth = np.clip(np.random.normal(3.7, 0.65), 1.0, 5.0).round(1)
        wlb_ratings.append(wlb)
        growth_ratings.append(growth)

    df = pd.DataFrame({
        "employee_id": [f"EMP-{50000 + i}" for i in range(n_records)],
        "job_title": selected_roles,
        "experience_level": selected_exp,
        "years_experience": years_exp,
        "work_setting": selected_settings,
        "company_location": selected_countries,
        "company_size": selected_sizes,
        "primary_skill": primary_skills,
        "salary_in_usd": salaries,
        "equity_grant_usd": equities,
        "total_compensation": np.array(salaries) + np.array(equities),
        "work_life_balance_rating": wlb_ratings,
        "career_growth_rating": growth_ratings
    })

    df.to_csv(DATA_FILE, index=False)
    print(f"[OK] Tech salary dataset generated: {DATA_FILE} ({len(df):,} records)")
    return df

def load_salary_data() -> pd.DataFrame:
    """Loads tech salary dataset."""
    if not os.path.exists(DATA_FILE):
        return generate_tech_salary_dataset()
    return pd.read_csv(DATA_FILE)

if __name__ == "__main__":
    generate_tech_salary_dataset()
