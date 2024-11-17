# Pomegranate-NatHACKS2024

## Authors:
**- Aaron Chiu**
**- Chidinma Amogu**
**- Dave K**
**- Grace Shin**
**- Karina Zhang**
**- Marcus Kim**

  
## Installation and running

1. Clone the repository
2. Create a python virtual environment (python -m venv env)
3. Activate the virtual environment (env\Scripts\activate)
4. Install the requirements (pip install -r requirements.txt)
5. Navigate to the django directory (cd pomegranate-django)
6. Run the app (python manage.py runserver)

## Hackathon Submission Write-up:
In an age where social media algorithms prioritize conflict and negativity to boost engagement, PomApp hopes to offer a new kind of social media experience. Recent trends in social media usage have shown an increase in a phenomenon called “doom-scrolling”, where users become trapped in a cycle of negative and hateful content, leading to feelings of sadness, anger, and fear.

PomApp will stop doom-scrolling in its tracks by reading and monitoring users’ brain EEG signals during app use. The app will identify the user's emotional reactions to posts, categorizing them as “positive,” “negative,” or “neutral”, immediately removing posts that incur negative responses from their feed. Eventually, this will lead to personalized feeds featuring only content that generates positive or neutral emotional reactions. 

The EEG readings are collected from four electrodes connected to a Ganglion device. The readings are transformed into 988 different features through a series of calculations. We then run the live data through a model trained on a dataset of EEG signals recorded during positive, negative, and neutral emotional states. The model determines whether the readings are consistent with a positive, negative, or neutral emotional state, and the algorithm will react accordingly. 

For now, the goal of our submission is to show proof of concept, so our app and algorithm are not robustly developed. These aspects will be our next steps going forward, but we are incredibly proud of the work we have accomplished concerning baseline emotional recognition and are excited to develop this app and this idea further, as we believe it could be the future of healthy social media usage.

## Dev-Post Submission Link:
https://devpost.com/software/pomapp?ref_content=user-portfolio&ref_feature=in_progress
