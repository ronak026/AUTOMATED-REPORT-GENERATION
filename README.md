# AUTOMATED-REPORT-GENERATION

"Company":CODTECH IT SOLUTIONS

"Name": Ronak Vekariya

"Intern ID":CT04DR535

"Domain":Python Programing

"Duration":4 Weeks

"Mentor":Neela Santosh

A Python script that generates a professional PDF sales performance report from CSV data. It reads sales data, performs basic statistical analysis, and creates a formatted PDF report with tables and insights.

## Features

- Reads sales data from CSV file
- Performs statistical analysis on sales data (mean, count, etc.)
- Generates professional PDF report with formatted tables
- Highlights key insights (average sales, top performer)
- Clean, structured output using ReportLab

## Project Structure

- `generate_report.py`: Main script that processes data and generates PDF
- `data.csv`: Sample sales data (Name, Region, Month, Sales, Profit)
- `report.pdf`: Generated PDF report (created when script runs)
- `requirements.txt`: Python dependencies

## Prerequisites

- Python 3.9+ recommended

## Setup

1. Clone/download the project and open the `Task-2` folder.
2. Create and activate a virtual environment (optional but recommended).
3. Install dependencies:

```bash
pip install -r requirements.txt
```

## Run

From the `Task-2` directory:

```bash
python generate_report.py
```

The script will read `data.csv`, perform statistical analysis, and generate `report.pdf` in the same directory.

## Output

The generated PDF includes:

- **Title**: "Sales Performance Report"
- **Summary Statistics Table**: Count, mean, std, min, max, and quartiles for numerical columns
- **Key Insights**: Average sales figure and top-performing salesperson

## image

<img width="1191" height="938" alt="Screenshot 2025-11-02 101410" src="https://github.com/user-attachments/assets/f01c0b2a-eaa0-4e1c-b322-4d3e41c43e74" />

## Customization

To analyze your own data:

1. Replace `data.csv` with your own CSV file
2. Ensure your CSV has a "Sales" column (and optionally "Name" column for top performer analysis)
3. Run the script as above

## Notes & Troubleshooting

- If you see: `FileNotFoundError: [Errno 2] No such file or directory: 'data.csv'`, ensure `data.csv` exists in the `Task-2` directory.
- The script expects at least one "Sales" column in the CSV for analysis and insights.
- To modify the report styling, edit the TableStyle parameters in `generate_report.py`.

## License

MIT (or as applicable to your project).
