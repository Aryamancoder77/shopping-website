from langchain.tools import tool
from duckduckgo_search import DDGS
import json

@tool
def web_search(query: str) -> str:
    """Search the web for products and prices"""
    with DDGS() as ddgs:
        results = [r for r in ddgs.text(query, max_results=5)]
    return json.dumps(results, ensure_ascii=False)

@tool
def compare_prices(product: str) -> str:
    """Compare prices on Amazon.in and Flipkart"""
    queries = [f"{product} site:amazon.in", f"{product} site:flipkart.com"]
    results = {}
    with DDGS() as ddgs:
        for q in queries:
            res = list(ddgs.text(q, max_results=3))
            results[q] = res
    return json.dumps(results, ensure_ascii=False)
