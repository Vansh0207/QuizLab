import dotenv from "dotenv";
dotenv.config();

import express from "express";
import cors from "cors";
import cookieParser from "cookie-parser";
import connectDB from "./utils/db.js";
import userRoutes from "./routes/user.routes.js";
import videoRoutes from "./routes/video.routes.js";
import questionRoutes from "./routes/question.routes.js";
import { app, server } from "./socket/socket.js";

const PORT = process.env.PORT || 8000;

//middlewares
app.use(express.json());
app.use(cookieParser());
app.use(express.urlencoded({ extended: true }));

const corsOptions = {
  origin: process.env.URL || "http://localhost:5173",
  credentials: true,
};
app.use(cors(corsOptions));

app.use("/api/user", userRoutes);
app.use("/api/video", videoRoutes);
app.use("/api/question", questionRoutes);

server.listen(PORT, () => {
  connectDB();
  console.log(`Server listen at port ${PORT}`);
});
