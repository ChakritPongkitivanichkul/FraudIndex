# FraudIndex
Regarding Thai academic fraud in 2023, I would like to contribute a bit by introducing a metric which can be used to measure how many connections between a person of interest and people who commit academic fraud. Last updated data (connections to cases) is on 2 February 2023. The latest version of code: 3 February 2023.

# Definition
- We start by counting how many connections between a person of interest and people who commit academic fraud.
- The Fraud Index = number of connections - 1
- For example, Alice has a paper with a person who commit academic fraud. Alice has 1 connection-> Alice has Fraud Index of 0
- Bob has a paper with Alice but does not have any paper with a person who commit academic fraud. Bob has 2 connections -> Bob has Fraud Index of 1
- Charlie has a paper with Bob but does not have any paper with Alice nor a person who commit academic fraud. Charlie has 3 connections -> Charlie has Fraud Index of 2

# Caveat
- This metric CANNOT be solely used to accuse anyone.
- Any accusation regarding the case should be done in a very careful manner and should be handled by people with authorities.

# Requirement
1. System: You need python with numpy + pandas package
2. File: Exported data of a person of interest from Scopus --> Read how to export the scopus file below..

# How to run
Using command:
python distance.py scopus.csv

# How to export a scopus file
1. Go to Scopus and search the person of interest
2. Scroll down to the documents section and click at "Export all"
3. The pop up screen (Export document settings) will appear, then choose CSV (Excel) and export
4. Put scopus.csv at the same directory of the code

# Evidence
https://www.scopus.com/authid/detail.uri?authorId=57211329338
https://www.scopus.com/authid/detail.uri?authorId=57219950613
https://www.scopus.com/authid/detail.uri?authorId=57214268798
https://www.scopus.com/record/display.uri?eid=2-s2.0-85141999552&origin=resultslist&sort=plf-f
