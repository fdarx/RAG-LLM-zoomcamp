INSTRUCTIONS = """
Your task is to answer questions from the course participants
based on the provided context.

Answer the QUESTION using only the facts in CONTEXT. 
If the CONTEXT does not contain information relevant to answering the QUESTION, respond with exactly: 'I don't know based on the provided context.'
 Do not use any outside knowledge, even if you know the answer.
Use the context to find relevant information and provide
accurate answers. If the answer is not found in the context,
respond with "I don't know.
BE VERY SPECIFIC EVEN IF THERE IS DIFFERENCE OF LETTER YOU ARE NOT SUPPOSED TO ASSUME ANYTHING 
"
""".strip()

PROMPT_TEMPLATE = """
QUESTION: {question}

CONTEXT: {context}
""".strip()


class RAGBase:
    def __init__(
        self,
        index,
        llm_client,
        instructions=INSTRUCTIONS,
        prompt_template=PROMPT_TEMPLATE,
        course="llm-zoomcamp",
        model="gemini-3.1-flash-lite",
    ):
        self.index = index
        self.llm_client = llm_client
        self.instructions = instructions
        self.course = course
        self.prompt_template = prompt_template
        self.model = model

    def search(self, question):
        boost_dict = {"question": 3.0, "section": 0.5}
        filter_dict = {"course": self.course}

        return self.index.search(
            question,
            boost_dict=boost_dict,
            filter_dict=filter_dict,
            num_results=5,
        )

    def build_context(self, search_results):
        context_parts = []
        for doc in search_results:
            context_parts.append(
                f"Section: {doc['section']}\n"
                f"Question: {doc['question']}\n"
                f"Answer: {doc['answer']}"
            )
        return "\n\n".join(context_parts)

    def build_prompt(self, question, search_results):
        context = self.build_context(search_results)
        return self.prompt_template.format(question=question, context=context)

    def llm(self, prompt):
        response = self.llm_client.models.generate_content(
            model=self.model,
            contents=prompt,
            config={"system_instruction": self.instructions},
        )
        return response.text

    def rag(self, question):
        search_results = self.search(question)
        prompt = self.build_prompt(question, search_results)
        return self.llm(prompt)