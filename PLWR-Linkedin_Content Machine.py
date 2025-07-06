# use this LINKEDIN POST GENERATOR
# Just update site link and the article selector value


import asyncio
from playwright.async_api import async_playwright
import os

async def scrape_hubspot_blog():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()

        # 1️⃣ Go to HubSpot Blog
        await page.goto("https://blog.hubspot.com/")

        # 2️⃣ Auto-accept cookies
        try:
            await page.click('button:has-text("Accept all")', timeout=5000)
            print("✅ Cookie consent accepted.")
        except:
            print("⚠️ No cookie dialog found -- continuing.")

        # 3️⃣ Wait for featured article selector
        selector = "#hs_cos_wrapper_blog_above_the_fold > section > div.blog-post-card.-featured > div.blog-post-card-body > h2 > a"
        await page.wait_for_selector(selector, timeout=60000)
    
        # 4️⃣ Get featured article title & URL
        article_element = await page.query_selector(selector)
        article_title = await article_element.inner_text()
        article_link = await article_element.get_attribute("href")
        article_link = article_link if article_link.startswith("http") else "https://blog.hubspot.com" + article_link

        print(f"🔗 Featured Article: {article_title}")
        print(f"📍 URL: {article_link}")

        # 5️⃣ Visit article page
        await page.goto(article_link)
        await page.wait_for_timeout(5000)  # Wait for content

        # 6️⃣ Extract article body text
        paragraphs = await page.query_selector_all("p")
        article_content = ""
        for para in paragraphs:
            text = await para.inner_text()
            article_content += text.strip() + "\n\n"

        # ✅ Storytelling Post Structure
        hook = f"🔥 Imagine this situation: You're trying to crack the next marketing breakthrough, but feel lost in trends. Here's what I found in HubSpot’s latest feature: *{article_title}*"
        
        # Extracting some "problem" sentences (simulate insight extraction)
        problem = "Many marketers today struggle with overwhelming trends, unclear strategies, and rapid digital shifts."
        
        # Solution from article: Use first few sentences from article body
        solution = "Here’s what caught my attention:\n\n" + article_content[:500].strip()
        
        # Call to action
        cta = f"💡 If this resonates with your business, take a moment to read the full article here: {article_link}"
        
        # Hashtags
        hashtags = "#Marketing #DigitalMarketing #HubSpot #BusinessGrowth #Trends"

        # Combine everything into one engaging post
        linkedin_post = f"{hook}\n\n---\n\n{problem}\n\n---\n\n{solution}\n\n---\n\n{cta}\n\n\n{hashtags}"

        # 7️⃣ Save storytelling LinkedIn post
        folder = r"C:\Users\rashe\OneDrive\Pictures\Screenshots\AI.SEA"
        os.makedirs(folder, exist_ok=True)
        file_path = os.path.join(folder, "hubspot_story_linkedin_post.txt")
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(linkedin_post)

        print(f"✅ Storytelling LinkedIn post saved successfully at: {file_path}")
        await browser.close()

if __name__ == "__main__":
    asyncio.run(scrape_hubspot_blog())
