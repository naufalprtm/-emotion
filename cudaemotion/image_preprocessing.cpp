#include <iostream>
#include <opencv2/opencv.hpp>

__global__ void grayscaleKernel(unsigned char* img, unsigned char* output, int width, int height) {
    int x = blockIdx.x * blockDim.x + threadIdx.x;
    int y = blockIdx.y * blockDim.y + threadIdx.y;
    if (x < width && y < height) {
        int index = (y * width + x) * 3;
        unsigned char r = img[index];
        unsigned char g = img[index + 1];
        unsigned char b = img[index + 2];
        output[y * width + x] = (r + g + b) / 3; // Simple grayscale conversion
    }
}

void preprocessImage(const cv::Mat& img) {
    int width = img.cols;
    int height = img.rows;
    unsigned char *d_img, *d_output;
    unsigned char *h_output = new unsigned char[width * height];

    cudaMalloc(&d_img, width * height * 3);
    cudaMalloc(&d_output, width * height);

    cudaMemcpy(d_img, img.data, width * height * 3, cudaMemcpyHostToDevice);

    dim3 blockSize(16, 16);
    dim3 gridSize((width + blockSize.x - 1) / blockSize.x, (height + blockSize.y - 1) / blockSize.y);
    grayscaleKernel<<<gridSize, blockSize>>>(d_img, d_output, width, height);
    
    cudaMemcpy(h_output, d_output, width * height, cudaMemcpyDeviceToHost);

    // Process the output as needed...
    
    cudaFree(d_img);
    cudaFree(d_output);
    delete[] h_output;
}

int main() {
    cv::Mat img = cv::imread("input.jpg");
    preprocessImage(img);
    return 0;
}