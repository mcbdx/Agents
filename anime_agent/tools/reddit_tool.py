from typing import Dict, Any 
from schemas.base_schema import BaseTool
from schemas.tool_schemas import RedditSearchParams

class RedditSearchTool(BaseTool[RedditSearchParams]):
    name = "search_reddit" # this is the function name
    description = "Searches Reddit for a given query"
    parameters = RedditSearchParams # this is the class itself

    # implement the execution 
    async def execute(self, params: RedditSearchParams) -> Dict[str, Any]:
        # mock data 
        posts = [
            {"title": "Post 1", "url": "http://reddit.com/r/test1", "text":"test reddit about life 1"},
            {"title": "Post 2", "url": "http://reddit.com/r/test2", "text":"test reddit about life 2"},
        ]

        return {
            "posts": posts
        }
    
if __name__ == "__main__":
    import asyncio

    async def main():
        search_reddit = RedditSearchTool()
        result = await search_reddit.execute(RedditSearchParams(query="life",subreddit="life",limit=10))
        print(result)
    asyncio.run(main())

     

