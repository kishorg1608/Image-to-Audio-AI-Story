# Image-to-Audio-Story AI Project

This project utilizes transformers and AI models to convert images into captivating audio stories. It combines image captioning and text generation models to create an immersive storytelling experience. Follow the steps below to set up and run the project.

## Prerequisites

1. **Python:** Make sure you have Python installed on your machine.

2. **Dependencies:** Install the required Python packages by running:
    ```bash
    pip install transformers
    pip install pipeline
    pip install python-dotenv
    ```

3. **Hugging Face API Key:** Obtain an API key from Hugging Face by signing up on their website.

## Project Structure

- **main.py:** Contains the core functionality of the project.
- **.env:** Store your Hugging Face API key in this file.

## Usage

1. **Clone the Repository:**
    ```bash
    git clone https://github.com/your-username/image-to-audio-story.git
    cd image-to-audio-story
    ```

2. **Set Up Environment Variables:**
    - Create a `.env` file in the project root.
    - Add your Hugging Face API key:
        ```
        HUGGING_FACE_API_KEY=your-api-key
        ```

3. **Run the Project:**
    ```bash
    python main.py
    ```
    Replace the image path in `img2txt` with the path to your desired image.

4. **Enjoy Your Audio Story:**
    The project will generate a captivating audio story based on the content of the image.

## Customization

Feel free to experiment with different models or modify the text prompts for story generation. You can explore additional transformer models on the Hugging Face Model Hub.

## Acknowledgments

- [Hugging Face Transformers](https://github.com/huggingface/transformers): Library for state-of-the-art Natural Language Processing.

Happy storytelling with Image-to-Audio-Story AI!
