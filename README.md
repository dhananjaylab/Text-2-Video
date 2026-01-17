# Text-to-Video Generation with Stable Diffusion

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Stars](https://img.shields.io/github/stars/dhananjaylab/Text-2-Video?style=social)](https://github.com/dhananjaylab/Text-2-Video)
[![Forks](https://img.shields.io/github/forks/dhananjaylab/Text-2-Video?style=social)](https://github.com/dhananjaylab/Text-2-Video)

A cutting-edge AI project demonstrating text-to-video synthesis using Stable Diffusion. This repository showcases advanced skills in generative AI, computer vision, and Python development, leveraging cross-frame attention and motion warping for coherent video outputs. Ideal for recruiters seeking expertise in PyTorch, Hugging Face Transformers, and diffusion models.

## 🚀 Features
- **Frame-Level Prompting**: Generate videos from sequential text descriptions.
- **Customizable Outputs**: Adjustable FPS, resolution, and motion strengths.
- **CLI & File Support**: Flexible input via command-line or prompt files.
- **GPU-Optimized**: Efficient inference on CUDA-compatible hardware.
- **Safety Checks**: Integrated NSFW filtering for responsible AI.

## 🛠 Technologies Used
- **Python 3.8+**: Core language for scripting and pipelines.
- **PyTorch**: Deep learning framework for model training/inference.
- **Hugging Face Diffusers**: Stable Diffusion pipeline integration.
- **Transformers & Accelerate**: Model loading and optimization.
- **ImageIO & OpenCV**: Video encoding and processing.
- **NumPy & PIL**: Image manipulation.

## 📋 Prerequisites
- Python 3.8 or higher.
- CUDA-compatible GPU (e.g., NVIDIA with cu118) for optimal performance.
- At least 8GB VRAM recommended.

## 🏃 Quick Start

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/dhananjaylab/Text-2-Video.git
   cd Text-2-Video
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Application**:
   - Default example (hummingbird video):
     ```bash
     python run_t2v.py
     ```
   - Custom prompts (e.g., running dogs):
     ```bash
     python run_t2v.py --prompt_file sample_video/running_dogs.txt --output dogs_video.mp4 --fps 8
     ```
   - Output: MP4 video saved to the specified file.

4. **Via Google Colab**:
   - Open `working_notebook.ipynb` in Colab.
   - Follow the notebook cells for setup and execution.

## 🎥 Demo
Check out sample videos generated from this pipeline:
- [Hummingbird and Flowers](https://example.com/hummingbird_video.mp4) (placeholder link – upload to GitHub Releases or YouTube).
- [Running Dogs](https://example.com/dogs_video.mp4).
- [Cheetah Sprint](https://example.com/cheetah_video.mp4).

Screenshots of generated frames:
![Sample Frame](https://via.placeholder.com/512x512.png?text=Sample+Video+Frame) (Replace with actual image).

## 🏗 How It Works
1. **Prompt Encoding**: Text prompts are tokenized and embedded using CLIP.
2. **Diffusion Process**: Stable Diffusion generates initial frames with cross-frame attention for temporal coherence.
3. **Motion Warping**: Applies optical flow-based warping for smooth transitions.
4. **Video Assembly**: Frames are stitched into MP4 using ImageIO.

Key components:
- `t2v_main.py`: Custom pipeline class extending Stable Diffusion for video.
- `run_t2v.py`: CLI entry point with argument parsing.
- `sample_video/`: Predefined prompt sequences.

## 🤝 Contributing
We welcome contributions! See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.
- Fork the repo and submit PRs.
- Report bugs or suggest features via Issues.

## 📄 License
This project is licensed under the MIT License – see [LICENSE](LICENSE) for details.

## 👨‍💻 About the Author
Built by [Dhananjay Lab](https://github.com/dhananjaylab) as a showcase of AI engineering skills. Passionate about generative models, open-source, and scalable ML solutions. Connect on [LinkedIn](https://linkedin.com/in/dhananjaylab) or email for opportunities.
