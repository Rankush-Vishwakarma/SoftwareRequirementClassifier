An API to predict the risk category based upon the user requirement.


# SoftwareRequirementClassifier
    This is a Flask API that I will keep improving with new features and functionalities. This is a deep learning based classification API which focus on making software requirement identification easy and fast.

Prioritizing requirements based on risk since it is impossible to test everything. 
Risk-based testing is testing based on the risk of failure and mitigates the risks using test design techniques. 
A Product quality risk can be defined as a potential problem with product quality. 
Product quality risks include  
Functional risks

	1. Non-functional performance risks 
	2. Non-functional usability risks 
	3. Non-Functional Security Risks
	4. Non-Functional Reliability Risks
 
Risk analysis is to be done to evaluate the probability (likelihood) and impact of each risk. Then, the risks are prioritized 
	
 	1. High Risks require Extensive Testing 
	2. Low Risks require only Cursory Testing 

# Dependencies
    1. Python - Programming Language
    2. Flask - The framework used
    3. Tensorflow - deep learning framework
    4. Pip - Dependency Management

# Virtual environment 
    $ sudo apt-get install python-virtualenv
    $ python3 -m venv venv
    $ . venv/bin/activate
    $ pip install Flask

# Install all project dependencies using:
    $ pip install -r requirements.txt

# Install model to you flask repository using;
    https://drive.google.com/drive/folders/1dP0UpnMEKLy-KYSuqZfqPKUdq4izpMr6?usp=sharing

# Running   
    $ export FLASK_APP=api.py
    $ export FLASK_ENV=development
    $ python -m flask run
    
    This launches a very simple builtin server, which is good enough for testing but probably not what you want to use in production.

    If you enable debug support the server will reload itself on code changes, and it will also provide you with a helpful debugger if things go wrong.

     If you have the debugger disabled or trust the users on your network, you can make the server publicly available simply by adding --host=0.0.0.0 to the command line:
      
      -- flask run --host=0.0.0.0
 
 # running from prompt
    We can use and start the WSGI server using conda/python prompt using 
    
    $ python api.py 
    
    or 
    
    $ python manage.py runserver
      
## Contirbuing 
    This API was developed based on:
    
    1. Flask documentation
    
    2. REST APIs with Flask and Python
    
    3. The Ultimate Flask Course
    
    4. Dataset - https://www.kaggle.com/datasets/iamsouvik/software-requirements-dataset
  
## License
    This project is licensed under the MIT License - see the LICENSE.md file for details



## introduction :
    ### Problem:-  The end-user requires some functional and non-functional features into the product
    He/she states these Requirements in the form of Functional and Non-Functional Software Requirements
    For Example 
        Functional Requirement – I would like to be able to accomplish XYZ task using the system
        Non-Functional Requirement – I would like to see performance, security, availability, maintainability and other non-functional features incorporated into the              system (like Authorization, Authentication, Response Time, etc.)
    To test these Requirements, in the form of test cases, we need to determine which requirements to test extensively, and which kind of testing to perform on a specific requirement
    There are certain attributes of a requirement which help us to categorize it into a particular risk category - FURPS
    Functionality 
    Usability
    Reliability (Fault Tolerance)
    Performance
    Security
    -- there are in total we have 12 different function/non-functional categoried but FURPS are the major one .
## Why is this a Problem!
    These Functional and Non-Functional requirements are highly customized based on the software domain, And may have varying degrees of complexity, from simple to highly complex requirements And hence, have a certain degree and type of Risk associated with these software requirements We would like to label these risks And hence, aid in Automated Risk Assessment Just by looking at the requirement, it is difficult to categorize the requirements into a specific risk category,  and might require domain experts from different non-functional testing fields to inspect the requirements Which is not feasible within a specified budget, schedule and limited resources

## I have collected the dataset from Kaggle platform.
    https://www.kaggle.com/datasets/iamsouvik/software-requirements-dataset
    ### Preprocessing 
          The preprocessing is done with the help of different libraries like nltk, spacy, contractions, stopwords, unicodedata. The main aim of the preprocessing step is to clean the text
          The major things we have done in preprocessing are
	            1. normalize the text.
	            2. Removing Unicode Characters
	            3. Removing Stopwords
	            4. Stemming and Lemmatization
	            5. remove punctuations.
	            6. removing special and accented characters
	            7. removing numbers
 
## Machine Learning supervised model strategy 
![image](https://user-images.githubusercontent.com/96487589/171377108-54ec11a1-39a5-42de-8b7c-8b786d0521b9.png)
  ### Model Pipeline creation 
      In this step we have used hybridized model pipeline. This has been created with the help of countVectorizer, TfidfTransformer, and the ML model  itself.
      I have included and test over 7 different ML supervised models. These are – Logistic regression, LinearSVC, DecisionTreeClassifier, RandomForestClassifier, MultinomialNB, KNeighborsClassifier and XGBClassifier.
![image](https://user-images.githubusercontent.com/96487589/171377343-de2b68ae-1b4c-41c6-ae56-ae163addabb2.png)

## Deep learning Architecture
   ### ![image](https://user-images.githubusercontent.com/96487589/171377467-4adef1de-c81d-4bd1-a662-4a895ab346f3.png)
  ### Generating Input ids and Attention mask	
      #### ![image](https://user-images.githubusercontent.com/96487589/171377727-eb320fec-805d-4278-b1a9-6785bbc0c66f.png)

      1. Input ids and Attention mask has been generated with the help of BertTokenizer pretrained model ‘bert-base-cased’ for the “description” column.Input IDs are token indices, numerical representations of tokens building the sequences that will be used as input by the model. 
      2. The attention mask is an optional argument used when batching sequences together.

  ### Base pretrained bert model
    ####
    1. pretrained model: a model that has been pretrained on some data (for instance all of Wikipedia). Pretraining methods involve a self-supervised objective, which can be reading the text and trying to predict the next word (see CLM) or masking some words and trying to predict them (see MLM).
    2. Pretrained model on English language using a masked language modeling (MLM) objective. 
    BERT is a transformers model pretrained on a large corpus of English data in a self-supervised fashion. This means it was pretrained on the raw texts only, with no humans labelling them in any way (which is why it can use lots of publicly available data) with an automatic process to generate inputs and labels from those texts

## Training and Validation 
  ![image](https://user-images.githubusercontent.com/96487589/171377974-ca9edcdd-1239-4d41-9e79-d0cc3e31daaa.png)

  ### Training has been done by hybridizing the pretrained base model with fully connected RNN layer.
    RNN (recurrent neural network) is a type of model that uses a loop over a layer to process texts.
    Bert model comes with self-attention where each element of the input finds out which other elements of the input they should attend to.
   
   
## Future Aspects
  ### 
    1. Detailed degree of Risk (Critical, High, Medium, Low, Cosmetic)
    2. Integration with JIRA and test case management systems to automatically determine the risk associated with a particular software requirement.

  





