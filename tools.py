import json

from pydantic import BaseModel, Field


class ToolDefinition:
    def __init__(self, name, description, input_schema, function):
        self.name = name
        self.description = description
        self.input_schema = input_schema
        self.function = function


# teach the model how to read files
def read_file(input_data):
    # we need to tell the function about the input data format
    # we use pydentic for that
    input_dict = json.load(input_data)
    path = input_dict["path"]

    try:
        with open(path, "r") as file:
            content = file.read()
        return (content, None)
    except Exception as e:
        return "", str(e)


class ReadFileInput(BaseModel):
    path: str = Field(description="Relative path of a file in the working directory.")


read_file_definition = ToolDefinition(
    name="read_file",
    description="Reads the contents of the given relative file path. Use this when you want to see what is inside of the file. Do not use this with directory names.",
    input_schema=ReadFileInput.model_json_schema(),
    function=read_file,
)
