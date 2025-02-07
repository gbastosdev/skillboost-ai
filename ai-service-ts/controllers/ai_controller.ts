import { HfInference } from "@huggingface/inference";
import dotenv from 'dotenv'
import path from 'path'
dotenv.config({ path: path.resolve(__dirname, '../../.env')})

const client = new HfInference(process.env.HF_KEY);

async function chat(){
  return await client.chatCompletion({
    model: "Qwen/QwQ-32B-Preview",
    messages: [
      {
        role: "user",
        content: "Create a simple monthly challenge to developers. This is aimed to enhance experience to devs. Also, you have to generate this text on a concise way with few lines. Generate this message on english version."
      }
    ],
    max_tokens: 500
  });
} 

export default chat()