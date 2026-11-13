# Growfinix Internship – Task 4
## IPL Sports Data Analysis using Python

### Project Overview
This project analyzes historical Indian Premier League (IPL) cricket match data using Python. It uses Pandas for data analysis and Matplotlib for data visualization.

The project explores team performance, win rates, Kolkata Knight Riders (KKR) performance, and IPL toss decisions.

### Objectives
- Analyze historical IPL match data.
- Calculate matches played and matches won by each team.
- Calculate team win percentages.
- Analyze Kolkata Knight Riders' performance.
- Examine toss decisions and match outcomes.
- Generate visualizations using Matplotlib.

### Technologies Used
- Python
- Pandas
- Matplotlib
- CSV Dataset
- Visual Studio Code

### Project Structure

```text
Growfinix-Task4-IPL-Analysis/
│
├── main.py
├── matches.csv
├── outputs/
│   ├── team_performance.csv
│   ├── toss_analysis.csv
│   ├── team_wins.png
│   ├── kkr_season_wins.png
│   └── toss_decisions.png
│
└── README.md
```

### Features

**1. IPL Dataset Analysis**
- Reads historical IPL match data.
- Displays dataset information and records.

**2. Team Performance Analysis**
- Calculates total matches played.
- Calculates total matches won.
- Calculates team win percentages.

**3. KKR Performance Analysis**
- Filters Kolkata Knight Riders match records.
- Calculates total KKR wins.
- Analyzes KKR wins by season.

**4. Toss Decision Analysis**
- Analyzes bat and field decisions.
- Calculates how often the toss-winning team also won the match.

**5. Data Visualization**
- IPL team wins bar chart.
- KKR season-wise wins bar chart.
- Toss decision pie chart.

### Installation

Install Python and the required libraries.

```bash
pip install pandas matplotlib
```

### How to Run

1. Download or clone this repository.
2. Place the IPL dataset file named `matches.csv` in the project folder.
3. Open the project in Visual Studio Code.
4. Open the terminal.
5. Run the following command:

```bash
python main.py
```

### Output

The program generates:
- Team performance CSV report.
- Toss analysis CSV report.
- IPL team wins chart.
- KKR season-wise wins chart.
- Toss decision distribution chart.

All generated files are saved inside the `outputs` folder.

### Learning Outcomes
- Python programming fundamentals.
- Data cleaning and manipulation using Pandas.
- Data analysis using CSV files.
- Data visualization using Matplotlib.
- Working with real-world sports datasets.

### Internship Information

**Organization:** Growfinix Technology  
**Internship Domain:** Python Development  
**Project:** Task 4 – Sports Data Analysis with Pandas

### Conclusion

This project demonstrates how Python can be used to analyze historical IPL cricket data, identify team performance trends, and present meaningful insights through visualizations.

---

Developed as part of the Growfinix Python Development Internship.
