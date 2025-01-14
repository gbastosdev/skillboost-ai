import { HfInference } from "@huggingface/inference";
import dotenv from 'dotenv'
dotenv.config({path: 'C:/Users/GabrielBastos/Desktop/git/skillboost-ai/.env'})

const client = new HfInference();

async function chat(){
  return await client.chatCompletion({
    model: "Qwen/QwQ-32B-Preview",
    messages: [
      {
        role: "user",
        content: "What is the capital of France?"
      }
    ],
    max_tokens: 500
  });
} 

var final_result = chat().then((result)=>{
  console.log(result.choices[0].message)
})

export default final_result