import streamlit as st
from transformers import BartTokenizer, BartForConditionalGeneration


tokenizer = BartTokenizer.from_pretrained("facebook/bart-large-cnn")
model = BartForConditionalGeneration.from_pretrained("facebook/bart-large-cnn")

st.title("Text Summarization")


user_input = st.text_area("Enter your text here:")


if st.button("Summarize"):
    if not user_input:
            st.error("Please enter some text to summarize.")
            st.stop()

    inputs = tokenizer.encode("summarize: " + user_input, return_tensors="pt", max_length=512, truncation=True)

    summary_ids = model.generate(inputs, max_length=130, min_length=30, length_penalty=2.0, num_beams=4, early_stopping=True)
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    
    st.subheader("Generated Summary:")
    st.write(summary)



# english, french
    