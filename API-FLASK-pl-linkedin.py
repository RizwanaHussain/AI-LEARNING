import asyncio
import os
from flask import Flask, request, jsonify
from playwright.async_api import async_playwright

app = Flask(__name__)

async def scrape_and_generate(site_url, selector):
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()

        await page.goto(site_url)

        # Auto-accept cookies (Optional)
        try:
            await page.click('button:has-text("Accept all")', timeout=5000)
        except:
            pass  # No cookie popup

        # Wait for selector
        await page.wait_for_selector(selector, timeout=60000)
        article_element = await page.query_selector(selector)
        article_title = await article_element.inner_text()
        article_link = await article_element.get_attribute("href")
        article_link = article_link if article_link.startswith("http") else site_url.rstrip("/") + article_link

        # Visit article
        await page.goto(article_link)
        await page.wait_for_timeout(3000)

        paragraphs = await page.query_selector_all("p")
        article_content = ""
        for para in paragraphs:
            text = await para.inner_text()
            article_content += text.strip() + "\n\n"

        # Prepare post
        hook = f"🔥 Imagine this situation: You're trying to crack the next marketing breakthrough, but feel lost in trends. Here's what I found in the article: *{article_title}*"
        problem = "Many marketers today struggle with overwhelming trends, unclear strategies, and rapid digital shifts."
        solution = "Here’s what caught my attention:\n\n" + article_content[:500].strip()
        cta = f"💡 Read the full article here: {article_link}"
        hashtags = "#Marketing #DigitalMarketing #BusinessGrowth #Trends"

        linkedin_post = f"{hook}\n\n---\n\n{problem}\n\n---\n\n{solution}\n\n---\n\n{cta}\n\n\n{hashtags}"

        await browser.close()

        return {
            "title": article_title,
            "link": article_link,
            "linkedin_post": linkedin_post
        }

@app.route('/generate-post', methods=['POST'])
def generate_post():
    data = request.json
    site_url = data.get("site_url")
    selector = data.get("selector")

    if not site_url or not selector:
        return jsonify({"error": "Missing site_url or selector"}), 400

    result = asyncio.run(scrape_and_generate(site_url, selector))
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
