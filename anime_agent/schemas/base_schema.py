from typing import Dict, Any, TypeVar, Generic, Type
from pydantic import BaseModel, Field, ConfigDict
from abc import ABC, abstractmethod

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

T = TypeVar('T', bound=ToolParameters) # an instance of subtype ToolParameters

class BaseTool(ABC, Generic[T]):
    """Abstract base class for all tools."""

    def __init__(self):
        self.contract = self._create_contract()

    # tools should be of type base tool, but have parameters of type ToolParameters 

    @property # means this will be a read-only attribute 
    @abstractmethod
    def name(self) -> str: ...

    @property
    @abstractmethod
    def description(self) -> str: ...

    @property
    @abstractmethod
    def parameters(self) -> Type[T]: ... # Type[T] means we use the class object itself and not the instance

    @abstractmethod
    async def execute(self, params: T) -> Dict[str, Any]: ...
    # meaning this will get an argument of type T params and return a dictionary of any type "K": Any

    def _create_contract(self) -> ToolContract:
        """ auto generate contract from pydantic model on instantiation """
        return ToolContract(
            name=self.name,
            description=self.description,
            parameters_schema=self.parameters.model_json_schema(),
            strict=True
        )