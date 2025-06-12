from workflows.langgraph_workflow import run_graph

if __name__ == "__main__":
    user_input = input("Enter your query: ")
    result = run_graph(user_input)
    print(result)
