import streamlit as st
import cohere

# Initialize the Cohere client with your API key
co = cohere.Client('XnjuHlhs02hrg1UYZYtx51Oi4XGRm8T2D2JYbV5N')

def generate_summary(user_input):
    prompt = f"Summarize the following text: {user_input}"
    
    response = co.generate(
        model='command-xlarge-nightly',  # You can choose the appropriate model for summarization
        prompt=prompt,
        max_tokens=400,
        temperature=0.5,
        stop_sequences=["."]
    )
    
    # Extract the text
    result = response.generations[0].text.strip()
    
    return result

# Streamlit interface
st.title('Text Summarization Tool')

user_input = st.text_area("Enter your text here:", "Paste your long text here...")

if st.button('Generate Summary'):
    summary = generate_summary(user_input)
    st.write(summary)  # Display the generated summary
