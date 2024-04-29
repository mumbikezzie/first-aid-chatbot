# test-open-ai-finetune
Pre-processing data and transforming it for fine-tuning on oepn ai api
I have followed the recommended steps according to openai api documentation and it is able to process the data into its roles and the bot is responsive
The errors that keep stemming lie in the json intents file, I thought it was corrected in-code but it seems it is still not in the required dictionary format
It was able to split the intents data into training and validation data but it still carries the error stating that the examples are not dictionaries


## HOW TO RUN THE APP

```
npm install
```

## TO RUN THE CLIENT

```
cd client && npm run dev
```

## TO RUN THE BACKEND

```
cd backend pip install -r requirements.txt && alembic upgrade head && uvicorn main:app --reload
```