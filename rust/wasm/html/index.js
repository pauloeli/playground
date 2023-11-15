// Import our outputted wasm ES6 module
// Which, export default's, an initialization function
import wasmInit from "../pkg";

const runWasm = async () => {
    // Instantiate our wasm module
    const calculator = await wasmInit("../pkg/pi_bg.wasm");

    // Call the Add function export from wasm, save the result
    const addResult = calculator.add(10,20);

    // Set the result onto the body
    document.body.textContent = `The result of 10 * 20 is ${addResult}`;
};

runWasm();