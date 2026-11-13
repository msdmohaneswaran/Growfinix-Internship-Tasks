
# ==========================================
# GROWFINIX INTERNSHIP - TASK 4
# IPL SPORTS DATA ANALYSIS
# Technologies: Python, Pandas, Matplotlib
# ==========================================

import pandas as pd
import matplotlib.pyplot as plt
import os

print("=" * 55)
print("       GROWFINIX - IPL SPORTS DATA ANALYSIS")
print("=" * 55)

# STEP 1: Create output folder
os.makedirs("outputs", exist_ok=True)

# STEP 2: Load IPL dataset
try:
    df = pd.read_csv("matches.csv")
except FileNotFoundError:
    print("Error: matches.csv not found!")
    print("Place matches.csv inside the project folder.")
    raise SystemExit

# STEP 3: Clean column names
df.columns = df.columns.str.strip()

# Check required columns
required_columns = [
    "team1", "team2", "winner",
    "toss_winner", "toss_decision"
]

for column in required_columns:
    if column not in df.columns:
        print(f"Missing required column: {column}")
        raise SystemExit

# Clean team names
for column in ["team1", "team2", "winner",
               "toss_winner", "toss_decision"]:
    df[column] = df[column].astype("string").str.strip()

# Remove rows without valid team names
df = df.dropna(subset=["team1", "team2"])

# STEP 4: Display dataset information
print("\n1. DATASET INFORMATION")
print("-" * 55)

print("Total matches:", len(df))
print("\nFirst five records:")
print(df.head())

# STEP 5: Calculate matches played
print("\n2. TEAM PERFORMANCE")
print("-" * 55)

team_matches = pd.concat([
    df["team1"],
    df["team2"]
])

matches_played = team_matches.value_counts()

# Calculate total wins
valid_winners = df[
    df["winner"].notna() &
    (df["winner"] != "") &
    (df["winner"].str.lower() != "nan")
]

team_wins = valid_winners["winner"].value_counts()

# Create performance table
performance = pd.DataFrame({
    "Matches Played": matches_played,
    "Matches Won": team_wins
}).fillna(0)

performance["Matches Won"] = (
    performance["Matches Won"].astype(int)
)

performance["Win Rate (%)"] = (
    performance["Matches Won"] /
    performance["Matches Played"] * 100
).round(2)

performance = performance.sort_values(
    by="Win Rate (%)",
    ascending=False
)

print(performance)

# Save team performance
performance.to_csv(
    "outputs/team_performance.csv"
)

# STEP 6: KKR analysis
print("\n3. KOLKATA KNIGHT RIDERS ANALYSIS")
print("-" * 55)

kkr = df[
    (df["team1"] == "Kolkata Knight Riders") |
    (df["team2"] == "Kolkata Knight Riders")
]

kkr_wins = kkr[
    kkr["winner"] == "Kolkata Knight Riders"
]

print("Total KKR matches:", len(kkr))
print("KKR matches won:", len(kkr_wins))

if len(kkr) > 0:
    kkr_win_rate = len(kkr_wins) / len(kkr) * 100
    print("KKR win rate:", round(kkr_win_rate, 2), "%")

# STEP 7: Toss decision analysis
print("\n4. TOSS DECISION ANALYSIS")
print("-" * 55)

toss_data = df.dropna(
    subset=["toss_winner", "winner", "toss_decision"]
).copy()

toss_data = toss_data[
    (toss_data["toss_winner"] != "") &
    (toss_data["winner"] != "")
]

toss_data["Toss and Match Winner Same"] = (
    toss_data["toss_winner"] == toss_data["winner"]
)

toss_summary = toss_data.groupby(
    "toss_decision"
).agg(
    Total_Matches=("winner", "count"),
    Toss_Winner_Also_Won=("Toss and Match Winner Same", "sum")
)

toss_summary["Success Rate (%)"] = (
    toss_summary["Toss_Winner_Also_Won"] /
    toss_summary["Total_Matches"] * 100
).round(2)

print(toss_summary)

toss_summary.to_csv(
    "outputs/toss_analysis.csv"
)

# STEP 8: GRAPH 1 - Team wins
print("\n5. GENERATING GRAPHS")
print("-" * 55)

team_wins.sort_values(
    ascending=False
).plot(
    kind="bar",
    figsize=(12, 6),
    title="IPL Team Total Wins"
)

plt.xlabel("IPL Teams")
plt.ylabel("Total Wins")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()

plt.savefig("outputs/team_wins.png")
plt.show()
plt.close()

# STEP 9: GRAPH 2 - KKR performance
if "season" in df.columns:
    kkr_season = kkr.copy()

    kkr_season["season"] = pd.to_numeric(
        kkr_season["season"],
        errors="coerce"
    )

    kkr_season = kkr_season.dropna(
        subset=["season"]
    )

    seasonal_wins = (
        kkr_season[
            kkr_season["winner"] == "Kolkata Knight Riders"
        ]
        .groupby("season")
        .size()
    )

    if not seasonal_wins.empty:
        seasonal_wins.plot(
            kind="bar",
            figsize=(12, 6),
            title="KKR Wins by IPL Season"
        )

        plt.xlabel("IPL Season")
        plt.ylabel("Matches Won")
        plt.tight_layout()

        plt.savefig("outputs/kkr_season_wins.png")
        plt.show()
        plt.close()

# STEP 10: GRAPH 3 - Toss decisions
toss_counts = toss_data["toss_decision"].value_counts()

toss_counts.plot(
    kind="pie",
    autopct="%1.1f%%",
    figsize=(7, 7),
    title="IPL Toss Decision Distribution"
)

plt.ylabel("")
plt.tight_layout()

plt.savefig("outputs/toss_decisions.png")
plt.show()
plt.close()

print("\n" + "=" * 55)
print("       IPL ANALYSIS COMPLETED SUCCESSFULLY!")
print("=" * 55)

print("\nGenerated files are available in the outputs folder.")
