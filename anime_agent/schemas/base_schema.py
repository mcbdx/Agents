from typing import Dict, Any
from pydantic import BaseModel, Field, ConfigDict

class ToolParameters(BaseModel):
    """Ensure that tools have a constrained interface."""
    model_config = ConfigDict(extra="forbid") 
    # this will allow any param, but will forbid extra params not defined

class ToolContract(BaseModel):
    """ Defines the contract for a tool"""

    name: str = Field(..., description="The name of the tool")
    description: str = Field(..., description="A brief description of the tool")
    parameters_schema: Dict[str, Any] = Field(..., description="The schema for the parameters that the tool accepts")
    strict: bool = Field(default=True, description="If True, the tool will only accept parameters defined in the schema")

    def to_json_schema(self) -> Dict[str, Any]:
        """Convert the tool contract to a JSON schema."""
        return {
            "type": "function",
            "name": self.name,
            "description": self.description,
            "parameters": self.parameters_schema,
            "strict": self.strict
        }