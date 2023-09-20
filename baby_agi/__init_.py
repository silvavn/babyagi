class BabyAGI:
    """
    A class representing a baby artificial general intelligence agent.
    """

    def __init__(self, **kwargs):
        """
        Args:
            vectordb_client (object): The vectordb client.
            AGENT_NAME (str): The name of the agent.
            OBJECTIVE (str): The objective of the agent.
            INITIAL_TASK (str): The initial task of the agent.
            LLM_MODEL (str): The LLM model alias being used to control the agent.
            LLAMA_API_PATH (str): The path to the llama api.
        """
        for key, value in kwargs.items():
            setattr(self, key, value)

    # prints the BabyAGI configuration
    def print_config(self):
        print("\033[95m\033[1m" + "\n*****CONFIGURATION*****\n" + "\033[0m\033[0m")
        print(f"Name  : {self.AGENT_NAME}")
        print(f"LLM   : {self.LLM_MODEL}")
        print(f"Objective  : {self.OBJECTIVE}")
