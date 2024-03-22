import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

def create_institutions_plot():
    years = range(2024, 2034)
    initial_count = 600
    reduction_rate = 0.05
    school_counts = [initial_count * (1 - reduction_rate) ** (year - 2024) for year in years]

    fig, ax = plt.subplots()
    ax.plot(years, school_counts, marker='o', linestyle='-')
    ax.set_title('Forecasted Decrease in Educational Institutions')
    ax.set_xlabel('Year')
    ax.set_ylabel('Number of Educational Institutions')
    return fig

# Function to create the salary distribution plot
def create_salary_distribution_plot():
    salary_ranges = ['10-11k', '11-12k', '12-13k', '13-14k', '14-15k']
    employee_counts = [500, 700, 900, 1100, 800]  # Example data

    fig, ax = plt.subplots()
    ax.bar(salary_ranges, employee_counts, color='skyblue')
    ax.set_title('Salary Distribution of Employees')
    ax.set_xlabel('Salary Range (thousand UAH)')
    ax.set_ylabel('Number of Employees')
    return fig

# Function to create the gasoline price and quality comparison plot
def create_gasoline_comparison_plot():
    gasoline_types = ['Regular', 'Premium', 'Diesel']
    prices = [2.50, 3.00, 2.80]  # Example prices in USD per gallon
    qualities = [3, 4, 3]  # Example qualities (arbitrary scale)

    fig, ax1 = plt.subplots()
    ax1.bar(gasoline_types, prices, color='skyblue')
    ax1.set_ylabel('Price (USD/gallon)', color='skyblue')
    ax1.tick_params(axis='y', labelcolor='skyblue')

    ax2 = ax1.twinx()
    ax2.plot(gasoline_types, qualities, color='orange', marker='o')
    ax2.set_ylabel('Quality (Arbitrary Scale)', color='orange')
    ax2.tick_params(axis='y', labelcolor='orange')

    fig.tight_layout()
    ax1.set_title('Gasoline Price and Quality Comparison')
    return fig

# Function to create the turnover rate plot for six departments
def create_turnover_rate_plot():
    departments = ['Department 1', 'Department 2', 'Department 3', 'Department 4', 'Department 5', 'Department 6']
    turnover_rates = np.random.uniform(low=10, high=20, size=6)  # Example turnover rates (arbitrary scale)

    fig, ax = plt.subplots()
    ax.barh(departments, turnover_rates, color='skyblue')
    ax.set_title('Turnover Rate in Six Departments (September)')
    ax.set_xlabel('Turnover Rate (%)')
    ax.set_ylabel('Department')
    return fig

# Function to create the pie chart showing time distribution
def create_time_distribution_plot():
    labels = ['With Clients', 'Other Activities']
    sizes = [15, 100 - 15]  # Shopkeeper spends 15% of time with clients
    explode = (0.1, 0)  # Explode the first slice (with clients)

    fig, ax = plt.subplots()
    ax.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', startangle=140)
    ax.set_title('Shopkeeper Time Distribution')
    return fig


# Function to create the plot demonstrating the independence between salary bonus and employment tenure
def create_bonus_tenure_independence_plot():
    tenure_years = np.random.randint(1, 30, size=100)  # Example tenure years
    bonus_amounts = np.random.randint(100, 1000, size=100)  # Example bonus amounts

    fig, ax = plt.subplots()
    ax.scatter(tenure_years, bonus_amounts, color='skyblue')
    ax.set_title('Independence Between Bonus and Tenure')
    ax.set_xlabel('Tenure (Years)')
    ax.set_ylabel('Bonus Amount (USD)')
    return fig

# Function to create the turnover rate by age category plot
def create_turnover_age_plot():
    age_categories = ['20-25', '25-30', '30-35', '35-40', '40-45']
    turnover_rates = [15, 18, 25, 20, 17]  # Example turnover rates (arbitrary scale)

    fig, ax = plt.subplots()
    ax.bar(age_categories, turnover_rates, color='skyblue')
    ax.set_title('Turnover Rate by Age Category (Last Year)')
    ax.set_xlabel('Age Category')
    ax.set_ylabel('Turnover Rate (%)')
    return fig

# Function to create the birth rate comparison plot for different regions
def create_birth_rate_comparison_plot():
    regions = ['Western', 'Eastern', 'Northern', 'Southern', 'Central']
    birth_rates = [14, 16, 12, 15, 10]  # Example birth rates (arbitrary scale)

    fig, ax = plt.subplots()
    ax.bar(regions, birth_rates, color='skyblue')
    ax.set_title('Birth Rate Comparison by Region')
    ax.set_xlabel('Region')
    ax.set_ylabel('Birth Rate (per 1000)')
    return fig

