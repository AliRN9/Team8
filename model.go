package Team8

type Model struct {
	Task          string `json:"task"`
	Environment   string `json:"environment"`
	OptimalPlan   string `json:"optimal_plan"`
	PredictedPlan string `json:"predicted_plan"`
}
