import argparse
import os
from openai import OpenAI
from refined_seed_patterns import seed_patterns

# 初始化 OpenAI 客户端（兼容百炼）
client = OpenAI(
    api_key=os.getenv("DASHSCOPE_API_KEY"),
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
)

def text_rephrase(input_path, output_path, model):
    if not client.api_key:
        raise ValueError("未设置 DASHSCOPE_API_KEY。请设置环境变量或在代码中传入。")

    if not os.path.exists(input_path):
        raise FileNotFoundError(f"找不到输入文件: {input_path}")

    output_dir = os.path.dirname(output_path)
    if output_dir:
        os.makedirs(output_dir, exist_ok=True)

    with open(input_path, "r", encoding="utf-8") as f:
        lines = [line.strip() for line in f if line.strip()]

    allowed_actions = [k.upper() for k in seed_patterns.keys()]
    results = []

    for idx, line in enumerate(lines):
        prompt = f"""
You are a scientific protocol assistant.

Your job is to rewrite the following chemical procedure as a clear, structured, step-by-step protocol.

🔒 IMPORTANT RULES:
- You MUST use only the following action types as your step starters:
  {', '.join(allowed_actions)}
- The action must appear in ALL CAPS at the beginning of each step.
- Each step should be separated by a semicolon `;`.
- Additional details (reagents, solvents, time, temperature) can follow the action, written in normal English.
- If no chemical action is present, return: NOACTION
- If the text is in a non-English language, return: OTHERLANGUAGE

📄 Original text:
{line}

✍️ Rewritten protocol:
"""

        response = client.chat.completions.create(
            model=model,
            messages=[
                {
                    "role": "system",
                    "content": "You are a chemistry assistant converting text into standardized lab protocol format using only allowed action types."
                },
                {"role": "user", "content": prompt}
            ]
        )

        result_line = response.choices[0].message.content.strip()
        results.append(result_line)

        print(f"✅ 已处理第 {idx + 1} 行")

    with open(output_path, "w", encoding="utf-8") as f:
        for item in results:
            f.write(item + "\n")

    print(f"\n✅ 所有改写完成，结果已保存到 {output_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="逐行改写化学实验步骤")
    parser.add_argument("input", help="输入文件路径")
    parser.add_argument("output", help="输出文件路径")
    parser.add_argument(
        "--model", default="qwen-max", help="选择使用的模型（如 deepseek-r1 或 qwen-max）"
    )
    args = parser.parse_args()

    text_rephrase(args.input, args.output, args.model)
