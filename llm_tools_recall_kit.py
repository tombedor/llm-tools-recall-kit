import llm


class RecallKit(llm.Toolbox):
    def create_memory(self, input: str) -> str:
        """
        Description of tool goes here.
        """
        return f"hello {input}"





@llm.hookimpl
def register_tools(register):
    register(RecallKit)
