import json


def execute_python_code(python_code) -> str:
    """
    Executes the given Python code and returns the result.
    the python code should define the 'evaluate' function.
    """
    try:
        context = {}
        exec(python_code, {}, context)
        evaluate = context.get("evaluate")

        if not evaluate:
            raise ValueError(
                "The 'evaluate' function is not defined in the Python code."
            )

        result = context["evaluate"]()
        return json.dumps(result)
    except Exception as e:
        raise RuntimeError(f"Error executing Python code: {e}")
