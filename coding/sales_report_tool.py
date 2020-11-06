from itertools import groupby

"""
   Sales Report Tool

   Input: Sales transactions (all sales made by a team in a quarter)
   Output: Two sales reports


   Input:


   Output:

    Sales by team:
       a: 2500000
       b: 500000

    Breakdown of top-selling team (a) by salesperson:
       ruslan: 20000000
       jerome: 500000
"""


def aggregate(arr, by_key, sum_value_key):
    res = {}

    for k, values in groupby(arr, key=lambda x: x[by_key]):
        res[k] = sum([item[sum_value_key] for item in values])
    return res


def top(arr, by_key, sum_value_key):
    aggregated = aggregate(arr, by_key, sum_value_key)
    top_value_key = max(aggregated, key=lambda x: aggregated[x])
    return filter(lambda x: x[by_key] == top_value_key, arr)


class SalesReportTool:
    def __init__(self, transactions):
        self.transactions = transactions

    def get_sales_by_team(self):
        return aggregate(self.transactions, 'team', 'amount')

    def get_top_selling_team_breakdown(self):
        top_transactions = top(self.transactions, 'team', 'amount')
        return aggregate(top_transactions, 'salesperson', 'amount')


report = SalesReportTool([
    {"salesperson": "ruslan", "item": "item_a", "amount": 1500000, "team": "a"},
    {"salesperson": "ruslan", "item": "item_b", "amount": 500000, "team": "a"},
    {"salesperson": "jerome", "item": "item_b", "amount": 500000, "team": "a"},
    {"salesperson": "nancy", "item": "item_a", "amount": 500000, "team": "b"}
])
print(report.get_sales_by_team())
print(report.get_top_selling_team_breakdown())
