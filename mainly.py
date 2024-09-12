from components.state import graph

while True:
    query = input("Q:")
    result = graph.invoke({
        "input":query
    })
    print(result['answer'])