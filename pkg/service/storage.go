package service

import (
	"context"
	"fmt"
	"io"
	"os"

	"cloud.google.com/go/storage"
)

// Upload ...
func Upload(file, bucket, object string) (string, error) {

	ctx := context.Background()

	client, err := storage.NewClient(ctx)

	if err != nil {
		return "", err
	}

	f, err := os.Open(file)

	if err != nil {
		return "", err
	}

	defer f.Close()

	wc := client.Bucket(bucket).Object(object).NewWriter(ctx)

	_, err = io.Copy(wc, f)

	if err != nil {
		return "", err
	}

	err = wc.Close()

	if err != nil {
		return "", err
	}

	return fmt.Sprintf("https://storage.googleapis.com/h-mandiola-files/%v", object), nil
}
