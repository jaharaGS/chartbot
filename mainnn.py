pip install transformers

from transformers import pipeline

# Initialize the question-answering pipeline
qa_pipeline = pipeline("question-answering")

# Knowledge base (can be expanded)
knowledge_base = {
    "loans": """We offer various loan products tailored to your needs.  
              Our loan terms and interest rates vary depending on your credit score and the loan amount.
              For more specific information, please contact our loan officers.""",
    "interest_rates": """Our interest rates are competitive and depend on the type of loan and your creditworthiness.
                        Current interest rates are subject to change based on market conditions.
                        Please contact us for the latest rates.""",
    "credit_report": """Your credit report reflects your credit history, including past payments, open accounts, and inquiries.
                       It's essential for loan applications and can impact your interest rates.  We recommend you check your report regularly.""",
    "credit_bureau": """A credit bureau is an agency that collects and maintains credit information.  
                       Examples include CIBIL, Experian, and Equifax.""",
    "cibil": """CIBIL (Credit Information Bureau India Limited) is one of the leading credit information companies in India.
               Your CIBIL score is a crucial factor for loan approvals and interest rates.""",
    "financial_services": """We provide a range of financial services including loans, credit cards, investment options, and more.  
                            Visit our website or contact us for detailed information on each service."""
}


def get_answer(user_question):
    best_match = None
    best_score = 0

    for topic, content in knowledge_base.items():
        result = qa_pipeline(question=user_question, context=content)
        if result["score"] > best_score:
            best_score = result["score"]
            best_match = result

    if best_score > 0.5: #Confidence Threshold
        return best_match["answer"]
    else:
      return "I'm sorry, I don't have enough information to answer your question. Could you rephrase it or contact customer support?"


while True:
  user_input = input("You: ")
  if user_input.lower() == "exit":
    break
  response = get_answer(user_input)
  print("Chatbot:", response)