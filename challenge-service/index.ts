import express from "express";
import router from "./routes.ts"
const app = express()
const port = process.env.PORT || 3300

app.use(router)

app.listen(port, () => console.log("Server running under port 3300"));