from deeppavlov import configs, train_model

# Train FAQ model
train_model(configs.faq.fasttext_logreg)
train_model(configs.faq.tfidf_autofaq)
