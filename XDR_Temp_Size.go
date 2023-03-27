package main

import (
	"fmt"
	"io/ioutil"
	"log"
	"os"
	"path/filepath"
	"strings"
	"time"

	"github.com/karrick/godirwalk"
)

func main() {
	// Define the folder to scan
	folderToScan := "C:\\Users"

	// Define the output file path
	outputFolder := "C:\\Temp\\CortexXDR"
	if _, err := os.Stat(outputFolder); os.IsNotExist(err) {
		os.Mkdir(outputFolder, 0755)
	}
	hostname, err := os.Hostname()
	if err != nil {
		log.Fatal(err)
	}
	outputFile := filepath.Join(outputFolder, fmt.Sprintf("%s_output.txt", hostname))

	// Define the headers for the output file
	headers := "Path|Filename|File Creation|File Size"

	// Initialize the total size variable
	totalSize := int64(0)

	// Walk through each file and folder
	err = godirwalk.Walk(folderToScan, &godirwalk.Options{
		Callback: func(osPathname string, de *godirwalk.Dirent) error {
			if !de.IsRegular() {
				return nil
			}

			// Get the file path
			filePath := filepath.Dir(osPathname)

			// Get the file name
			fileName := filepath.Base(osPathname)

			// Get the file creation time
			fileCreationTime := de.ModTime().Format("2006-01-02 03:04:05 PM")

			// Get the file size in bytes
			fileSize := de.Size()

			// Convert the file size to a human-readable format
			sizeSuffixes := []string{"B", "KB", "MB", "GB", "TB"}
			sizeSuffixIndex := 0
			for fileSize > 1024 && sizeSuffixIndex < len(sizeSuffixes)-1 {
				fileSize /= 1024
				sizeSuffixIndex++
			}
			fileSizeString := fmt.Sprintf("%d%s", fileSize, sizeSuffixes[sizeSuffixIndex])

			// Update the total size
			totalSize += de.Size()

			// Write the file info to the output file
			fileInfo := fmt.Sprintf("%s|%s|%s|%s\n", filePath, fileName, fileCreationTime, fileSizeString)
			err := ioutil.WriteFile(outputFile, []byte(fileInfo), 0644)
			if err != nil {
				log.Fatalf("Error writing file info to output file: %v\n", err)
			}

			return nil
		},
		ErrorCallback: func(osPathname string, err error) godirwalk.ErrorAction {
			log.Printf("Error scanning %q: %v\n", osPathname, err)
			return godirwalk.SkipNode
		},
		Unsorted: true, // Traverse the directory in an arbitrary order
	})
	if err != nil {
		log.Fatalf("Error scanning directory: %v\n", err)
	}

	// Convert the total size to a human-readable format
	sizeSuffixes := []string{"B", "KB", "MB", "GB", "TB"}
	sizeSuffixIndex := 0
	for totalSize > 1024 && sizeSuffixIndex < len(sizeSuffixes)-1 {
		totalSize /= 1024
		sizeSuffixIndex++
	}
	totalSizeString := fmt.Sprintf("%d%s", totalSize, sizeSuffixes[sizeSuffixIndex])

	// Write the total size to the output file
