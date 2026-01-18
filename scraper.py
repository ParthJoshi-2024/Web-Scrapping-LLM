import requests
from bs4 import BeautifulSoup

def extract_main_content(url: str) -> str:
    response = requests.get(
        url,
        timeout=15,
        headers={"User-Agent": "Mozilla/5.0"}
    )
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    for tag in soup(["script", "style", "nav", "footer", "header", "aside"]):
        tag.decompose()

    text = " ".join(p.get_text(strip=True) for p in soup.find_all("p"))
    return text[:12000]  # token safety
