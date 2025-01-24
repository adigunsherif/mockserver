import json


def execute_python_code(python_code: str, response_body: str) -> str:
    """
    Executes the given Python code on the response_body.
    """

    execution_env = {
        "response_body": response_body,
        "json": json,
        "transformed_response": None,
    }

    try:
        exec(python_code, {}, execution_env)
        transformed_response = execution_env.get("transformed_response")

        if transformed_response is None:
            raise ValueError("Python code did not set 'transformed_response'")

        return transformed_response
    except Exception as e:
        pass
