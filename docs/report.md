# DATA 606 Capstone in Data Science
## PROJECT TITLE: SENTIMENTAL ANALYSIS OF ONLINE REVIEWS
## AUTHOR: VIHAAN SUBHASH MATTURI

### INTODUCTION:

Online reviews are becoming a more significant factor in customer decision-making in the current digital era because they are the rich source of text data that may be examined to learn what customers think and feel about a product or service.For businesses looking to better understand their clients and enhance their offerings and services, this information can be helpful. Understanding customers ideas, feedback, and experiences with a company's goods or services is made possible through the sentiment analysis of online reviews, which can be helpful for making adjustments, spotting trends, and making wise judgments. Online reviews may be used to assess a product or service's quality, to contrast similar goods or services, and to gain an understanding of what other customers thought of a certain good or service.

Sentiment analysis is a technique for extracting the sentiment, or emotional tone, of a piece of words.Sentiment analysis may be used to determine if a review is Positive or Negative, to gauge the overall sentiment of a group of reviews, and to pinpoint the major topics that are brought up in a group of reviews.The goal of the sentiment analysis model of online reviews is to automatically recognize and categorize the sentiment indicated in a written text as positive, negative, or neutral.

Link To PPT : https://github.com/DATA-606-SPRING-2023-THU/VihaanSubhash_DATA606/blob/main/docs/capstone.pptx

Link to video : https://youtu.be/v8zno_vmPVo

### Project Goals:


This project's objectives are to:

1.Learn how to evaluate internet reviews using sentiment analysis.
2.Create a sentiment analysis model that can be used to forecast how fresh reviews would feel.
3.Make a web application that may be used to display the sentiment analysis findings.

This project answers the following questions:

1.How do the sentiments of online reviews vary by product category?
2.How do the sentiments of online reviews vary by brand?
3.How can sentiment analysis be used to improve the customer experience?
4.How can sentiment analysis be used to help businesses make better decisions?

### Project Process:

The project's processing was based on a systematic approach of sentiment analysis. It guarantees that the data is accurate and that the model has been appropriately trained and assessed. This makes it possible to confidently forecast the sentiment regarding new reviews and helps to guarantee that the model is correct.

1.Data collection: Collecting the data is the first stage. The data used in this instance is a collection of online reviews for products purchased from Internet. 
2.Data cleaning  : After data has been collected, it must be cleansed. This means clearing up any mistakes or inconsistencies in the data. You might need to delete reviews that are spam or that don't pertain to your question.
3.Data preprocessing : Preprocessing is required once the data has been cleaned. This entails converting the data into a format that the sentiment analysis model can utilize. For example, you may need to convert the text of the reviews to lowercase and remove stop words.
4.Model training : The next step is to train the sentiment analysis model. It involves applying the training data to teach the model how to recognize positive and negative sentiment.
5.Model evaluation : It's important to evaluate the model after it's been trained. This involves using the test data to assess how well the model works.
6.Model deployment : The model may be deployed after being tested. In order for users to use the model to predict the sentiment of new reviews, it must be made available to them.

Jupyter Notebooks and Python were widely used at all phases of the project.


### About the Data Used:

The dataset has been collected https://data.world/datafiniti/grammar-and-online-product-reviews website and is a .csv file consisting of information of over 71,045 online reviews form 1000 different Products provided by Datafiniti's Product Database.

The dataset includes the text and title of the review, the name and manufacturer of the product, reviewer metadata, and more.

Researchers and companies looking to better understand how customers feel about goods and services might benefit greatly from the data gathering. Uses for the dataset include:

1.Determine the recurrent topics in online reviews.
2.Analyze the overall senitiment of a group of reviews.
3.Determine the major variables that affect how consumers feel.
4.Create sentiment analysis models that can be used to forecast the sentiment of fresh reviews.

### Unit of analysis:

