# Ray tracing Denoiser
A user friendly interface to denoise rendered ray traced images using Nvidia Optix or Intel OID

![screenshot](https://user-images.githubusercontent.com/20252333/173795343-c9ae5d0d-8eaa-4e1e-a80e-05b65fe8db0d.jpg)

## Features:
 - You can repeat the process if necessary.
 - You can specify the result destination.
 - It's extremely easy to use.
 - Supports Nvidia Optix (much faster but needs a Maxwell Nvidia card) and Intel OID (works on CPUs as old as Core 2 Duo)
### Use cases:
 - You rendered an image with too much noise and don't have the original files anymore.
 - You forgot to check the denoise checkbox.
 - You don't know how to use the denoise node in blender XD (and even if you do, this is easier).
### Features to be added:
- [ ] Batch Processing.
- [ ] Allow albedo and/or normal passing to the AI.
-------
![compare](https://user-images.githubusercontent.com/20252333/173801710-60e5b9e6-62d0-444b-8429-685a175dc03b.png)
-------
This is a GUI for the two implementations of Nvidia Optix and IOID by [DeclanRussell](https://github.com/DeclanRussell); [NvidiaAIDenoiser](https://github.com/DeclanRussell/NvidiaAIDenoiser), and [IntelOIDenoiser](https://github.com/DeclanRussell/IntelOIDenoiser).
Both are licenced under [MIT License](https://mit-license.org/)
