import openai
import streamlit as st

# 1. 在代码中设置您的 OpenAI API 密钥
openai.api_key = "YOUR_API_KEY"

# 2. 定义一个翻译函数，该函数接受一段文字和源语言和目标语言作为参数，并返回翻译后的文本。
def translate(text, source_language, target_language):
    # 3. 使用 OpenAI API 调用翻译模型。
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=f"Translate the following {source_language} text into {target_language}: \n\n{text}",
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    # 4. 从 OpenAI API 的响应中提取翻译文本并返回它。
    translation = response.choices[0].text.strip()
    return translation

# 5. 使用 Streamlit 构建交互式 Web 应用程序。
def app():
    st.title("画词翻译")

    # 获取用户输入的文本和源语言。
    text = st.text_input("请输入需要翻译的文本：")
    source_language = st.selectbox(
        "请选择源语言：",
        ["英语", "中文"]
    )

    # 根据源语言选择目标语言。
    if source_language == "英语":
        target_language = "中文"
    else:
        target_language = "英语"

    # 如果有输入文本，则调用翻译函数并显示翻译结果。
    if text:
        translation = translate(text, source_language, target_language)
        st.write(f"翻译结果：{translation}")

# 6. 启动 Streamlit 应用程序。
if __name__ == "__main__":
    app()
