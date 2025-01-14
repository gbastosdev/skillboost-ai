import express, { Request, Response } from 'express';
import ai_message from '../controllers/ai_controller'

const app = express();
const port = 3000;

app.get('/', (req: Request, res: Response) => {
  res.send(ai_message);
});

app.listen(port, () => {
  console.log(`Server is running at http://localhost:${port}`);
});