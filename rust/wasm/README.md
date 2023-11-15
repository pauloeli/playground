# wasm-multiplication

A simple Rust project that demonstrates using WebAssembly with `wasm_bindgen` to expose a multiplication function to JavaScript.

Based on [Wasm By Example](https://wasmbyexample.dev/examples/hello-world/hello-world.rust.en-us.html)

## Building the Project

### Prerequisites

- [Rust](https://www.rust-lang.org/tools/install)
- [wasm-pack](https://rustwasm.github.io/wasm-pack/installer/)
- [Node.js](https://nodejs.org/)

### Build Steps

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/wasm-multiplication.git
    cd wasm-multiplication
    ```

2. Build the Rust project:

    ```bash
    wasm-pack build --target web 
    ```

## Running the Example

1. Open your web browser and open [index.html](html/index.html)