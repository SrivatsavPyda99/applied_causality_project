# applied_causality_project

02/28/18 - Did some more research into sentiment analysis on tweets. Identified a dataset that has sentiment analysis as a stock price indicator, but also realized it's too expensive.

03/04/18 - Read more on finding causal relations on data, as well as parsing twitter data. Decided on preliminary graphical model. The next steps are 1) Mine all the data (ALL of Musk's tweets, stock price data, twitter sentiment data, earning report, earning calls from seeking alpha) 2) Run PC algorithm to discover causal graph structure/confirm idea for causal graph structure 3) Run causal inference algorithm on graph.

03/11/18 - Tried out mining scheme using twitter API. Got tweets dating back to 2017. 

03/25/18 - Completed scraping twitter data by using selenium + twitter advanced search to scrape all tweet ids since the beginning of Elon Musk's twitter. Next step is to figure out how to process the tweet ids into usable data. I think this will be a lot of stuff using json.

04/1/18 - Fixed rate limiting issues with data scraping.

04/15/18 - Began reading some works on time series from piazza post (https://piazza.com/class/jrfiy8z1o3h42l?cid=25).

04/23 - Continued reading time series literature.

04/30 - Checked out Bloomberg terminal information on investment banks' company reports. Data was too infrequent for use, but gave some insight on how companies are evaluated. Perhaps twitter sentiment about Tesla can be a substitute for this information.

05/21 - Finished deciding on model and prepped data fully. Re-read chapter 23 of Shalizi to review the estimation process.

05/27 - Finished basic linear regression + backdoor estimation. Began matching. Results were subpar. Next things to try: 1) Sentiment analysis of text tweets as additional data 2) Deep learning for improved regression performance 3) RNN method from time-series paper
