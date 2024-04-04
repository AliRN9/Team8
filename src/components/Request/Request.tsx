import {useState} from "react";
import {Plan} from "../../model/plan.ts"
import classes from "./Request.module.css"
import "./SuccessMark.css"
import "./FailedMark.css"
import {mockEnvironment, mockOptimalPlan, mockPredictedPlan, mockTask} from "./mockData.ts";
import planAPI from "../../api/planAPI.ts";

const Request = () => {
    const [task, setTask] = useState<string>("");
    const [environment, setEnvironment] = useState<string>("");
    const [optimalPlan, setOptimalPlan] = useState<string>("");
    const [predictedPlan, setPredictedPlan] = useState<string>("");
    const [responseStatus, setResponseStatus] = useState<number>(-1);

    const asyncSendData = async () => {
        const data = toResponseData();
        const response = await planAPI.post(data);
        if ("status" in response.data) {
            console.log(response.data.status)
            setResponseStatus(response.data.status);
        }
    }

    const toResponseData = (): Plan => {
        return {
            task: task,
            environment: environment,
            optimal_plan: optimalPlan,
            predicted_plan: predictedPlan
        }
    }

    const fillInTheFields = () => {
        setTask(mockTask)
        setEnvironment(mockEnvironment)
        setOptimalPlan(mockOptimalPlan)
        setPredictedPlan(mockPredictedPlan)
    }

    return (
        <div className={classes.request}>
            <h1>The team 8 model</h1>
            <input placeholder={"Task"} value={task} onChange={(e) => setTask(e.target.value)}/>
            <input placeholder={"Environment"} value={environment} onChange={(e) => setEnvironment(e.target.value)}/>
            <input placeholder={"Optimal plan"} value={optimalPlan} onChange={(e) => setOptimalPlan(e.target.value)}/>
            <input placeholder={"predicted plan"} value={predictedPlan}
                   onChange={(e) => setPredictedPlan(e.target.value)}/>
            <button className={classes.sendButton} onClick={() => asyncSendData()}>Send</button>
            <button className={classes.fillButton} onClick={() => fillInTheFields()}>Fill in the fields</button>
            {responseStatus == 1 &&
                <div className="success-checkmark">
                    <div className="check-icon">
                        <span className="icon-line line-tip"></span>
                        <span className="icon-line line-long"></span>
                        <div className="icon-circle"></div>
                        <div className="icon-fix"></div>
                    </div>
                </div>
            }
            {responseStatus == 0 &&
                <div className="cross">
                    <div className="line line1"></div>
                    <div className="line line2"></div>
                    <div className="circle"></div>
                </div>
            }
        </div>
    );
};

export default Request;