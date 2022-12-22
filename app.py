import os
import streamlit as st
from keras.applications import vgg16
# from keras.preprocessing.image import load_img,img_to_array
from tensorflow.keras.preprocessing.image import load_img
from keras.models import Model
from keras.applications.imagenet_utils import preprocess_input

from PIL import Image
import os,keras
import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
from tensorflow.keras.utils import load_img,img_to_array
from numpy.linalg import norm


imgs_model_width, imgs_model_height = 224, 224
nb_closest_images = 5




def return_image_embedding(img):
     # load the model
     vgg_model = vgg16.VGG16(weights='imagenet')
     # remove the last layers in order to get features instead of predictions
     feat_extractor = Model(inputs=vgg_model.input, outputs=vgg_model.get_layer("fc2").output)
     original = load_img(img, target_size=(224, 224))
     numpy_image = img_to_array(original)
     image_batch = np.expand_dims(numpy_image, axis=0)
    # Chuẩn bị ảnh cho model vgg16
     processed_image = preprocess_input(image_batch.copy())
    # get the extracted features
     img_features = feat_extractor.predict(processed_image)
     # retrieve products
     return img_features
    
def file_selector(folder_path='.'):
    filenames = os.listdir(folder_path)
    selected_filename = st.selectbox('Select a file', filenames)
    return os.path.join(folder_path, selected_filename)



def imgs_features():
    df_2 = pd.read_csv('../Data/model//model2.csv')
    B = (df_2.iloc[0:,1:]).to_numpy()
    return B


def retrieve_most_similar_products(given_img):
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.error("most similar products: ")
    # st.write(return_image_embedding(given_img))
    imgs_path = r"../Data/Images//img_trains"
    files = [imgs_path+'//' + x for x in os.listdir(imgs_path) if "png" in x]
    A = return_image_embedding(given_img)
    B = imgs_features()
    for b,file in zip(B,files) :
      # compute cosine similarity
      cosine = np.dot(A,b)/(norm(A)*norm(b))
     #   print("Cosine Similarity:", cosine)
      if(cosine > 0.75 and cosine < 1.0) :
        #  print('hong tuoi xinh dep',cosine,file)
        st.write('Similarity',str(cosine))
        original = load_img(file, target_size=(320, 400))
        st.image(original, caption='Uploaded Image', use_column_width=False)
    



@st.cache()
def names():
    filename = file_selector()
    return filename


def main():
    # st.sidebar.titile('Product recommendation')
    st.sidebar.subheader('Van Hieu - Tien Dat')
    actives = ['Product', 'About']
    choice = st.sidebar.selectbox("select Activity", actives)
    if choice == 'Product':
        st.title("Product Recommendation System")
        # n = st.selectbox("select Image", name)
        file_uploaded = st.file_uploader("Chọn File", type=["png", "jpg", "jpeg"])
        st.write(file_uploaded.name)
        if file_uploaded is not None:
            path = "../Data/Images/img_trains//" + f'{file_uploaded.name}'
            im1 = Image.open(file_uploaded)
            newsize = (224, 320)
            image1= im1.resize(newsize)
            st.success("original product:")
            st.image(image1, caption='Uploaded Image', use_column_width=False)
            st.write('image',path)
            img = Image.open(file_uploaded)
            df = load_data()
            retrieve_most_similar_products(path)


            
        else:
            st.error("write the path name")

    elif choice == 'About':
        st.title("About Me")
        st.success("A")
        st.error("If you")
        st.title("Please")


if __name__ == '__main__':
    main()
