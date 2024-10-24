import gensim

# Load model
def loadModel():
    print("Loading Model...")
    model = gensim.models.Word2Vec.load('./model/model.mdl')
    print("Done Loading Model.")
    return model