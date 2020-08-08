import pickle
import numpy as np
from flask import Flask,render_template,request
app = Flask(__name__)

@app.route('/index')
@app.route('/')
def home():
    return render_template('index.html')

def ValuePredictor(to_predict_list): 
    to_predict = np.array(to_predict_list).reshape(1, 12) 
    loaded_model = pickle.load(open("model.pkl", "rb")) 
    result = loaded_model.predict(to_predict) 
    return result 

@app.route('/res')  
def res():
	prediction = "No data given for prediction."
	b1 = "The most common symptoms of COVID-19 are fever, tiredness and dry cough."
	b2 = "Some patients may have aches and pains, nasal congestion, runny nose, sore throat or diarrhea."
	b3 = "Some people become infected but don’t develop any symptoms and don't feel unwell."
	b4 = "Most people (about 80%) recover from the disease without needing special treatment."
	b5 = """In any case, if you have fever, cough and difficulty in breathing seek medical care early to reduce the risk of developing a more severe infection and
	be sure to share your recent travel history with your health care provider.""".replace('\n',' ')
	return render_template("result.html", prediction = prediction, b1=b1, b2=b2, b3=b3, b4=b4, b5=b5)

@app.route('/result', methods = ['POST']) 
def result():
	if request.method == 'POST':   
		to_predict_list = request.form.to_dict() 
		to_predict_list = list(to_predict_list.values()) 
		to_predict_list = list(map(int, to_predict_list)) 
		result = ValuePredictor(to_predict_list)         
		if int(result)== 1: 
			prediction ='The risk level is low.'
			b1 = "Continue with regular good hygiene practices."
			b2 = "Wear a mask that covers your nose & mouth in public places."
			b3 = "Use alcohol based sanitizers to clean your hands regularly whenever you are out of home."
			b4 = "Cover your mouth & nose with a tissue whenever you cough or sneeze. Throw used tissues in a lined wastebasket & wash your hands."
			b5 = """Learn about COVID-19 that is a new virus. It spreads by respiratory droplets of an infected person to others with whom they have close 
			contact such as people who live in the same household or those who provide care.""".replace('\n',' ')
		elif int(result)==2: 
			prediction ='The risk level is medium.'
			b1 = "Self-monitor for symptoms for 14 days from last known exposure."
			b2 = "Limit those with whom you have close physical contact (closer than 2 mtrs or 6 ft) to household members & essential caregivers."
			b3 = "Avoid crowded public spaces & places where you cannot easily separate yourself from others if you become ill."
			b4 = "Stay away from seniors & people with chronic medical conditions (e.g. diabetes, lung problems, immune deficiency)."
			b5 = "Do not use public transportation, taxis or rideshares. Else, work from home, if possible."
		elif int(result)==3:     
			prediction ='The risk level is high.'
			b1 = "Self isolate yourself for 14 days from last known exposure."
			b2 = "If symptoms develop, contact your local public health unit."
			b3 = "Wash your hands & use an alcohol based sanitizer before & after touching anything."
			b4 = "Connect socially & ask for help. Stay in touch with friends & family through phone, instant messaging or video chat."
			b5 = "Clean & disinfect frequently touched surfaces in your home such as doorknobs & handles."
		else:     
			prediction ='The risk level is very high.'
			b1 = "Self isolate yourself."
			b2 = "As much as possible, stay in a separate room from other people in your home & use a separate bathroom if you have one."
			b3 = "Immediately contact local public health unit for a COVID test."
			b4 = "Don't panic & ask people around you to sanitize things you have touched."
			b5 = "If the test is positive, ask people around you to home isolate themselves for 14 days."
		return render_template("result.html", prediction = prediction, b1=b1, b2=b2, b3=b3, b4=b4, b5=b5)

if __name__ == "__main__":
    app.run(debug=True)
