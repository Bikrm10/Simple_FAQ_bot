import streamlit as st
import spacy  
import en_core_web_lg



def main():
    st.title("Simple Chatbot")

    
    st.sidebar.markdown(
        """
        # Danson Sollutions :notebook:
        :rocket: This app is an simple FAQ chatbot built using:

        - [Streamlit](https://streamlit.io/): For creating the interactive web interface.

        - [spaCy](https://spacy.io/): For NLP models.

        
        

        **Workflow:**:arrow_down:
        1. **Load Model**: We load spaCy large model that tokenize english language.
        2. **Create FAQ**: The list of general questions and answers are prepared .
        3. **Find similar questions**:The similarity score in  the FAQ question and iser query is done.
        4. **Query Processing**: The answer stored in FAQ are then response to the query.

        This workflow ensures that users can interactively query general question about Danson and receive relevant, accurate information.


        """
    )
    st.sidebar.write(":heart: Made by Bikram Karki.")
    nlp_model = spacy.load("en_core_web_lg")
    FAQ = {
        "What are your working hours?": "We are open from 9 AM to 5 PM, Monday to Friday.",
        "Who are you?": "Danson is an IT and Marketing firm.",
        "when the company started":"It was started from 2020",
        "What is the name of the company": "The name of the company is Danson Solutions.",
        "where is the company ?":"It is located in New Jersey, USA",
        "Can you provide contact details": "you can call at +1 201-899-0314 or mail in dansonsolutions@gmail.com",
        "who is the founder of Danson":"Vijayesh Sainju is the Founder and CEO of Danson ",
        "Does it provide training":"Yes, It provides training in web development , AI chatbot , Interactive Contents , Educational Games, and so on",
        "What services do you offer?": "Our key projects include ChimpVine, Danson Training, Danson 360, Flux Fantasia, AI-driven Chatbot, and AI game design and tool implementation",

    }

    greetings = ["hi", "hello", "good morning", "good afternoon", "namaste"]

    # Function to find the most similar FAQ question using spaCy
    def find_most_similar_faq(user_message):
        user_doc = nlp_model(user_message)
        most_similar_question = None
        highest_similarity = 0.7  # Set a similarity threshold
        for question , _ in FAQ.items():
            question_doc = nlp_model(question)
            similarity = user_doc.similarity(question_doc)
            if similarity > highest_similarity:
                highest_similarity = similarity
                most_similar_question = question
        return most_similar_question

    
    def message_processing(message):
        message_lower = message.lower()

        
        for greet in greetings:
            if greet in message_lower:
                return "Hello dear! How can I assist you?"

        
        matched_question = find_most_similar_faq(message)
        if matched_question:
            for question , answer in FAQ.items():
                if question == matched_question:
                 return answer
        
        
        doc = nlp_model(message)
        entities = [(ent.text, ent.label_) for ent in doc.ents]
        if entities:
            return f"I detected these entities in your message: {entities}"

        
        return "I'm sorry, I don't understand your question. Could you rephrase?"


    

    if 'chat_history' not in st.session_state:
        st.session_state['chat_history'] = []

    # st.write("### conversation history")
    for message in st.session_state['chat_history']:
        st.write(message)
    user_message = st.text_input(f"**Ask**:")
    if user_message:
        st.session_state['chat_history'].append(f"**You:** {user_message}")
        bot_response = message_processing(user_message)
        st.write(f"**Bot:** {bot_response}")
        st.session_state['chat_history'].append(f"**Bot:** {bot_response}")

if __name__ == "__main__" :
    main()
