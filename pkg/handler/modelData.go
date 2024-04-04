package handler

import (
	"encoding/json"
	"fmt"
	"github.com/gin-gonic/gin"
	"math/rand"
	Team8 "middlewareGolang"
	"net/http"
	"time"
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
	type Response struct {
		Status string `json:"Status"`
	}

	source := rand.NewSource(time.Now().UnixNano())
	random := rand.New(source)
	number := random.Intn(11)

	var response Response
	if number > 5 {
		response = Response{
			Status: "1",
		}
	} else {
		response = Response{
			Status: "0",
		}
	}

	jsonData, err := json.Marshal(response)
	if err != nil {
		fmt.Println("Ошибка при маршалинге JSON:", err)
		return nil, nil
	}

	return jsonData, nil

	//jsonData, err := json.Marshal(model)
	//if err != nil {
	//	return nil, fmt.Errorf("error marshaling JSON")
	//}
	//
	//resp, err := http.Post(URL, ContentType, bytes.NewBuffer(jsonData))
	//if err != nil {
	//	return nil, fmt.Errorf("error sending model to app")
	//}
	//
	//defer resp.Body.Close()
	//
	//var responseBody []byte
	//decoder := json.NewDecoder(resp.Body)
	//if err := decoder.Decode(&responseBody); err != nil {
	//	return nil, fmt.Errorf("error decoding response")
	//}
	//
	//return jsonData, nil
}
