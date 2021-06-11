## Usage
The following steps are recommended to set up the environment (using `conda`):
```
conda create -n dqn python=3.6
```

Install `tensorpack`. This is a wrapper around `tensorflow` (very much like
`keras`). This implementation of Deep DQN uses it.
```
pip install --upgrade git+https://github.com/tensorpack/tensorpack.git
```
Now, install `tensorflow`. Supported versions are $\geq 1.5$ and $<2$.
```
pip install tensorflow==1.15
```
Alternatively, if you have a fancy GPU, you can install the release with GPU
support.
```
pip install tensorflow-gpu==1.15
```
Install dependencies by `pip install 'gym[atari]'`.
### With ALE (paper's setting):
Download an [atari rom](https://github.com/openai/atari-py/tree/gdb/atari_py/atari_roms), e.g.:
```
wget https://github.com/openai/atari-py/raw/gdb/atari_py/atari_roms/breakout.bin
```
### With gym's Atari:

Install gym and atari_py. Use `--env BreakoutDeterministic-v4` instead of the ROM file.