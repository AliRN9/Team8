import axios from "axios";
import {Plan} from "../model/plan.ts";

class PlanAPI {
    async post(data: Plan) {
        const response = await axios.post("http://localhost:8080/api/predict", data, {
            withCredentials: true
        })

        return response
    }

    async getData() {
        return await axios.get("https://jsonplaceholder.typicode.com/todos/1")
    }
}

export default new PlanAPI()