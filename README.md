# Text Summarization Project

This project demonstrates text summarization using Streamlit and Transformers. It uses pre-trained models to generate summaries from input text.
For this purpose, there was a many choice from huggingface library and i wantted to use the "facebook/bart-large-cnn" model for the reason that it is the most know and complet model who dessigened for this task. While originally trained in English, it performs well on French text as well.

I also wanted to test T5('google/flan-t5-base') model wich is a general text-to-text generative model but also usuable to summarize text and pre trained with 5 languages include english and french.

Despite their performance, they remain lightweight enough to be executable on my laptop.

## Logic of Processing the Input Text and Generation of Summary

1. **Input Text Processing:**
   - Tokenization: Breaking the text into individual words or subword units.
   - Removing Stop Words: Eliminating common words that don't carry significant meaning.
   - Handling Special Characters: Addressing punctuation and special characters.

2. **Generating Summaries:**
   - For "facebook/bart-large-cnn," the model leverages its bidirectional and auto-regressive capabilities to produce concise and coherent summaries.
   - For "google/flan-t5-base," the model's general text-to-text approach is employed, framing the summarization task as a text generation problem.



## Install Necessary Libraries

```bash
pip install -r requirements.txt
```

## Usage

### Using Streamlit Directly
Dowloading the model take some time at first execution!

```bash
streamlit run bart.py
```

or

```bash
streamlit run t5.py
```


### Using Docker

Build the Docker image:

for bart:
```bash
docker build -t image_bart -f Dockerfile_bart .
```

for T5:
```bash
docker build -t image_t5 -f Dockerfile_t5.
```

Run the Docker container:

for bart:
```bash
docker run -p 8501:8501 --name container_bart -d image_bart
```
for t5:
```bash
docker run -p 8501:8501 --name container_t5 -d image_t5
```

Access the app in your browser:
- Network URL: http://localhost:8501
- External URL: http://your_host_ip:8501

Stop the Docker container:
```bash
docker stop container_bart
```
or
```bash
docker stop container_t5
```


## License

[MIT](https://choosealicense.com/licenses/mit/)