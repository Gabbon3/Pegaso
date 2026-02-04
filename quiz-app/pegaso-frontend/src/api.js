import axios from "axios";

const url = import.meta.env.API_BASE_URL;

console.log(`API base url ${url}`);

const api = axios.create({
    baseURL: url || "http://localhost:8000"
});

export default api;