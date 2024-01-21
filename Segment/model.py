# Importing the Libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import colors
import seaborn as sns
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from yellowbrick.cluster import KElbowVisualizer
from sklearn.cluster import KMeans
from io import BytesIO
import base64
import warnings
import sys

if not sys.warnoptions:
    warnings.simplefilter("ignore")
np.random.seed(42)


# model.py

customersdata = pd.read_csv('uploads/data.csv')
def uploaded_file(filename):
    global customersdata
    name = 'uploads/' + filename
    customersdata = pd.read_csv(name)



# Load the dataset
pallet = ["#682F2F", "#9E726F", "#D6B2B1", "#B9C0C9", "#9F8A78", "#F3AB60"]
cmap = colors.ListedColormap(["#682F2F", "#9E726F", "#D6B2B1", "#B9C0C9", "#9F8A78", "#F3AB60"])


# Function to print the original data
def get_header():
    header_list = customersdata.columns.tolist()
    return header_list


# Function to print information about the dataset
def print_info():
    customersdata.info()


# Function to print the count of categories for selected features
def data_count():
    print("Total categories for the Gender feature:\n", customersdata["Gender"].value_counts(), "\n")
    print("Total categories for the Country Education:\n", customersdata["country"].value_counts())


# Function to describe the dataset
def describe():
    customersdata.describe()


# Function to clean the data (null remove, , label encoding, scaling, PCA)
def data_clean():
    dataset = customersdata.dropna()
    s = (dataset.dtypes == 'object')
    object_columns = list(s[s].index)
    LE = LabelEncoder()
    for i in object_columns:
        dataset[i] = dataset[[i]].apply(LE.fit_transform)

    # making a duplicate of the data
    copy_dataset = dataset.copy()

    # Scaling
    standard_scaler = StandardScaler()
    standard_scaler.fit(copy_dataset)
    scaled_dataset = pd.DataFrame(standard_scaler.transform(copy_dataset), columns=copy_dataset.columns)
    scaled_dataset.head()

    # Initiating PCA to reduce dimensions, aka features, to 3
    pca = PCA(n_components=3)
    pca.fit(scaled_dataset)
    PCA_data = pd.DataFrame(pca.transform(scaled_dataset), columns=["col1", "col2", "col3"])
    return PCA_data


def plot_to_img(plt):

    # Save the plot to a BytesIO object
    buffer = BytesIO()
    plt.savefig(buffer, format='png')

    # Encode the image as base64
    plot_data = base64.b64encode(buffer.getvalue()).decode('utf-8')

    plt.close()

    return plot_data
# Function to plot the reduced data in 3D
def reduce_data_plot():
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection="3d")
    ax.scatter(x, y, z, c="maroon", marker="o")
    ax.set_title("A Reduced Dimensional 3D Data Projection")
    plt.show()
    plt.savefig('')


# Function to determine the number of clusters using the elbow method
def determine_clusters():
    Elbow_method = KElbowVisualizer(KMeans(), k=10)
    Elbow_method.fit(PCA_dataset)
    # Elbow_method.show()
    k = Elbow_method.elbow_value_
    # Define K-means model
    kmeans_model = KMeans(n_clusters=k)
    kmeansCluster = kmeans_model.fit_predict(PCA_dataset)

    PCA_dataset["Clusters"] = kmeansCluster


def plot_3dcluster():
    plt.figure()
    ax = plt.subplot(111, projection='3d', label="bla")
    ax.set_title("The Plot Of The Clusters")
    ax.scatter(x, y, z, s=40, c=PCA_dataset["Clusters"], marker='o', cmap='viridis')
    return plt


def plot_against_two(jojo, hoho):
    # between spending and income
    pl = sns.scatterplot(data=PCA_dataset, x=customersdata[jojo], y=customersdata[hoho],
                         hue=PCA_dataset["Clusters"], palette='viridis')
    pl.set_title(f"Cluster's {jojo} and {hoho} Profile")
    plt.legend()
    return plt


def indi_cluster():
    pl = sns.countplot(x=PCA_dataset["Clusters"], palette='viridis')
    pl.set_title("Arrangement Of The Clusters")
    return plt


def plot_data_cluster(data):
    plt.figure()
    pl = sns.countplot(x=customersdata[data], hue=PCA_dataset["Clusters"], palette='viridis')
    plt.show()


def letseeee():
    Personal = ['Gender', 'no_of_transaction', 'country', 'Age']

    for i in Personal:
        plt.figure()
        sns.jointplot(x=customersdata[i], y=customersdata["Spending"], hue=PCA_dataset["Clusters"], kind="kde",
                      palette='viridis')
        plt.show()


# Execute the functions
# header_list = get_header()
# print_info()
# data_count()
# diff_parameter()
# corr()
# describe()
PCA_dataset = data_clean()
x = PCA_dataset["col1"]
y = PCA_dataset["col2"]
z = PCA_dataset["col3"]
# reduce_data_plot()
determine_clusters()
# plot_3dcluster()
# plot_against_Spending()
# plot_data_cluster('country')
