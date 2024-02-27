import streamlit as st
from transformers import T5Tokenizer, T5ForConditionalGeneration

tokenizer = T5Tokenizer.from_pretrained("google/flan-t5-base")
model = T5ForConditionalGeneration.from_pretrained("google/flan-t5-base")


st.title("Text Summarization")

user_input = st.text_area("Enter your text to summarize:")

if st.button("Summarize"):
    input_ids = tokenizer(user_input, return_tensors="pt").input_ids

    outputs = model.generate(input_ids, max_length=140, num_beams=2, length_penalty=2.0, early_stopping=True)


    summary = tokenizer.decode(outputs[0], skip_special_tokens=True)
    st.subheader("Generated Summary:")
    st.write(summary)
