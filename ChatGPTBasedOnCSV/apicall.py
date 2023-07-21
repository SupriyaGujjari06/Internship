from fastapi import FastAPI
from pydantic import BaseModel
import pickle
# Define a Pydantic model for the request body
class QuestionRequest(BaseModel):
    question: str

# Load the agent object from the pickle file
pickle_file_path = "agent.pkl"
with open(pickle_file_path, "rb") as file:
    agent = pickle.load(file)

# Create a FastAPI instance
app = FastAPI()
# Endpoint to handle the question
@app.post("/ask")
def ask_question(request: QuestionRequest):
    question = request.question
    response = agent.run(question)
    return { "response": response}

# Run the FastAPI application """ "question": question, """
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)

