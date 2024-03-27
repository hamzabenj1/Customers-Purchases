# Exam - Customers & Purchases

This project is designed to process customer and purchase data from CSV files and send the data to a REST API based on the provided environment.

## Setup

### Prerequisites
- Python 3.x installed on your system.
- [pip](https://pip.pypa.io/en/stable/installation/) package manager installed.

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/hamzabenj1/Customers-Purchases.git
   ```
   
2. Navigate to the project directory:
   ```bash
   cd Customers-Purchases
   ```
   
3. Create a virtual environment:
   ```bash
   python -m venv venv
   ```
   
4. Activate the virtual environment:
   * Windows:
   ```bash
   venv\Scripts\activate
   ```
   * Linux/macOS:
   ```bash
   source venv/bin/activate
   ```

5. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Run the script
Run the main script with the required arguments (for environment, you can choose Development, Staging, Production. 
Each environment has its own API URL)
   ```bash
   python main.py --customers_file=<path_to_customers_csv> --purchases_file=<path_to_purchases_csv> --environment=<Environment>
   ```

Replace "path_to_customers_csv" and "path_to_purchases_csv" with the paths to your CSV files containing customer and purchases data respectively.
"Environment" should be one of 'Development', 'Staging', or 'Production'.

### Arguments
* --customers_file: Path to the CSV file containing customer data.
* --purchases_file: Path to the CSV file containing purchases data.
* --environment: Environment for sending the data. Must be one of 'Development', 'Staging', or 'Production'.

### Example
   ```bash
   python main.py --customers_file=customers.csv --purchases_file=purchases.csv --environment=Production
   ```