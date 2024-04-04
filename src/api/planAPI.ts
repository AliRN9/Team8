import axios from "axios";
import {Plan} from "../model/plan.ts";

class PlanAPI {
    async post(data: Plan) {
        return axios.post(process.env.BASE_API_URL!, data)
    }


}

export default new PlanAPI()