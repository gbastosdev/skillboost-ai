import { MongoClient, ServerApiVersion } from "mongodb"
import dotenv from 'dotenv'
import { Challenge } from '../schemas/challenges'
dotenv.config({path: 'C:/Users/GabrielBastos/Desktop/git/skillboost-ai/.env'})

const uri = process.env.MONGODB_URL_PROD;

const client = new MongoClient(uri, {
  serverApi: {
    version: ServerApiVersion.v1,
    strict: true,
    deprecationErrors: true,
  }
});

async function run(): Promise<void> {
    try {
        const database = client.db("challenges");
        // Specifying a Schema is always optional, but it enables type hinting on
        // finds and inserts
        const challenge = database.collection<Challenge>("challenge");
        console.log(challenge);
      } finally {
        await client.close();
      }
}
run().catch(console.dir);

