# Monthly Totals Script

This script reads a CSV file with date ranges and total sums, then calculates how much of each sum falls in each month. It uses a **sweep line** approach and **daily rate distribution** to compute the totals per month.

---

## Features

1. **CSV Input**: Each row must have:
   - A start date (`YYYY-MM-DD`)
   - An end date (`YYYY-MM-DD`)
   - A total sum (numeric, but can include dollar signs and commas)

2. **Monthly Aggregation**:  
   The script outputs the sum of all contributions for each month in the range of dates provided.

3. **Easy to Use**:  
   Just provide the CSV file as a command-line argument, and the script does the rest.

---

## Requirements

- **macOS** (or any system with Python 3 installed)  
- **Python 3** (not included by default on the latest macOS, see below for installation instructions)

---

## Installation

### 1. Install Python 3 (If You Don’t Already Have It)

**Option A: Official Installer**
1. Go to [python.org/downloads](https://www.python.org/downloads/).
2. Click the link for the **latest Python 3 release** for macOS.
3. Download and run the installer.

**Option B: Homebrew (Recommended for Command-Line Users)**
1. [Install Homebrew](https://brew.sh/) by opening Terminal and running:
   ```bash
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```
2. Once Homebrew is installed, run:
   ```bash
   brew install python
   ```
3. Verify Python 3 installation:
   ```bash
   python3 --version
   ```
   You should see something like `Python 3.x.x`.

---

## Usage

1. **Open Terminal**  
   - Press `Command + Space`, type `Terminal`, and hit Enter to launch it.

2. **Navigate to the Script’s Folder**  
   - Use the `cd` command. For example:
     ```bash
     cd /Users/YourName/Desktop/python
     ```
   - Replace the path above with the actual folder where you have `main.py`.
   - **ALTERNATIVELY: you can drag and drop the csv file into your terminal when you're ready to run the script**

3. **Prepare Your CSV File**  
   - Make sure your CSV has rows with three fields:
     1. `start_date` (YYYY-MM-DD)
     2. `end_date` (YYYY-MM-DD)
     3. `total` (numeric—dollar signs and commas are okay, e.g., `$1,234.56`)

   Example CSV content:
   ```csv
   2025-06-02,2025-12-31,$3,045.00
   2025-03-07,2025-12-31,$6,000.00
   2025-07-07,2025-08-07,$5,400.00
   ...
   ```

4. **Run the Script**  
   - Simply run:
     ```bash
     python3 main.py /path/to/your/data.csv
     ```
   - If the path has spaces, you can drag and drop the CSV file into the Terminal after typing:
     ```bash
     python3 main.py 
     ```
     (then press space, drag the file into Terminal, and press Enter).

5. **View the Output**  
   - The script prints each raw row (for debugging) and then shows monthly totals in the format:
     ```bash
     Monthly Totals:
     2025-03: 7422.86
     2025-04: 6363.14
     2025-05: 3137.20
     ...
     ```

---

## Troubleshooting

1. **No Data Processed**:  
   If you see:
   ```
   Monthly Totals:
   No data processed or valid dates not found.
   ```
   - Check that your CSV has the correct format.  
   - Ensure the dates are in `YYYY-MM-DD`.
   - Confirm that the totals column doesn’t have extra text that might break parsing.

2. **Python Not Found**:  
   - Make sure you’ve installed Python 3 correctly.  
   - If `python3 --version` doesn’t work, restart Terminal or re-install Python 3.

3. **CSV Has a Header Row**:  
   - If your CSV’s first line is something like `start_date,end_date,total`, you’ll need to skip it in the script.  
   - Open `main.py`, find the CSV reading section, and **uncomment** (remove the #) from the line:
     ```python
     # next(reader)
     ```
     so it reads:
     ```python
     next(reader)
     ```



