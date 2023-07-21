from dotenv import load_dotenv
from langchain import OpenAI, SQLDatabase, SQLDatabaseChain
from urllib.parse import quote_plus

load_dotenv()
# Encode the password
password = quote_plus("xxxxxx")

# Construct the URI
dburi = f"mysql+pymysql://xxxxxxxxx:{password}@xxxxx:xxxx/xxxxxxx"

db = SQLDatabase.from_uri(dburi, include_tables=['data'])
llm = OpenAI(temperature=0,max_tokens=20)

# Create an instance of SQLDatabaseChain
db_chain = SQLDatabaseChain(llm=llm, database=db, verbose=True)
db_chain.run("no of records")