Hey Team,

I've implemented an AI-powered Codebase Q&A API that allows us to query our project's codebase using natural language. This will help us quickly understand functions, file structures, and dependencies without manually searching through code.

🔹 I’ve shared the codebase_api.py file with you. Please follow the steps below to set it up.

🛠️ How to Set Up & Run the API
1️⃣ Clone the latest code from GitHub (if applicable):


git pull origin main
2️⃣ Install dependencies (if not already installed):


pip install fastapi uvicorn langchain langchain-groq langchain-openai faiss-cpu python-dotenv
3️⃣ Set up your Groq API key:

Create a .env file in the project folder.
Add this line inside .env:


GROQ_API_KEY=your_actual_groq_api_key_here
4️⃣ Update the project path in codebase_api.py:
Find this line:


project_directory = "C:/Users/YourUsername/HackathonProject"  # Change to your actual path
🔹 Replace it with your actual project folder path.

If you're using Windows, right-click the project folder in VS Code → Copy Path → Paste it.
Example for Windows:


project_directory = "C:/Users/MyName/Documents/HackathonProject"
Example for Mac/Linux:



project_directory = "/Users/MyName/Documents/HackathonProject"
5️⃣ Run the API in VS Code Terminal:


python codebase_api.py
✅ If everything is set up correctly, the API will start at:


http://127.0.0.1:8000