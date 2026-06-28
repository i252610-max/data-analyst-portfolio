# Project 3 - SQL Data Analysis

## Overview
Queried Superstore retail database using SQL 
inside Python to extract business insights.

## Tools
Python, SQLite3, Pandas, SQL

## Queries written
- Sales and profit by region
- Average profit by category  
- Top 10 sub-categories by sales
- Order count analysis

## Key SQL Findings

1. California is the top state by sales at $457,687
2. Furniture has lowest avg profit at $8.69 
   despite $741K in total sales
3. Discount analysis reveals serious profitability problem:
   - No discount: avg profit $66.98 — healthy
   - Low discount: avg profit $26.58 — declining  
   - Medium discount: avg profit -$77.86 — losing money
   - High discount: avg profit -$106.70 — worst performer
4. Recommendation: Company should eliminate medium 
   and high discounts immediately