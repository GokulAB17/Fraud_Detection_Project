import pickle
from flask import Flask, request, render_template


app = Flask(__name__)


# Model path
#model = pickle.load(open(r"D:\project1\model_RF_upsampled.pkl", "rb"))


@app.route('/')
def home():
    return render_template('index.html')

# Model business logic function
def ValuePredictor():
    print('In function ValuePredictor()')
    return 1
	
	
@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        
        # Store the key and values from page 
        data_from_page = request.form.to_dict()
        print('data from page : ', data_from_page)
        return render_template('index.html', prediction_text='1')
       
        # Prediction model
        # Todo: Need to implement the model business logic in below function
       # prediction = ValuePredictor()
        
        #print('prediction  = ', prediction)
"""        
        if int(prediction) == 1:
            print('Genuine claim = ', prediction)
            prediction = 'Genuine claim'
        else:
            print('Fraud claim = ', prediction)
            prediction = 'Fraud claim'        
"""    
    # Render the prediction result to html page
  
    # comment off if result need to show on different page
    # return render_template('index.html', prediction_text='prediction')


if __name__ == "__main__":
    app.run(debug=True)
