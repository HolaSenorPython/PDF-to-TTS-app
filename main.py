from dotenv import load_dotenv
import os
import boto3
from PyPDF2 import PdfReader
from pathlib import Path # For fixing up their file paths on all OS
from botocore.exceptions import BotoCoreError, ClientError
text_for_polly = ""
load_dotenv()

#------Start the stuff------#
print("Welcome to the PDF to TTS converter! If you've ever wanted\n"
      "a PDF to be read out to you, here you go. To get started, follow\n"
      "instructions below.")
print("NOTE: Your PDF file has to be LESS than 3000 characters of text.")
selected_file = input("Write the EXACT name of the file you want to convert."
                      " If it isn't in this folder, write the absolute path.\n")
# Strip the input of quotes or anything
stripped = selected_file.strip("'").strip('"')
file_path = Path(stripped) # make path obj

# Try reading from the Pdf and stuff (rb mode for pdfs)
try:
    with file_path.open('rb') as file:
        reader = PdfReader(file)
        for page in reader.pages: # for every page in pdf
            page_txt = page.extract_text() # extract text
            if page_txt: # If there was text:
                text_for_polly += page_txt
except FileNotFoundError as e:
    print(f"Sorry, I couldn't find a pdf file with that name or\n"
          f"at that path: {e}")

# Print the text we want polly to read later for safe measure
print(f"This is the text we got from your PDF!:\n"
      f"{text_for_polly}")

# Create client (polly)
polly = boto3.client('polly',
                     aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
                     aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
                     region_name=os.getenv('AWS_DEFAULT_REGION'),
                     )

# Text to read
text = text_for_polly

# Synthesize, but with error handling 😏
try:
    response = polly.synthesize_speech(
        Text=text,
        OutputFormat='mp3',
        VoiceId='Joanna',
    )

    status_code = response['ResponseMetadata']['HTTPStatusCode']
    if status_code != 200: # If it isn't equal to 200 (success!)
        raise Exception(f"Polly request failed! :( Status code: {status_code}")

    # Save audio to a file (in WB mode, audio is in binary not text)
    audio_stream = response['AudioStream'] # define for Closing later
    with open('speech.mp3', 'wb') as f:
        f.write(audio_stream.read())
    audio_stream.close() # Close it, it is separate from speech mp3 and python closing

    print("Done! Audio saved as 'speech.mp3' in this folder.")

except (BotoCoreError, ClientError) as error:
    print(f"An error occured: {error}")