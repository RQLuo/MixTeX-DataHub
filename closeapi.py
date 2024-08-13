import os
import base64
import json
import csv
from openai import OpenAI

# OpenAI API Key
api_key = ''

# Initialize OpenAI client
client = OpenAI(api_key=api_key)

# Function to encode the image
def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

# Directory containing images
image_directory = "img"
your_pt = "Recognize the text, Output the text directly, no extra words:"
# Prepare batch input
batch_input = []
for i, filename in enumerate(os.listdir(image_directory)):  # Limit to 100 images
    if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
        image_path = os.path.join(image_directory, filename)
        base64_image = encode_image(image_path)
        
        request = {
            "custom_id": f"request-{i+1}",
            "method": "POST",
            "url": "/v1/chat/completions",
            "body": {
                "model": "gpt-4o-2024-08-06",
                "messages": [
                    {
                        "role": "user",
                        "content": [
                            {
                                "type": "text",
                                "text": your_pt
                            },
                            {
                                "type": "image_url",
                                "image_url": {
                                    "url": f"data:image/jpeg;base64,{base64_image}"
                                }
                            }
                        ]
                    }
                ],
                "max_tokens": 768
            }
        }
        batch_input.append(request)

# Save batch input to a JSONL file
with open("batchinput.jsonl", "w") as f:
    for item in batch_input:
        f.write(json.dumps(item) + "\n")

# Create a batch input file
batch_input_file = client.files.create(
    file=open("batchinput.jsonl", "rb"),
    purpose="batch"
)

# Create a batch job
batch_job = client.batches.create(
    input_file_id=batch_input_file.id,
    endpoint="/v1/chat/completions",
    completion_window="24h",
    metadata={
        "description": "Image OCR batch job"
    }
)

print(f"Batch job created with ID: {batch_job.id}")

# Wait for the batch job to complete (you might want to implement a proper waiting mechanism)
import time
while True:
    job_status = client.batches.retrieve(batch_job.id)
    if job_status.status == "completed":
        break
    time.sleep(120)  # Check every minute

output_file = client.files.retrieve(job_status.output_file_id)
output_content = client.files.content(output_file.id)

results = [json.loads(line) for line in output_content.text.split('\n') if line]

# Write results to CSV
with open("ocr_results.csv", "w", newline="", encoding="utf-8") as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(["file_name", "text"])
    
    for result in results:
        custom_id = result['custom_id']
        file_name = os.listdir(image_directory)[int(custom_id.split("-")[1]) - 1]
        ocr_text = result['response']['body']['choices'][0]['message']['content']
        csvwriter.writerow([file_name, ocr_text])

print("OCR results have been saved to ocr_results.csv")