# LinkedIn PDF to HTML Resume Converter

## Overview
This web application converts a LinkedIn PDF resume into a structured HTML format using OpenAI's GPT-4 API. Built with Streamlit, it provides a simple interface for uploading your resume and obtaining an HTML version.

## Features
- **PDF Upload**: Upload your LinkedIn PDF resume.
- **AI Conversion**: Utilizes OpenAI's GPT-4 to convert PDF text to HTML.
- **HTML Preview**: View the generated HTML resume directly on the website.
- **Download Option**: Download the HTML resume for your records.

## Setup & Deployment

### Local Setup
1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/linkedin-pdf-to-html.git
   cd linkedin-pdf-to-html
   ```

2. **Create a `.env` File**
   
   Create a `.env` file in the root directory and add your OpenAI API key:
   ```env
   OPENAI_API_KEY=your_openai_api_key_here
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the App**
   ```bash
   streamlit run app.py
   ```

5. **Open in Browser**
   Navigate to `http://localhost:8501` in your web browser.

### Deployment
Since GitHub Pages does not support dynamic applications like Streamlit, it's recommended to use [Streamlit Cloud](https://streamlit.io/cloud) or [Vercel](https://vercel.com/) for deployment.

#### Deploying on Streamlit Cloud
1. **Push Your Repository to GitHub**
   
2. **Create a Streamlit Cloud Account**
   
3. **Deploy the App**
   - Go to Streamlit Cloud and select "New app".
   - Connect your GitHub repository.
   - Specify the branch and `app.py` as the entry point.
   - Add the `OPENAI_API_KEY` in the Secrets section.

#### Deploying on Vercel
1. **Install Vercel CLI**
   ```bash
   npm install -g vercel
   ```

2. **Initialize Vercel in Your Project**
   ```bash
   vercel
   ```

3. **Set Environment Variables**
   ```bash
   vercel env add OPENAI_API_KEY
   ```

4. **Deploy**
   ```bash
   vercel --prod
   ```

## Usage
1. **Upload PDF**
   - Upload your LinkedIn PDF resume using the file uploader.

2. **Convert**
   - The app processes the PDF and converts it to HTML.

3. **View & Download**
   - Preview the HTML resume on the website.
   - Download the HTML file for your records.

## Project Structure
- `app.py`: The main Streamlit application.
- `requirements.txt`: Python dependencies.
- `.env`: Environment variables (contains the OpenAI API key).
- `test_openai.py`: (Optional) Tests for OpenAI integration.
- `cursorTest/`: Jupyter notebook extensions and virtual environment.

## Dependencies
- **Streamlit**: For building the web interface.
- **OpenAI**: For AI-powered text conversion.
- **PyPDF2**: For extracting text from PDF files.
- **python-dotenv**: For managing environment variables.

## Security
- **API Key Management**: Ensure that your OpenAI API key is stored securely in the `.env` file and not exposed in the repository. When deploying, use the platform's secret management features to keep your API keys safe.

## License
This project is licensed under the MIT License.
