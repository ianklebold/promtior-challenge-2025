def get_response_by_query_and_chain(chain, question):
    return chain.invoke({"input": question})["answer"]

def execute_generation_step(chain, question):
    return get_response_by_query_and_chain(chain, question)