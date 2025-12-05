from langchain.messages import HumanMessage
from osmnx import plot_graph
from graph import make_graph

async def main():

    checkpointer = InMemoryStore()

    graph = make_graph(
        checkpointer=checkpointer,
        plot_graph=True
    )

    init_state = {"messages" : HumanMessage(content="")}  # fill this

    result = []

    async for chunk in graph.astream(init_state, config={"thread_id": "1"}):
        if chunk.content:
            print(chunk.content)  # NOTE: this is badly written, we would see al stream chunks
            result.append(chunk.content)

    


