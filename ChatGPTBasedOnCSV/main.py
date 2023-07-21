import pickle
from dotenv import load_dotenv
from langchain import OpenAI 
from langchain.document_loaders.csv_loader import CSVLoader
from langchain.agents import create_csv_agent
load_dotenv()
filepath = "data.csv"
loader = CSVLoader(filepath)
data = loader.load()
llm = OpenAI(temperature=0.4,model_name='text-davinci-003')
agent = create_csv_agent(llm, filepath, verbose=True)


# Save the agent object to a pickle file
pickle_file_path = "agent.pkl"
with open(pickle_file_path, "wb") as file:
    pickle.dump(agent, file)
    
print("Agent object saved successfully.") 