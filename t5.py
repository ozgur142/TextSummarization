import streamlit as st
from transformers import T5Tokenizer, T5ForConditionalGeneration

tokenizer = T5Tokenizer.from_pretrained("google/flan-t5-base")
model = T5ForConditionalGeneration.from_pretrained("google/flan-t5-base")


st.title("Text Summarization")

user_input = st.text_area("Enter your text to summarize:")

if st.button("Summarize"):
    if not user_input:
            st.error("Please enter some text to summarize.")
            st.stop()
    
    input_ids = tokenizer(user_input, return_tensors="pt", max_length=512, truncation=True).input_ids
    summary_ids = model.generate(input_ids, max_length=140, num_beams=2, length_penalty=1.0, early_stopping=True)
    

    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    
    st.subheader("Generated Summary:")
    st.write(summary)

