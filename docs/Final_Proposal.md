# DATA 606 Capstone in Data Science
## PROJECT TITLE: SENTIMENTAL ANALYSIS OF ONLINE REVIEWS
## AUTHOR: VIHAAN SUBHASH MATTURI

#### _1)What is your issue of interest (provide sufficient background information)?_

Customer review data is being used as a technique to get insight into consumption-related decisions because understanding the associated emotion gives firms with critical market awareness and the ability to proactively address complaints early.Understanding customers’ ideas, feedback, and experiences with a company's goods or services is made possible through the sentiment analysis of online reviews, which can be helpful for adjusting, spotting trends, and making wise judgments.

#### _2)Why is this issue important to you and/or to others?_

Online reviews are a rich source of text data that may be examined to learn what customers think and feel about a product or service. A consumer's decision to buy something online is greatly impacted by customer reviews, both positive and negative, which provide them with a better understanding of the product's features and functionality and allow them to compare it to similar products. Information on the product and ideas for how the merchant can better their services are also given. For businesses looking to better understand their clients and enhance their offerings and services, this information can be helpful.

#### _3)What questions do you have in mind and would like to answer?_

At the end of my analysis, I would like to answer the following questions.
       
        1.What are the products that need to be adjusted in order to make the customers satisfied?
        
        2.How can a business understand the demand and interests of its customers.

#### 4)Where do you get the data to analyze and help answer your questions (creditability of source, quality of data, size of data, 
attributes of data. etc.)

The dataset has been collected https://data.world/datafiniti/grammar-and-online-product-reviews website and is a .csv file consisting of information of over 71,045 online reviews form 1000 different Products provided by Datafiniti's Product Database. The dataset includes the text and title of the review, the name and manufacturer of the product, reviewer metadata, and more.

#### 5)What will be your unit of analysis (for example, patient, organization, or country)? Roughly how many units (observations) do 
  you expect to analyze?

I will analyze the following units.
        1.name
        2. reviews.source URLs
        3.reviews.text
        4.reviews.tittle
        5.reviews.username

#### _6)What kinds of techniques/models do you plan to use (for example, clustering, NLP, ARIMA, etc.)?_
Four different feature extraction models like Bag of Words, Term Frequency-Inverse Document Frequency (TF-IDF), Word Embeddings and Topic modeling
Machine Learning models like Logistic Regression ,Linear Support Vector Mechanism.

#### _7)How do you plan to develop/apply ML and how you evaluate/compare the performance of the models?_

I would like to use ROC curve and F-1 scores as my performance evaluators.

#### _8)What outcomes do you intend to achieve?_

By the end I would like to develop a sentimental analysis model on the online reviews.

