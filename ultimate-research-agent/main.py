from llm import llm


def main():
    print("The Ultimate Research Agent")
    print("Tell me, how can I help you?")

    response = llm.invoke("Introduce yourself in one line")

    print("Response")
    print(response.content)


if __name__ == "__main__":
    main()