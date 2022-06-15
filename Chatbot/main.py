# All the imports
import nltk
from nltk.stem.lancaster import LancasterStemmer

stemmer = LancasterStemmer()
import numpy
import tensorflow
import random
import tflearn
import json
import nltk
import pickle

# nltk.download('punkt')

with open("Chat.json") as file:
    data = json.load(file)

# print(data["intents"])

words = []
labels = []
docs_x = []
docs_y = []  # making a new list

# making a loop of words to output the typed statement by the user
for intents in data["intents"]:
    for pattern in intents["patterns"]:
        wrds = nltk.word_tokenize(pattern)
        words.extend(wrds)
        docs_x.append(wrds)
        docs_y.append(intents["tag"])

    if intents["tag"] not in labels:
        labels.append(intents["tag"])

# stemming it to remove duplicaiton and get the root of the word
words = [stemmer.stem(w.lower()) for w in words if w != "?"]
words = sorted(list(set(words)))

labels = sorted(labels)

# neural network dont take string as input we have to convert in numbers
training = []
output = []

out_empty = [0 for _ in range(len(labels))]

for x, doc in enumerate(docs_x):
    bag = []

    wrds = [stemmer.stem(w.lower()) for w in doc]

    for w in words:
        if w in wrds:
            bag.append(1)
        else:
            bag.append(0)

    output_row = out_empty[:]
    output_row[labels.index(docs_y[x])] = 1

    training.append(bag)
    output.append(output_row)

# convert training data in numpy arrays
training = numpy.array(training)
output = numpy.array(output)

# designing model of neural network
# tensorflow.reset_default_graph()  # reset the previous settings

net = tflearn.input_data(shape=[None, len(training[0])])
net = tflearn.fully_connected(net, 8)  # 2 hidden layers which takes input each layer is connected with other
net = tflearn.fully_connected(net, 8)
net = tflearn.fully_connected(net, len(output[0]),
                              activation="softmax")  # output layer have softmax activation which helps to predict the answer it gives percentage of probabilty.
net = tflearn.regression(net)

model = tflearn.DNN(net)

# passing all training data
model.fit(training, output, n_epoch=1000, batch_size=8,
          show_metric=True)  # n_epoch is how many times it will see data. we can increase it or decrease it as per our requirement
model.save("model.tflearn")


# making predictions
def bag_of_words(s, words):
    bag = [0 for _ in range(len(words))]

    s_words = nltk.word_tokenize(s)
    s_words = [stemmer.stem(word.lower()) for word in s_words]

    for se in s_words:
        for i, w in enumerate(words):
            if w == se:
                bag[i] = 1

    return numpy.array(bag)


def chat():
    print("Start talking with the bot (type quit to stop)!")
    while True:
        inp = input("You: ")
        if inp.lower() == "quit":
            break

        results = model.predict([bag_of_words(inp, words)])[0]  # gives probability of the output in percentage
        results_index = numpy.argmax(results)  # gives us the index of the greatest probability to display
        tag = labels[results_index]  # get the tags which have the highest probability

        # if bot gets some random question it wouldn't go gibberish instead response smart
        if results[results_index] > 0.75:  # if the probability is above 70% it will show the response
            for tg in data["intents"]:
                if tg['tag'] == tag:
                    responses = tg['responses']  # choose the response

            print(random.choice(responses))  # randomize the response
        else:  # if probability is less than 70% it will run this block
            print("I didn't understand.")


chat()
