# BitcoinDataset-Analysis-using-Pandas-in-Python
Dataset analysis in Bitcoin using Pandas (Jupyter Notebook) in Python. This analysis is based on the bitcoin transaction dataset provided in https://senseable2015-6.mit.edu/bitcoin/

Some of the questions answered are :

1. What is the number of transactions and addresses in the dataset? 

2. What is the Bitcoin address that is holding the greatest amount of bitcoins? How much is that exactly? Note that the address here must be a valid Bitcoin address string. To answer this, you need to calculate the balance of each address. The balance here is the total amount of bitcoins in the UTXOs of an address. 

3. What is the average balance per address? 

4. What is the average number of input and output transactions per address? What is the average number of transactions per address (including both inputs and outputs)? An output transaction of an address is the transaction that is originated from that address. Likewise, an input transaction of an address is the transaction that sends bitcoins to that address. 

5. What is the transaction that has the greatest number of inputs? How many inputs exactly? Show the hash of that transaction. If there are multiple transactions that have the same greatest number of inputs, show all of them. 


6. What is the average transaction value? Transaction value is the sum of all outputs’ value. 

7. How many coinbase transactions are there in the dataset? 

8. What is the average number of transactions per block?




-> Go through the AnalysisResults_Report.pdf for instructions on how to run and report from the analysis. Analysis code for each of the questions answered in the report is given in Code_Part1 and Code_Part2.


