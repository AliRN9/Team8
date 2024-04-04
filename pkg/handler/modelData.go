package handler

import (
	"bytes"
	"encoding/json"
	"fmt"
	"github.com/gin-gonic/gin"
	Team8 "middlewareGolang"
	"net/http"
)

func (h *Handler) getPredict(c *gin.Context) {
	var model Team8.Model

	if err := c.ShouldBindJSON(&model); err != nil {
		newErrorResponse(c, http.StatusBadRequest, err.Error())
		return
	}

	answer, err := sendModelToApp(model)
	if err != nil {
		newErrorResponse(c, http.StatusBadRequest, err.Error())
		return
	}

	type Response struct {
		Status string `json:"status"`
	}

	var response Response
	err = json.Unmarshal(answer, &response)
	if err != nil {
		newErrorResponse(c, http.StatusBadRequest, err.Error())
		return
	}

	c.JSON(http.StatusOK, response)
}

const URL = "*"
const ContentType = "application/json"

func sendModelToApp(model Team8.Model) ([]byte, error) {
	jsonData, err := json.Marshal(model)
	if err != nil {
		return nil, fmt.Errorf("error marshaling JSON")
	}

	resp, err := http.Post(URL, ContentType, bytes.NewBuffer(jsonData))
	if err != nil {
		return nil, fmt.Errorf("error sending model to app")
	}

	defer resp.Body.Close()

	var responseBody []byte
	decoder := json.NewDecoder(resp.Body)
	if err := decoder.Decode(&responseBody); err != nil {
		return nil, fmt.Errorf("error decoding response")
	}

	return jsonData, nil
}
