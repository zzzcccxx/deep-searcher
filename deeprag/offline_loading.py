from typing import List


def load_from_local_files(filepath_or_directory: str | List[str], collection_name: str = None):
    from docling.document_converter import DocumentConverter

    converter = DocumentConverter()
    result = converter.convert(filepath_or_directory)
    markdown_content = result.document.export_to_markdown()
    print(markdown_content)

def load_from_website(url: str | List[str], collection_name: str = None):
    import os
    from firecrawl import FirecrawlApp
    app = FirecrawlApp(api_key=os.environ["FIRECRAWL_API_KEY"])
    scrape_status = app.scrape_url(
        url,
        params={"formats": ["markdown"]},
    )
    markdown_content = scrape_status["markdown"]
    print(markdown_content)