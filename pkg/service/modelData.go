package service

type ModelService struct{}

func NewModelService() *ModelService {
	return &ModelService{}
}

func (s *ModelService) GetStatus(jsonInput []byte) {}
