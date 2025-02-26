#include "preprocessing.h"
#include <opencv2/opencv.hpp>
#include <iostream>

void preprocessImage(const std::string& inputPath, const std::string& outputPath) {
    cv::Mat image = cv::imread(inputPath, cv::IMREAD_COLOR);
    if (image.empty()) {
        std::cerr << "Image not found: " + inputPath << std::endl;
        return;
    }

    // Convert to grayscale
    cv::Mat gray;
    cv::cvtColor(image, gray, cv::COLOR_BGR2GRAY);

    // Save processed image
    cv::imwrite(outputPath, gray);
}
