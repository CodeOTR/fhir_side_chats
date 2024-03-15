# Rasa Server Setup

This README provides instructions on how to set up and run the Rasa server for the FHIR Side Chats application.

## Prerequisites

- Python 3.7 or 3.8
- pip (Python package installer)
- Virtual environment (optional but recommended)

## Installation

1. Create a new virtual environment (optional):

   ```
   python -m venv venv
   ```

2. Activate the virtual environment (optional):

   ```
   source venv/bin/activate  # For Unix/Linux
   venv\Scripts\activate  # For Windows
   ```

3. Install Rasa:
   ```
   pip install rasa
   ```

## Configuration

1. Navigate to your Rasa project directory (e.g., `rasa-chatbot`):

   ```
   cd rasa-chatbot
   ```

2. Train your Rasa model:

   ```
   rasa train
   ```

   This command will train your NLU and dialogue models based on the training data and configuration files in your Rasa project.

## Running the Rasa Server

1. Start the Rasa server:

   ```
   rasa run --enable-api --cors "*" --debug
   ```

   - `--enable-api`: Enables the Rasa HTTP API, which allows your frontend to communicate with the Rasa server.
   - `--cors "*"`: Enables Cross-Origin Resource Sharing (CORS) for all origins. This is necessary for your frontend to make requests to the Rasa server from a different origin (e.g., `http://localhost:3000`).
   - `--debug`: Runs the Rasa server in debug mode, which provides more detailed logging information.

   By default, the Rasa server will start on `http://localhost:5005`.

2. Verify that the Rasa server is running:
   Open a new terminal window and run the following command:

   ```
   curl http://localhost:5005/status
   ```

   If the Rasa server is running correctly, you should see a response similar to:

   ```json
   { "status": "ok" }
   ```

   This indicates that the Rasa server is up and running at `http://localhost:5005`.

## Usage

Once the Rasa server is running, your React frontend can communicate with it by making HTTP requests to `http://localhost:5005`.

For example, to send a user message to the Rasa server and receive a response, you can use the following code snippet in your frontend:

```tsx
try {
  const response = await axios.post(
    "http://localhost:5005/webhooks/rest/webhook",
    {
      sender: "user",
      message: userMessage.text,
    }
  );

  const botMessage: Message = {
    text: response.data[0].text,
    sender: "bot",
  };
  setMessages([...messages, userMessage, botMessage]);
} catch (error) {
  console.error("Error communicating with Rasa server:", error);
}
```

Make sure to keep the Rasa server running while you're testing and using your chatbot application.

If you have any questions or encounter any issues, please refer to the Rasa documentation or reach out to the project maintainers.
