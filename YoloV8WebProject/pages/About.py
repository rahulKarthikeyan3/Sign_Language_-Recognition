import streamlit as st 

st.set_page_config(page_title="Home",
                   layout='wide',
                   page_icon='./images/home.png')

st.title("SIGN LANGUAGE RECOGNITION 👋")
st.caption('Signs are 👀 What words are to 👂')

# Content
st.title("About sign language ")

st.markdown("""
###
-  Sign language recognition is a field of research and technology development focused on building systems that can automatically interpret and understand sign language gestures. The goal is to enable communication between sign language users and non-signers by converting sign language into spoken or written language, or vice versa.

-  Sign language recognition systems typically involve the use of computer vision techniques and machine learning algorithms. Here's an overview of the key steps and components involved:

1. Data collection: The first step in building a sign language recognition system is to collect a dataset of sign language videos or images. This dataset should include a variety of sign language gestures performed by different signers to ensure diversity and coverage of the language.

2. Preprocessing: The collected data is then preprocessed to extract relevant features and remove noise or irrelevant information. This may involve techniques such as background subtraction, hand tracking, or normalization.

3. Feature extraction: Once the data is preprocessed, features need to be extracted to represent the sign language gestures effectively. Commonly used features include hand shape, hand movement, hand orientation, and facial expressions. Various computer vision techniques, such as contour analysis, motion analysis, or optical flow, can be employed to extract these features.

4.  Machine learning algorithms: With the extracted features, machine learning algorithms are used to train models that can recognize and classify different sign language gestures. These algorithms can include deep learning approaches like convolutional neural networks (CNNs) or recurrent neural networks (RNNs), as well as traditional machine learning techniques like support vector machines (SVMs) or hidden Markov models (HMMs).

5.  Training and evaluation: The models are trained using the collected dataset, where the features are associated with their corresponding sign language gestures. The training process involves optimizing the model's parameters to minimize the recognition error. Evaluation is performed using separate testing data to assess the model's performance and accuracy.

6.  Real-time recognition: Once the model is trained and evaluated, it can be deployed for real-time sign language recognition. This typically involves capturing video input from a camera or using sensor-based technologies, processing the input, and feeding it into the trained model for recognition. The system then produces the corresponding spoken or written language output.

-  Sign language recognition systems have the potential to facilitate communication between sign language users and non-signers in various domains, including education, healthcare, customer service, and more. Ongoing research aims to improve the accuracy, efficiency, and robustness of these systems, making sign language more accessible and inclusive.


""")

st.markdown('''<a>
<img src="https://media.istockphoto.com/id/1306688274/vector/deaf-mute-language-american-deaf-mute-hand-gesture-alphabet-letters-asl-vector-symbols.jpg?s=612x612&w=0&k=20&c=3O0NA8bSPz8hyWJIhvkQ2RJ61O8uRLtLDv7VJir0TAw=")
</a>
''',
unsafe_allow_html=True
)