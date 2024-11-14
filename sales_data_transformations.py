import pandas as pd


def read_sales_data():
    sales_data = pd.read_csv('./sales_data_cleaned.csv')
    return sales_data

def sales_data_transformations(sales_data):
    sales_data = sales_data[sales_data['Year'] != 2014]
    sales_data = sales_data[sales_data['Year'] != 2016]
    sales_data['Discount'] = sales_data['Order_Quantity'] * sales_data['Unit_Price'] - sales_data['Revenue']
    return sales_data


if __name__ == '__main__':
    sales_data = read_sales_data()
    sales_data = sales_data_transformations(sales_data)
    print(sales_data.head())