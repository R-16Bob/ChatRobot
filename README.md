# ChatRobot 

## 概述

ChatRobot 是一个基于 Streamlit 和 LangChain 的聊天机器人应用。用户可以通过网页界面与 AI 进行对话，AI 使用 OpenAI 的 GPT-4o-mini 模型来生成回复。项目支持对话历史的保存和清除功能。

## 使用方法

1. **克隆仓库**

   ```bash
   git clone https://github.com/your-username/ChatRobot.git
   cd ChatRobot
   ```


2. **安装依赖**

   ```bash
   conda env create -f environment.yml
   ```

3. **设置 OpenAI API 密钥**

   设置系统环境变量 `OPENAI_API_KEY`

   ```plaintext
   OPENAI_API_KEY=your_openai_api_key
   ```
   注意：我使用了base_url，请根据需要自行修改代码。 


4.  **启动应用**

   在项目根目录下运行以下命令启动 Streamlit 应用：

   ```bash
   streamlit run main.py
   ```


### 功能介绍

- **发送消息**：在输入框中输入消息并点击发送按钮，AI 将生成回复。
- **查看对话历史**：所有对话历史将显示在聊天窗口中。
- **清除对话历史**：点击“清除对话历史”按钮，将清空当前对话记录并重置对话状态。

## 代码结构

```
ChatRobot/
├── main.py           # 前端聊天网页
├── utils.py          # 后端对话
└── environment.yml  # 环境依赖
```




## 未来计划


