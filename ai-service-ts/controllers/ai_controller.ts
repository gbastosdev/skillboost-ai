import axios from 'axios'

class AIController{

  requestObject = {}
  constructor(){
    this.requestObject = {
      model: "tinyllama",
      messages: [{
          role: "user",
          content: "Create a simple monthly challenge to developers. Create this challenge with less than 500 characters."
        }],
      headers: {
        'Content-Type': 'application/json'
      },
      stream: false
    }
  }

  public async create_chat(){
    try {
      const {data, status} = await axios.post('http://localhost:11432/api/chat', this.requestObject)
      console.log('Status returned:', status)
      return data
    } catch (error) {
      if (axios.isAxiosError(error)) {
        console.log('error message: ', error.message);
        return error.message;
      } else {
        console.log('unexpected error: ', error);
        return 'An unexpected error occurred';
      }
    }
  } 
}

const AIControllerInstance = new AIController();

export default AIControllerInstance;
