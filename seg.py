import pandas as pd  
from sklearn.cluster import KMeans
import warnings
import pickle
import matplotlib.pyplot as plt
from sklearn.metrics import ConfusionMatrixDisplay
warnings.filterwarnings('ignore')      #prevents windows warning

df=pd.read_csv('Mall_Customers.csv')
X = df[['Annual Income (k$)', 'Spending Score (1-100)']]
kmeans_model=KMeans(n_clusters=5,random_state=42,n_init=10)
kmeans_model.fit(X)

print('Customer Segmentation')
print('Model trained successfully on Mall_Customers.csv (5clusters)\n')

while True:
    user_in=input("enter annual income (k$) and spending score (1-100) separated by a comma or 'q' to quit: ")
    if user_in.lower()=='q':
        print('end of program')
        break
    data=user_in.split(',')
    income=float(data[0])
    spend=float(data[1])

    cluster_id=kmeans_model.predict([[income,spend]])[0]
    print(f"\nPREDICTED CLUSTER :{cluster_id}")
    if cluster_id == 0:
        print("CUSTOMER PERSONA  : Standard Customer")
        print("MARKETING STRATEGY: Maintain engagement with standard promotional offers.")
    elif cluster_id== 1:
        print("CUSTOMER PERSONA  : Premium Target (VIP)")
        print("MARKETING STRATEGY: Primary targets for upsells and new product launches.")
    elif cluster_id ==2:
        print("CUSTOMER PERSONA  : Impulse Spender")
        print("MARKETING STRATEGY: Target with flash sales and limited-time offers.")
    elif cluster_id==3:
        print("CUSTOMER PERSONA  : Careful Spender")
        print("MARKETING STRATEGY: Highlight product durability, ROI, and high quality.")
    elif cluster_id==4:
        print("CUSTOMER PERSONA  : Budget Conscious")
        print("MARKETING STRATEGY: Target with heavy discount campaigns and clearance sales.")

with open('spam_model.pkl', 'wb') as f:
    pickle.dump(model, f)
with open('vectorizer.pkl', 'wb') as f:
    pickle.dump(vecto, f)
disp = ConfusionMatrixDisplay.from_estimator(model, X_test_tfidf, y_test, cmap='Blues')
plt.title("Spam Classifier Confusion Matrix")
plt.savefig('confusion_matrix.png', bbox_inches='tight')
