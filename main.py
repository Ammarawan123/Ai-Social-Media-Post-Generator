import os
from text_generator import generate_text
from image_generator import generate_image

# File paths
IMAGE_PATH = "generated_content/generated_image.jpg"

def main():
    while True:
        user_input = input("Enter a prompt (or type 'exit' to quit): ")
        if user_input.lower() == "exit":
            print("👋 Goodbye!")
            break
        
        action = input("Would you like text or image generation? (text/image): ").strip().lower()
        
        if action == "text":
            print("🤖 Bot:", generate_text(user_input))

        elif action == "image":
            image_path = generate_image(user_input)
            if image_path:
                print(f"✅ Image saved successfully at {image_path}")
            else:
                print("❌ Image generation failed.")

        else:
            print("⚠️ Invalid choice. Please type 'text' or 'image'.")

if __name__ == "__main__":
    main()