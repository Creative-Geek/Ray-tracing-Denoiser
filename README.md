# Ray tracing Denoiser
A user friendly interface to denoise rendered ray traced images using Nvidia Optix or Intel OID

![screenshot](https://user-images.githubusercontent.com/20252333/185997472-aeac3cc2-ebf6-4387-9aa1-b77e3a3e3c17.png)

## Features:
 - You can repeat the process if necessary.
 - You can pass the first sample albedo and normals to the AI for better results.
 - You can specify the result destination.
 - It's extremely easy to use.
 - Supports Nvidia Optix (much faster but needs a Maxwell Nvidia card) and Intel OID (works on CPUs as old as Core 2 Duo)
### Usage:
1. Browse for a noisy photo OR drag 'n' drop it on the interface.
2. Choose the AI engine as per the above feature list.
3. Choose the output location
4. Specify the repeat count (1 is almost always enough, maybe 2 if the AI missed a spot or two. any more is mostly wasteful)
5. Hit start (it takes from 0.01 of a second up all the way to a minute depending on your PC)
### Use cases:
 - You rendered an image with too much noise and don't have the original files anymore.
 - You forgot to check the denoise checkbox.
 - You don't know how to use the denoise node in blender XD (and even if you do, this is easier).
### Features to be added:
- [ ] Batch Processing.
- [x] ~~Allow albedo and/or normal passing to the AI~~.
-------
![compare](https://user-images.githubusercontent.com/20252333/173801710-60e5b9e6-62d0-444b-8429-685a175dc03b.png)
-------
This is a GUI for the two implementations of Nvidia Optix and IOID by [DeclanRussell](https://github.com/DeclanRussell); [NvidiaAIDenoiser](https://github.com/DeclanRussell/NvidiaAIDenoiser), and [IntelOIDenoiser](https://github.com/DeclanRussell/IntelOIDenoiser).
Both are licenced under [MIT License](https://mit-license.org/)
