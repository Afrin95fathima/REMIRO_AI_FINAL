import random
from datetime import datetime

# Mock news data - in a real application, this would fetch from an API
career_news = [
    {
        "title": "Remote Work Trends 2025",
        "summary": "Studies show 65% of knowledge workers now prefer hybrid work arrangements, with companies adapting policies to attract top talent.",
        "date": "2025-09-15"
    },
    {
        "title": "AI Skills Gap Widens",
        "summary": "Demand for AI specialists continues to outpace supply, with machine learning engineers and data scientists commanding premium salaries.",
        "date": "2025-09-20"
    },
    {
        "title": "Green Jobs on the Rise",
        "summary": "Sustainability sector shows 30% growth in job postings as companies invest in climate initiatives and renewable energy transitions.",
        "date": "2025-09-18"
    },
    {
        "title": "Digital Nomad Visa Programs Expand",
        "summary": "Twenty more countries introduced digital nomad visa programs this year, making location-independent work increasingly accessible.",
        "date": "2025-09-12"
    },
    {
        "title": "Soft Skills Premium",
        "summary": "New research indicates employers are paying up to 20% more for candidates with exceptional communication and adaptability skills.",
        "date": "2025-09-22"
    }
]

def get_career_news(count=3):
    """Get recent career news items"""
    # In a real application, this would fetch from an API
    # For now, return random selections from our mock data
    
    if not career_news:
        return []
    
    # Ensure we don't request more items than available
    count = min(count, len(career_news))
    
    # Return random selection of news items
    return random.sample(career_news, count)