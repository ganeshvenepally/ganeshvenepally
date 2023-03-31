import os
import pandas as pd
import yfinance as yf
from datetime import datetime, timedelta

def get_trading_dates(start_date, end_date):
    trading_dates = pd.bdate_range(start_date, end_date, freq='W')
    return trading_dates

def record_data(date, ETF_price, shares_purchased, total_investment, total_shares, final_results=False):
    return {
        'date': date,
        'ETF_price': ETF_price,
        'shares_purchased': shares_purchased,
        'total_investment': total_investment,
        'total_shares': total_shares,
        'final_results': final_results
    }

def calculate_final_results(data_records):
    last_record = data_records[-1]
    total_investment = last_record['total_investment']
    total_shares = last_record['total_shares']
    ETF_price = last_record['ETF_price']
    final_portfolio_value = total_shares * ETF_price

    ROI = (final_portfolio_value - total_investment) / total_investment

    max_portfolio_value = 0
    max_drawdown = 0
    for record in data_records:
        portfolio_value = record['total_shares'] * record['ETF_price']
        max_portfolio_value = max(max_portfolio_value, portfolio_value)
        drawdown = (max_portfolio_value - portfolio_value) / max_portfolio_value
        max_drawdown = max(max_drawdown, drawdown)

    return {
        'total_investment': total_investment,
        'total_shares': total_shares,
        'final_portfolio_value': final_portfolio_value,
        'ROI': ROI,
        'max_drawdown': max_drawdown,
    }

def DCA(ETF_ticker, start_date, end_date, weekly_investment):
    trading_dates = get_trading_dates(start_date, end_date)
    ETF_data = yf.download(ETF_ticker, start=start_date, end=end_date, progress=False)
    
    data_records = []

    for date in trading_dates:
        if date not in ETF_data.index:
            date = date + timedelta(days=1)
            while date not in ETF_data.index:
                date = date + timedelta(days=1)
        
        ETF_price = ETF_data.loc[date, 'Close']
        shares_purchased = weekly_investment / ETF_price
        total_investment = (len(data_records) + 1) * weekly_investment
        total_shares = sum([record['shares_purchased'] for record in data_records]) + shares_purchased
        
        data_records.append(record_data(date, ETF_price, shares_purchased, total_investment, total_shares))

    final_results = calculate_final_results(data_records)
    data_records.append(record_data(None, None, None, final_results['total_investment'], final_results['total_shares'], final_results=True))

    return data_records, final_results

ETF_ticker = 'QQQ'
start_date = '2022-01-01'
end_date = '2023-3-31'
weekly_investment = 500

data, final_results = DCA(ETF_ticker, start_date, end_date, weekly_investment)

df = pd.DataFrame(data)
print(df)

# Create a folder for the output file if it doesn't exist
output_folder = 'DCA'
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Save the DataFrame as a CSV file
output_file = os.path.join(output_folder, 'DCA_data.csv')
df.to_csv(output_file, index=False)

print(f"Total investment: ${final_results['total_investment']:.2f}")
print(f"Total shares: {final_results['total_shares']:.2f}")
print(f"Final portfolio value: ${final_results['final_portfolio_value']:.2f}")
print(f"ROI: {final_results['ROI'] * 100:.2f}%")
print(f"Max Drawdown: {final_results['max_drawdown'] * 100:.2f}%")

