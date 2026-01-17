"""
CLI script for running Text-to-Video generation.
Loads prompts from file, initializes pipeline, and generates video.
"""

import torch
import imageio
import argparse
from t2v_main import T2VPipeline

def load_prompts(file_path):
    """
    Load prompts from a text file.
    
    Args:
        file_path (str): Path to the file containing prompts.
    
    Returns:
        list: List of prompt strings.
    """
    with open(file_path, 'r') as f:
        content = f.read()
        # Simple parsing for list format
        prompts = eval(content.split('=')[1].strip())
    return prompts

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate video from text prompts using Stable Diffusion.")
    parser.add_argument('--prompt_file', type=str, default='sample_video/hummingbird_and_flowers.txt', help='Path to prompt file.')
    parser.add_argument('--output', type=str, default='video_out.mp4', help='Output video file name.')
    parser.add_argument('--fps', type=int, default=5, help='Frames per second for output video.')
    args = parser.parse_args()

    prompts = load_prompts(args.prompt_file)
    
    model_id = "runwayml/stable-diffusion-v1-5"
    pipe = T2VPipeline.from_pretrained(model_id, torch_dtype=torch.float16).to("cuda")
    
    result = pipe(prompt=prompts, generator=torch.Generator('cuda').manual_seed(10)).images
    result = [(r * 255).astype("uint8") for r in result]
    imageio.mimsave(args.output, result, fps=args.fps)

    prompts = load_prompts(args.prompt_file)
    
    model_id = "runwayml/stable-diffusion-v1-5"
    pipe = T2VPipeline.from_pretrained(model_id, torch_dtype=torch.float16).to("cuda")
    
    result = pipe(prompt=prompts, generator=torch.Generator('cuda').manual_seed(10)).images
    result = [(r * 255).astype("uint8") for r in result]
    imageio.mimsave(args.output, result, fps=args.fps)
