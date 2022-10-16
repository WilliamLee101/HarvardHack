from Parse import professors_dict, students_dict
from sklearn.cluster import KMeans
import numpy as np
from sklearn.cluster import KMeans
from sklearn.cluster import KMeans
from yellowbrick.cluster import KElbowVisualizer
import random
from sklearn.preprocessing import StandardScaler
import pandas as pd
from sklearn.manifold import MDS
import seaborn as sns
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt


def choose_k(samples):
    model = KMeans()
    visualizer = KElbowVisualizer(model, k=(1,15))
    visualizer.fit(samples)       
    visualizer.finalize()
    return visualizer.elbow_value_
    
def run_kmeans():
    for professor in professors_dict:
        input_matrix = []
        for student in students_dict:
            input_vector = []
            
            
        ### we need a key of subject here, and also the number of students is too little
        
            if student["subject"]!= professor["subject"]:
                input_vector.append(0)
            else:
                input_vector.append(5)
                
            if student["gpa"] >= professor["gpa"]:
                input_vector.append(1)
            else:
                input_vector.append(0)
                
            if student["in_person"]==True:
                input_vector.append(1)
            elif professor["in_person"]==False:
                input_vector.append(1)
            else:
                input_vector.append(0)
            
            if student["internship_months"] >= professor["internship_months"]:
                input_vector.append(3)
            else:
                input_vector.append(0)
                
            len_loc = len(professor["location"])
            stud_loc_count = 0
            for stud_loc in student["location"]:
                if stud_loc in professor["location"]:
                    stud_loc_count += 1
            
            if stud_loc_count!=0:
                input_vector.append(1)
            else:
                input_vector.append(0)
            
            if professor["study"] in student["study"]:
                input_vector.append(3)
            else:
                input_vector.append(0)
            
            #print("vector", input_vector)
            input_matrix += [input_vector]

        input_matrix = np.array(input_matrix)
        
        #print("matrix", input_matrix)
        
        scaler = StandardScaler()
        scaled_features = pd.DataFrame(scaler.fit_transform(input_matrix))
        
        pca = PCA(n_components = 0.99)
        pca.fit(scaled_features)
        reduced = pca.transform(scaled_features)
        
        k = choose_k(reduced)
        kmeans = KMeans(n_clusters=k, max_iter = 20,random_state=0)
        label = kmeans.fit_predict(reduced)
        
        result_dict = {}
        for i in range(1000):
            if students_dict[i]["subject"]=="CS":
                if kmeans.labels_[i] not in result_dict:
                    result_dict[kmeans.labels_[i]]=1
                else:
                    result_dict[kmeans.labels_[i]]+=1
        print(result_dict)
        
        break
run_kmeans()
        
        
        
        

        
        
        
        
            