This project's unit of analysis is the review_text which containing the reviewer's views and ideas regarding a good or service. The sentiment analysis model will be used to predict the sentiment of fresh reviews after being trained on a dataset of online reviews. The unit of analysis is crucial because it influences how the data is gathered, processed, and interpreted. 


### Preparation Challenges:

1.This project included significant data cleaning and preparation challenges.
2.It was difficult to extract seller information from the url since the data is often not structured consistently. 
3.Certain texts are subjective, which means they reflect the author's viewpoint. Because of this, it could be challenging for NLP systems to accurately determine a text's sentiment.
4.Since natural language can be ambiguous, it can be challenging for NLP algorithms to accurately determine a text's attitude.
5.Significant demand on computer resources and long processing times due to a huge amount of data.


### Data Cleaning:

Check that the data types are accurate.
Examine any missing values. This helps control for errors.
Check the column names. This facilitates the selection of data.

### Data Preparation:

The dataset must first be cleaned and prepared before analysis. A model that works depends mostly on a clean dataset rather than just a good algorithm. Text Data Processing uses several techniques, including:

1.Remove any characters other than white space and alphanumerics.
2.To treat the words equally, change all of the letters to lowercase.
3.Considering lemmatization, stemming, and tokenization.

 ### Data Visualization:

1.Distribution of 5-star ratings by brand

Created a pie chart that displays the quantity of 5-star reviews for each brand to demonstrate the distribution of 5-star ratings by brand. This would provide a thorough summary of the most well-liked brands among consumers.

2.Distribution of 1-star ratings by brand

Created a pie chart that displays the quantity of 1-star reviews for each brand to demonstrate the distribution of 1-star ratings by brand.This would provide you a clear picture of which brands are least beloved by consumers.

3.Determining the average rating for each brand

To get the average rating for each brand, sum up the stars for each and divide by the total number of reviews for each. This would provide you with an accurate measure of how consumers see each brand generally.

4.Getting the number of words by splitting them by a space

You might divide a review by a space and count the number of strings that arise to determine how many words are contained in the review. This would provide you with a reliable estimate of the review's length.

### Extracting features from text documents:

We used three distinct feature extraction models such as Bag of Words, Topic modeling, and Word Embeddings to perform text classification (NLP).Machine learning algorithms can utilize the data from these attributes as training data. It builds a vocabulary out of all the distinct terms that appear in every text in the dataset. 

## Building  Machine Learning Models:


we compared the results of their prediction accuracies by using the two models Logistic Regression and Random Forest to categorize text as either exhibiting positive or negative sentiment (1 or 0): 

### Bag of Words Model with 3 gram:

f1 score for the model logistic_Regression :  0.98
f1 score for the model Random Forest :  0.97

### Word Embedding Model with glove data:

f1 score for the model word embedding :  0.96

Best model is determained as Bag of words model with Logistic Regression


### Deployment:

Initially, A user interface was created to allow individuals to interact with the model and receive predicted sentiment.For this deployment, best performing model is used and interface is most likely in the form of a notebook or console, into which users can enter text and receive predicted sentiment as output.

After creating the user interface,a web application is constructed that incorporates the sentiment analysis model using the Streamlit Python library, which allowed to create a more user-friendly web interface for the sentiment analysis model.

## Conclusion:

It can be conluded that sentiment analysis can be a powerful tool for companies to understand their customers' opinions and feelings. Businesses can obtain insights into their consumers' attitudes regarding their products or services by evaluating internet reviews, and utilize this knowledge to improve their offers and make better decisions.

Sentiment analysis can be used to answer important questions such how sentiments differ by product category and brand, and how it can be used to improve the customer experience. The usage of a web application to present sentiment analysis findings can make it easier for businesses to evaluate and act on sentiment analysis insights.

Businesses that include sentiment research into their decision-making processes can gain a competitive advantage by enhancing client happiness and loyalty, and thereby revenue and profitability.









