package service

type Model interface {
}

type Service struct {
	Model
}

func NewService() *Service {
	return &Service{
		Model: NewModelService(),
	}
}
