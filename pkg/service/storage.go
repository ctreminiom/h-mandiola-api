package service

import (
	"context"
	"io"
	"os"

	"cloud.google.com/go/storage"
)

// Upload ...
func Upload(file, bucket, object string) error {

	ctx := context.Background()

	client, err := storage.NewClient(ctx)

	if err != nil {
		return err
	}

	f, err := os.Open(file)

	if err != nil {
		return err
	}

	defer f.Close()

	wc := client.Bucket(bucket).Object(object).NewWriter(ctx)

	_, err = io.Copy(wc, f)

	if err != nil {
		return err
	}

	err = wc.Close()

	if err != nil {
		return err
	}

	return nil
}
