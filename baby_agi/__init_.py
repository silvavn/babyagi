class BabyAGI:
    class BabyAGI:
        """
        A class representing a baby artificial general intelligence agent.
        """
        def __init__(self, **kwargs):
            """
                Args:
                    vectordb_client (object): The vectordb client.
                    INSTANCE_NAME (str): The name of the agent.
                    COOPERATIVE_MODE (str): The cooperative mode of the agent.
                    OBJECTIVE (str): The objective of the agent.
                    INITIAL_TASK (str): The initial task of the agent.
                    LLM_MODEL (str): The LLM model of the agent.
            """
            for key, value in kwargs.items():
                setattr(self, key, value)

    # function to set up chromadb client
    @property
    def vectordb_client(self):
        return self._vectordb_client
    
    @vectordb_client.setter
    def vectordb_client(self, value):
        self._vectordb_client = value
    
    # function to set up LLM model
    @property
    def LLM_MODEL(self):
        return self._LLM_MODEL
    
    @LLM_MODEL.setter
    def LLM_MODEL(self, value):
        self._LLM_MODEL = value

    # prints the BabyAGI configuration
    def print_config(self):
        print("\033[95m\033[1m" + "\n*****CONFIGURATION*****\n" + "\033[0m\033[0m")
        print(f"Name  : {self.INSTANCE_NAME}")
        print(f"LLM   : {self.LLM_MODEL}")