from typing import Dict, Any
from schemas.base_schema import BaseTool
from schemas.tool_schemas import TMDBSearchParams


class RedditSearchTool(BaseTool[TMDBSearchParams]):
    name = "search_tmbd"
    description = "Searches TMBD for a given query"
    parameters = TMDBSearchParams

    # implement the execution
    async def execute(self, params: TMDBSearchParams) -> Dict[str, Any]:
        # mock data
        animes = [
            {
                "adult": False,
                "backdrop_path": "/abcd1234xyz.jpg",
                "genre_ids": [16, 18],
                "id": 12345,
                "origin_country": ["JP"],
                "original_language": "ja",
                "original_name": "ムシシ",
                "overview": "Ginko is a 'Mushi-shi' who travels around investigating ...",
                "popularity": 45.67,
                "poster_path": "/efgh5678poster.jpg",
                "first_air_date": "2005-10-23",
                "name": "Mushishi",
                "vote_average": 8.5,
                "vote_count": 512,
            },
            {
                "adult": False,
                "backdrop_path": "/zyx9876backdrop.jpg",
                "genre_ids": [16, 35, 10765],
                "id": 67890,
                "origin_country": ["JP"],
                "original_language": "ja",
                "original_name": "このすば",
                "overview": "After a traffic accident, Kazuma Satou wakes up in ...",
                "popularity": 123.4,
                "poster_path": "/posterXYZ.jpg",
                "first_air_date": "2016-01-14",
                "name": "KonoSuba: God's Blessing on This Wonderful World!",
                "vote_average": 8.2,
                "vote_count": 3200,
            },
        ]

        return {"animes": animes}


if __name__ == "__main__":
    import asyncio

    async def main():
        reddit_search_tool = RedditSearchTool()
        result = await reddit_search_tool.execute(
            TMDBSearchParams(terms="Cozy")
        )
        print(result)

    asyncio.run(main())
