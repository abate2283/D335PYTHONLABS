daily_revenues = [
    2356.23,  # Monday
    1800.12,  # Tuesday
    1792.50,  # Wednesday
    2058.10,  # Thursday
    1988.00,  # Friday
    2002.99,  # Saturday
    1890.75  # Sunday
]

total = 0
for revenue in daily_revenues:
    total += revenue
revenue_average = total/len(daily_revenues)
print(f"Average: {revenue_average:.2f}")
