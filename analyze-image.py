import sys
import openai

# Initialize OpenAI client
client = openai.OpenAI()


def analyze_image(image_url):
  try:
    response = client.chat.completions.create(
        model="gpt-4o",  # The latest vision-enabled model
        messages=[{
            "role":
            "user",
            "content": [{
                "type": "text",
                "text": "Describe the content of this image."
            }, {
                "type": "image_url",
                "image_url": {
                    "url": image_url
                }
            }]
        }])

    # Output the assistant's response
    print(response.choices[0].message.content)

  except Exception as e:
    print(f"Error: {e}")


if __name__ == "__main__":
  if len(sys.argv) < 2:
    print("Usage: python analyze-image.py <image_url>")
  else:
    analyze_image(sys.argv[1])
