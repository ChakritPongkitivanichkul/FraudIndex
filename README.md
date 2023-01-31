# FraudIndex
Regarding Thai academic fraud in 2023, I would like to contribute a bit by introducing a metric which can be used to measure how many connections between a person of interest and people who commit academic fraud.

# Definition
We start by counting how many connections between a person of interest and people who commit academic fraud.
The Fraud Index = number of connections - 1
For example, Alice has a paper with a person who commit academic fraud. Alice has 1 connection-> Alice has Fraud Index of 0
Bob has a paper with Alice. Bob has 2 connections -> Bob has Fraud Index of 1

# Requirement
1. System: You need python with numpy + pandas package
2. File: Exported data of a person of interest from Scopus --> Read how to export file below..

# How to run
Using command:
python distance.py scopus.csv

# How to export file
1. Go to Scopus and search the person of interest
2. Scroll down to the documents section and click at "Export all"
3. The pop up screen (Export document settings) will appear, then choose CSV (Excel) and export
4. Put scopus.csv at the same directory of the code
