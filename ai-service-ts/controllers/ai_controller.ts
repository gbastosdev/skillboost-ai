import { HfInference } from "@huggingface/inference";
import dotenv from 'dotenv'
dotenv.config({path: 'C:/Users/GabrielBastos/Desktop/git/skillboost-ai/.env'})

const client = new HfInference(process.env.HF_KEY);

async function chat(){
  return await client.chatCompletion({
    model: "Qwen/QwQ-32B-Preview",
    messages: [
      {
        role: "user",
        content: "Create a simple monthly challenge to developers. This is aimed to enhance experience to devs. Keep in mind that you have to provide this challenge the finest way to the developers."
      }
    ],
    max_tokens: 500
  });
} 

export default chat()