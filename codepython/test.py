from utils import *
from wordEmbedding import *
print("bat dau")

def predict(text, phobert, tokenizer):
    model = load_model('model.h5')
    X_test = word2vec(text, phobert, tokenizer)
    x_test_tensor = tf.convert_to_tensor(X_test)

    X_tests = []
    X_tests.append(x_test_tensor)

    X_tests =  tf.convert_to_tensor(X_tests)
    y = model.predict(X_tests)
    y_predict = np.argmax(y, axis=-1)

    print(y_predict+1)

if __name__ == "__main__":
    print("1 Chỗ này hơi lâu bạn đợi tí")
    phobert = AutoModel.from_pretrained("vinai/phobert-base")
    print("2")
    tokenizer = AutoTokenizer.from_pretrained("vinai/phobert-base", use_fast=False)
    print("3")
    predict("tôi làm giấy X ở đâu", phobert, tokenizer)
    print("4")
    predict("tôi làm giấy X ở đâu", phobert, tokenizer)
    print("5")
    predict("tôi làm giấy X cần những gì", phobert, tokenizer)
    
    
