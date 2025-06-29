def build_prompt(transcript: str) -> str:
    return (
        "You are an AI assistant helping summarize business meetings.\n"
        "Given the following transcript, do two things:\n"
        "1. Summarize the key discussion points.\n"
        "2. Extract action items with owner names and deadlines if available.\n\n"
        #f"Transcript:\n{transcript}\n\n"
        "Output in this format:\n"
        "Summary:\n...\n\n Most traditional AI models are built by using machine learning, which requires a large,"
        "\n structured, well-labeled data set that encompasses a specific task that you want to tackle."
        " \nOften these datasets must be sourced, curated, and labeled by hand, a job that requires people with domain knowledge "
        "and takes time." "\n After it is trained, a traditional AI model can do a single task well. The traditional AI model uses"
        "what it learns from patterns in the training data to predict outcomes in unknown data."
        " \n You can create machine learning models for your specific use cases with tools like AutoAI and Jupyter notebooks, and ""\nthen deploy them."
        "\nIn contrast, foundation models are trained on large, diverse, unlabeled \ndatasets and can be used for many different tasks. Foundation models were first used to generate text by calculating the most-probable next word in natural language translation tasks.\n However, model providers are learning that, when prompted with the right input, foundation models can do various other tasks well.\n Instead of creating your own foundation models, you use existing deployed models and \nengineer prompts to generate the results that you need."
    )