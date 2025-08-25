from typing import Literal
from pydantic import Field
from .base_schema import ToolParameters

class WeatherParams(ToolParameters):
    """define weather function parameters"""
    # field helps add metadata, will usually output title, description, type like
    # {"location": {"title": "Location", "description": "City and Country, e.g. Merida, Mexico", "type": "string"}}
    location: str = Field(..., description="City and Country, e.g. Merida, Mexico")
    units: Literal["celsius", "fahrenheit"] = Field(..., description="Temp units")

class RedditSearchParams(ToolParameters):
    """define reddit search function parameters"""
    query: str = Field(..., description="Search query")
    subreddit: str = Field(..., description="Subreddit to search in")
    limit: int = Field(10, description="Number of results to return")

class TMDBSearchParams(ToolParameters):
    """define TMDB search function parameters"""
    title: str = Field(..., description="Anime Title")
    year: int | None = Field(None, description="Year of release") # None is default 

if __name__ == "__main__":
    print(WeatherParams.model_json_schema())
    print(RedditSearchParams.model_json_schema())
    print(TMDBSearchParams.model_json_schema())
