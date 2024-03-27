import argparse
import pandas as pd
import json
import requests

url_env = {
    'Development': "https://myhostname.com/v1/customers",
    'Staging': "https://myhostname.com/v1/customers",
    'Production': "https://myhostname.com/v1/customers"
}


def create_json(group):
    """
    Create JSON Template for customer data
    :param group: type=Dataframe, Grouped Dataframe that contains customer data
    :return: JSON
    """
    customer_json = {
        'salutation': group['salutation'].iloc[0],
        'last_name': group['last_name'].iloc[0],
        'first_name': group['first_name'].iloc[0],
        'email': group['email'].iloc[0],
        'purchases': group[['product_id', 'price', 'currency', 'quantity', 'purchased_at']].to_dict('records')
    }
    return customer_json


def process_data(customers_df: pd.DataFrame, purchases_df: pd.DataFrame):
    """
    Process Customers et Purchases Data
    :param customers_df: type=Dataframe, Dataframe of Customers Data
    :param purchases_df: type=Dataframe, Dataframe of Purchases Data
    :return: List of JSON
    """
    new_df = pd.merge(customers_df, purchases_df, on='customer_id')
    new_df.rename(columns={'lastname': 'last_name', 'firstname': 'first_name', 'date': 'purchased_at'}, inplace=True)
    new_df['salutation'] = new_df['title'].map({1: 'Female', 2: 'Male'})
    new_df['currency'] = new_df['currency'].map({'EUR': 'euro', 'USD': 'dollars'})
    result = new_df.groupby('customer_id').apply(create_json, include_groups=False).tolist()
    print(json.dumps(result, indent=3))
    return result


def main():
    parser = argparse.ArgumentParser(description='Exam - Customers & Purchases')
    parser.add_argument('--customers_file', type=str, required=True, help='Path to Customers CSV file')
    parser.add_argument('--purchases_file', type=str, required=True, help='Path to Purchases CSV file')
    parser.add_argument('--environment', type=str, required=True, help='Environment must be : Development, Staging, '
                                                                       'Production',
                        choices=['Development', 'Staging', 'Production'])
    args = parser.parse_args()

    try:
        customers_df = pd.read_csv(args.customers_file, delimiter=';')
        purchases_df = pd.read_csv(args.purchases_file, delimiter=';')
        result_data = process_data(customers_df, purchases_df)
        response = requests.put(url_env[args.environment], json=result_data,
                                headers={"Content-Type": "application/json"})
        if response.status_code == 200:
            print("Data sent successfully.")
        else:
            print(f"Failed to send data. Status code: {response.status_code}")

    except FileNotFoundError as e:
        print(f"File not found error: {str(e)}")
    except Exception as e:
        print(f"Error: {str(e)}")


if __name__ == '__main__':
    main()
