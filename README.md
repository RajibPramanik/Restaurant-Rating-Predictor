## 🍽️ Restaurant-Rating-Predictor

![GitHub](https://img.shields.io/badge/Project-Type-ML%20App-blue) ![GitHub](https://img.shields.io/badge/Language-Python-blue) ![GitHub](https://img.shields.io/badge/Library-Streamlit-red)  

---

### 🚀 **About the Project**
The **Restaurant Rating Predictor** is a machine learning project built using **Python** and **Streamlit**.  
It predicts the average rating of a restaurant based on certain features like:  
✅ **Country**  
✅ **Price Range**  
✅ **Cuisine Type**  
✅ **Online Delivery Availability**  

---

## 🌟 **How It Works**
👉 The model takes input data and predicts the restaurant rating using a pre-trained ML model.  
👉 The user inputs the required details using an interactive Streamlit-based interface.  
👉 Once submitted, the model predicts the restaurant rating and displays the result instantly.  

---

## 🎯 **Features**
✅ Clean and responsive Streamlit-based UI  
✅ Dropdown, slider, and radio buttons for easy input  
✅ Real-time prediction using a pre-trained ML model  
✅ Intuitive animations and user feedback  
✅ Reset button to clear inputs quickly  

---

## 🛠️ **Technologies Used**
- **Python**  
- **Streamlit**  
- **Scikit-learn**  
- **Joblib**  
- **NumPy, Pandas**  
- **Matplotlib, Seaborn**  
- **Plotly**  

---

## 📁 **Project Structure**
```bash
📂 restaurant-rating-predictor
├── 📄 app.py              # Main Streamlit app file
├── 📄 rating_prediction_model.pkl # Pre-trained ML model
├── 📄 README.md           # Project details
```

---

## ⚙️ **Setup Instructions**
### Step 1: Clone the repository  
```bash
git clone https://github.com/your-username/restaurant-rating-predictor.git
cd restaurant-rating-predictor
```

### Step 2: Create a virtual environment  
```bash
python -m venv env
source env/bin/activate  # On Windows: .\env\Scripts\activate
```

### Step 3: Install the dependencies  
```bash
pip install -r requirements.txt
```

### Step 4: Run the Streamlit app  
```bash
streamlit run app.py
```

---

## 🚨 **Usage Instructions**
1. Open the app using the link generated in the terminal.  
2. Enter the details in the input fields:  
   - **Country Code** – Select from the dropdown  
   - **Price Range** – Select from 1 to 4  
   - **Cuisine Type** – Select from the dropdown  
   - **Online Delivery** – Select Yes or No  
3. Click on **🚀 Predict Rating** to get the prediction.  
4. Click on **🔄 Reset** to clear the inputs.  

---

## 📊 **Model Details**
- **Algorithm:** Linear Regression  
- **Training Dataset:** Zomato Restaurant Dataset  
- **Target:** Predicting the aggregate rating of a restaurant  

---

## 🏆 **Example**
| Country Code | Price Range | Cuisine Code | Online Delivery | Predicted Rating |
|-------------|-------------|--------------|-----------------|------------------|
| 1           | 2           | 5            | Yes             | 4.3              |

---

## ✅ **Future Improvements**
- Add more features (e.g., customer reviews)  
- Improve model performance using more complex models  
- Include geographical-based analysis  

---

## 📌 **Contributors**
👨‍💻 **Your Name** – [GitHub](https://github.com/your-username)  

---

## 💡 **Feedback**
If you like this project, please ⭐ the repository!  
For issues or suggestions, open a GitHub issue or reach out.  

---

🔥 **Happy Coding!** 😎
