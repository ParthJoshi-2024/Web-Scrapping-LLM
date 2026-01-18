from scraper import extract_main_content
from summarizer import summarize_text

def main():
    print("\n🌐 Web Page Summarizer (OpenAI)\n")
    url = input("Enter the website URL: ").strip()

    print("\n🔍 Extracting content...")
    content = extract_main_content(url)

    print("🧠 Generating structured summary...\n")
    summary = summarize_text(content)

    print("📄 SUMMARY\n")
    print(summary)

if __name__ == "__main__":
    main()
