import express, { Request, Response } from 'express';
import ai_message from '../controllers/ai_controller'

const app = express();
const port = 3000;

app.get('/', (req: Request, res: Response) => {
  var final_message = String()
  ai_message.then((async (result)=>{
    final_message = await result.choices[0].message.content 
    res.send({"AI_Message": final_message});
  }))
  
});

app.listen(port, () => {
  console.log(`Server is running at http://localhost:${port}`);
});