from typing import Dict, Any 
from schemas.base_schema import BaseTool
from schemas.tool_schemas import WeatherParams

class WeatherTool(BaseTool[WeatherParams]):
    name = "get_weather" # this is the function name
    description = "Fetches current weather given a location"
    parameters = WeatherParams # this is the class itself 

    # implement the execution 
    async def execute(self, params: WeatherParams) -> Dict[str, Any]:
        # mock data 
        temp = "22C" if params.units == "celsius" else "72F"

        return {
            "location": params.location,
            "units": params.units, 
            "temperature": temp,
            "condition": "Sunny",
            "humidity": "65%"
        }
    
if __name__ == "__main__":
    import asyncio

    async def main():
        get_weather = WeatherTool()
        print(get_weather.contract.model_dump_json())
        result = await get_weather.execute(WeatherParams(location="Bogota",units="celsius"))
        print(result)

    asyncio.run(main())

     