# Function to create the profitability trend plot
def create_profitability_trend_plot():
    years = range(2015, 2025)
    profits = [1000, 950, 920, 880, 850, 830, 820, 800, 780, 750]  # Example profits (arbitrary scale)

    fig, ax = plt.subplots()
    ax.plot(years, profits, marker='o', linestyle='-')
    ax.set_title('Profitability Trend of Company Stocks')
    ax.set_xlabel('Year')
    ax.set_ylabel('Profitability')
    return fig

# Function to create the pie chart showing the distribution of funds
def create_fund_distribution_plot():
    sectors = ['Production', 'Marketing', 'Research', 'Administration', 'Others']
    fund_allocation = [50, 20, 15, 10, 5]  # Example fund allocation percentages

    fig, ax = plt.subplots()
    ax.pie(fund_allocation, labels=sectors, autopct='%1.1f%%', startangle=140)
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    ax.set_title('Distribution of Funds Across Sectors')
    return fig

# Function to create the scatter plot showing the relationship between income and salary
def create_income_salary_relationship_plot():
    # Example data
    num_employees = 100
    income_mean = 50000
    income_std = 15000
    salary_mean = 30000
    salary_std = 10000

    np.random.seed(0)
    income = np.random.normal(income_mean, income_std, num_employees)
    salary = np.random.normal(salary_mean, salary_std, num_employees)

    fig, ax = plt.subplots()
    ax.scatter(salary, income, color='skyblue')
    ax.set_title('Relationship Between Income and Salary')
    ax.set_xlabel('Salary (USD)')
    ax.set_ylabel('Income (USD)')
    return fig


# Function to create the bar plot showing the performance of students
def create_student_performance_plot():
    students = ['Student A', 'Student B', 'Student C', 'Student D', 'Student E', 'Student F', 'Student G', 'Student H']
    performance = [80, 85, 70, 75, 78, 90, 82, 83]  # Example performance scores

    fig, ax = plt.subplots()
    ax.bar(students, performance, color='skyblue')
    ax.set_title('Student Performance in August')
    ax.set_xlabel('Students')
    ax.set_ylabel('Performance Score')

    # Highlighting the top two students
    top_performers_indices = sorted(range(len(performance)), key=lambda i: performance[i], reverse=True)[:2]
    for index in top_performers_indices:
        ax.bar(students[index], performance[index], color='orange')  # Highlighting top performers in orange

    return fig
def update_plot():
    plot_type = plot_selector.get()
    if plot_type == 'institutions_plot':
        fig = create_institutions_plot()
    elif plot_type == 'forecast_plot':
        fig = create_forecast_plot()
    elif plot_type == 'salary_distribution_plot':
        fig = create_salary_distribution_plot()
    elif plot_type == 'gasoline_comparison_plot':
        fig = create_gasoline_comparison_plot()
    elif plot_type == 'turnover_rate_plot':
        fig = create_turnover_rate_plot()
    elif plot_type == 'time_distribution_plot':
        fig = create_time_distribution_plot()
    elif plot_type == 'bonus_tenure_independence_plot':
        fig = create_bonus_tenure_independence_plot()
    elif plot_type == 'turnover_age_plot':
        fig = create_turnover_age_plot()
    elif plot_type == 'birth_rate_comparison_plot':
        fig = create_birth_rate_comparison_plot()
    elif plot_type == 'profitability_trend_plot':
        fig = create_profitability_trend_plot()
    elif plot_type == 'fund_distribution_plot':
        fig = create_fund_distribution_plot()
    elif plot_type == 'income_salary_relationship_plot':
        fig = create_income_salary_relationship_plot()
    elif plot_type == 'student_performance_plot':
        fig = create_student_performance_plot()

    fig.tight_layout()
    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.draw()
    canvas.get_tk_widget().grid(row=1, column=0, sticky="nsew")
# Create the main application window
root = tk.Tk()
root.title("Plot Selector")

# Create a frame to contain the dropdown menu and plot
frame = ttk.Frame(root)
frame.pack(fill=tk.BOTH, expand=True)

# Create a dropdown menu for selecting plot type
plot_selector = ttk.Combobox(frame, values=['institutions_plot', 'forecast_plot', 'salary_distribution_plot',
                                           'gasoline_comparison_plot', 'turnover_rate_plot', 'time_distribution_plot',
                                            'bonus_tenure_independence_plot', 'turnover_age_plot', 'birth_rate_comparison_plot',
                                            'profitability_trend_plot', 'fund_distribution_plot', 'income_salary_relationship_plot',
                                            'student_performance_plot'])
plot_selector.set('institutions_plot')
plot_selector.grid(row=0, column=0, padx=10, pady=10)
plot_selector.bind("<<ComboboxSelected>>", lambda event: update_plot())

# Initial plot
fig = create_institutions_plot()
canvas = FigureCanvasTkAgg(fig, master=frame)
canvas.draw()
canvas.get_tk_widget().grid(row=1, column=0, sticky="nsew")

root.mainloop()
