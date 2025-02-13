import express, { Request, Response } from 'express';
import AIControllerInstance from '../controllers/ai_controller'

const app = express();
const port = 3000;

app.get('/', async (req: Request, res: Response) => {
  let final_message = await AIControllerInstance.create_chat();
  res.send({"response": final_message.message.content})
});

app.listen(port, () => {
  console.log(`Server is running at http://localhost:${port}`);
});